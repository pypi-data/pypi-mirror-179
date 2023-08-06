import os
import shutil
import subprocess
import time

import allure
import wda

from qrunner.core.ios.common import get_device_list, get_tcp_port, get_current_device
from qrunner.core.ios.element import IosElement
from qrunner.utils.config import config
from qrunner.utils.exceptions import DeviceNotFoundException, ScreenFailException
from qrunner.utils.log import logger


def _start_wda_xctest(udid: str, port, wda_bundle_id=None) -> bool:
    xctool_path = shutil.which("tidevice")
    logger.info(
        f"WDA is not running, exec: {xctool_path} -u {udid} wdaproxy --port {port} -B {wda_bundle_id}"
    )
    args = []
    if udid:
        args.extend(["-u", udid])
    args.append("wdaproxy")
    args.extend(["--port", str(port)])
    if wda_bundle_id is not None:
        args.extend(["-B", wda_bundle_id])
    p = subprocess.Popen([xctool_path] + args)
    time.sleep(3)
    if p.poll() is not None:
        logger.warning("xctest launch failed")
        return False
    return True


class IosDriver(object):
    # _instance = {}
    #
    # def __new__(cls, serial_no=None, bundle_id=None):
    #     if serial_no not in cls._instance:
    #         cls._instance[serial_no] = super().__new__(cls)
    #     return cls._instance[serial_no]

    def __init__(self, serial_no=None, bundle_id=None):
        if serial_no is None:
            self.serial_no = get_current_device()
        else:
            if serial_no in get_device_list():
                self.serial_no = serial_no
            else:
                raise DeviceNotFoundException(msg=f"设备 {serial_no} 未连接")
        self.bundle_id = bundle_id
        logger.info(f"启动 ios driver for {self.serial_no}")
        # 启动wda
        port = get_tcp_port(self.serial_no)
        self.d = wda.Client(f"http://localhost:{port}")
        if not self.d.is_ready():
            logger.info("wda未启动，开始启动wda")
            _start_wda_xctest(self.serial_no, port=port)

    # @classmethod
    # def get_instance(cls, serial_no=None):
    #     if serial_no not in cls._instance:
    #         logger.info(f"{serial_no} Create ios driver singleton")
    #         return IosDriver(serial_no)
    #     return IosDriver._instance[serial_no]

    @staticmethod
    def get_elem(**kwargs):
        return IosElement(**kwargs)

    def install_app(self, ipa_url):
        """安装应用"""
        cmd = f"tidevice -u {self.serial_no} install {ipa_url}"
        logger.info(f"安装应用: {ipa_url}")
        output = subprocess.getoutput(cmd)
        if "Complete" in output.split()[-1]:
            logger.info(f"{self.serial_no} 安装应用{ipa_url} 成功")
            return
        else:
            logger.info(f"{self.serial_no} 安装应用{ipa_url}失败，因为{output}")

    def new_install_app(self, ipa_url, bundle_id=None):
        """先卸载，再安装"""
        pkg_name = bundle_id if bundle_id else self.bundle_id
        self.uninstall_app(pkg_name)
        cmd = f"tidevice -u {self.serial_no} install {ipa_url}"
        logger.info(f"安装应用: {ipa_url}")
        output = subprocess.getoutput(cmd)
        if "Complete" in output.split()[-1]:
            logger.info(f"{self.serial_no} 安装应用{ipa_url} 成功")
            return
        else:
            logger.info(f"{self.serial_no} 安装应用{ipa_url}失败，因为{output}")

    def uninstall_app(self, bundle_id=None):
        """卸载应用"""
        pkg_name = bundle_id if bundle_id else self.bundle_id
        cmd = f"tidevice -u {self.serial_no} uninstall {pkg_name}"
        logger.info(f"卸载应用: {pkg_name}")
        output = subprocess.getoutput(cmd)
        if "Complete" in output.split()[-1]:
            logger.info(f"{self.serial_no} 卸载应用{pkg_name} 成功")
            return
        else:
            logger.info(f"{self.serial_no} 卸载应用{pkg_name}失败，因为{output}")

    def start_app(self, bundle_id=None):
        """启动应用"""
        if not bundle_id:
            bundle_id = self.bundle_id
        logger.info(f"启动应用: {bundle_id}")
        self.d.app_start(bundle_id)

    def force_start_app(self, bundle_id=None):
        """重启应用"""
        if not bundle_id:
            bundle_id = self.bundle_id
        logger.info(f"强制启动应用: {bundle_id}")
        self.d.app_terminate(bundle_id)
        self.start_app(bundle_id)

    def stop_app(self, bundle_id=None):
        """停止应用"""
        if not bundle_id:
            bundle_id = self.bundle_id
        logger.info(f"停止应用: {bundle_id}")
        self.d.app_terminate(bundle_id)

    def app_current(self):
        """获取运行中的app列表"""
        cur_apps = self.d.app_current()
        logger.info(f"获取运行中的app列表: {cur_apps}")
        return cur_apps

    def app_launch(self, bundle_id=None):
        """将应用切到前台"""
        if not bundle_id:
            bundle_id = self.bundle_id
        logger.info(f"将应用切到前台: {bundle_id}")
        self.d.app_launch(bundle_id)

    def back(self):
        """返回上一页"""
        logger.info("返回上一页")
        time.sleep(1)
        self.d.swipe(0, 100, 100, 100)

    def go_home(self):
        """返回手机主页"""
        logger.info("返回手机主页")
        self.d.home()

    def send_keys(self, value):
        """输入内容"""
        logger.info(f"输入: {value}")
        self.d.send_keys(value)

    def screenshot(self, file_name):
        """
        截图并保存到预定路径
        @param file_name: foo.png or fool
        @return:
        """
        # 把文件名处理成test.png的样式
        try:
            if "." in file_name:
                file_name = file_name.split(r".")[0]
            # 截图并保存到当前目录的images文件夹中
            img_dir = os.path.join(os.getcwd(), "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            time_str = time.strftime("%Y年%m月%d日 %H时%M分%S秒")
            file_path = os.path.join(img_dir, f"{time_str}-{file_name}.png")
            self.d.screenshot(file_path)
            # 上传allure报告
            allure.attach.file(
                file_path,
                attachment_type=allure.attachment_type.PNG,
                name=f"{file_name}.png",
            )
            return file_path
        except Exception as e:
            raise ScreenFailException(f"{file_name} 截图失败\n{str(e)}")

    # def screenshot_and_mark(self, file_name, rect):
    #     """给图片指定范围画上红框
    #     rect: [x, y, width, height]
    #     x: 左上坐标x
    #     y：左上角坐标y
    #     width：矩形宽度
    #     height：矩形高度
    #     """
    #     # 把文件名处理成test.png的样式
    #     if '.' in file_name:
    #         file_name = file_name.split(r'.')[0]
    #     # 截图并保存到当前目录的images文件夹中
    #     img_dir = os.path.join(os.getcwd(), 'images')
    #     if os.path.exists(img_dir) is False:
    #         os.mkdir(img_dir)
    #     time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
    #     file_path = os.path.join(img_dir, f'{time_str}-{file_name}.png')
    #     self.d.screenshot(file_path)
    #     # 画框
    #     ImageRecognition.mark(file_path, rect)
    #     # 上传allure报告
    #     allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG, name=f'{file_name}.png')
    #     return file_path

    def get_page_content(self):
        """获取页面xml内容"""
        page_source = self.d.source(accessible=False)
        logger.info(f"获取页面内容: \n{page_source}")
        return page_source

    def get_window_size(self):
        """获取屏幕尺寸"""
        size = self.d.window_size()
        logger.info(f"获取屏幕尺寸: {size}")
        return size

    def click(self, x, y):
        """点击坐标"""
        logger.info(f"点击坐标: ({x}, {y})")
        logger.info(f"{self.serial_no} Tap point ({x}, {y})")
        self.d.appium_settings({"snapshotMaxDepth": 0})
        self.d.tap(x, y)
        self.d.appium_settings({"snapshotMaxDepth": 50})
        time.sleep(1)

    def double_click(self, x, y):
        """双击坐标"""
        logger.info(f"双击坐标: {x},{y}")
        self.d.double_tap(x, y)

    def tap_hold(self, x, y):
        """长按坐标"""
        logger.info(f"长按: {x},{y}")
        self.d.tap_hold(x, y, 1.0)

    def click_alert(self, alert_list: list):
        """点击弹窗"""
        try:
            self.d.alert.click(alert_list)
        except:
            pass

    def swipe(self, start_x, start_y, end_x, end_y, duration=0):
        """根据坐标滑动"""
        logger.info(f"从坐标({start_x}, {start_y})滑动到({end_x}, {end_y})")
        logger.info(
            f"{self.serial_no} swipe from point ({start_x}, {start_y}) to ({end_x}, {end_y})"
        )
        self.d.appium_settings({"snapshotMaxDepth": 2})
        self.d.swipe(int(start_x), int(start_y), int(end_x), int(end_y), duration)
        self.d.appium_settings({"snapshotMaxDepth": 50})
        time.sleep(2)

    def swipe_by_screen_percent(
        self, start_x_percent, start_y_percent, end_x_percent, end_y_percent, duration=0
    ):
        """根据屏幕百分比滑动"""
        logger.info(f"根据屏幕百分比进行滑动")
        w, h = self.d.window_size()
        start_x = w * start_x_percent
        start_y = h * start_y_percent
        end_x = w * end_x_percent
        end_y = h * end_y_percent
        self.swipe(start_x, start_y, end_x, end_y, duration=duration)

    def swipe_left(self, start_percent=1, end_percent=0.5):
        """往左滑动"""
        logger.info("往左边滑动")
        w, h = self.d.window_size()
        self.swipe(start_percent * (w - 1), h / 2, end_percent * w, h / 2)

    def swipe_right(self, start_percent=0.5, end_percent=1):
        """往右滑动"""
        logger.info("往右边滑动")
        w, h = self.d.window_size()
        self.swipe(start_percent * w, h / 2, end_percent * (w - 1), h / 2)

    def swipe_up(self, start_percent=0.8, end_percent=0.2):
        """往上滑动"""
        logger.info("往上边滑动")
        w, h = self.d.window_size()
        self.swipe(w / 2, start_percent * h, w / 2, end_percent * h)

    def swipe_down(self, start_percent=0.2, end_percent=0.8):
        """往下滑动"""
        logger.info("往下面滑动")
        w, h = self.d.window_size()
        self.swipe(w / 2, start_percent * h, w / 2, end_percent * h)

    def check(self):
        """检查设备连接状态"""
        logger.info("健康检查")
        self.d.healthcheck()

    def locked(self):
        """检查手机是否锁屏"""
        logger.info("是否锁屏")
        status = self.d.locked()
        logger.info(status)
        return status

    def lock(self):
        """锁屏"""
        logger.info("锁住屏幕")
        self.d.lock()

    def unlock(self):
        """解锁"""
        logger.info("解锁屏幕")
        self.d.unlock()

    def open_url(self, url):
        """
        打开schema
        @param: url，schema链接，taobao://m.taobao.com/index.htm
        @return:
        """
        logger.info(f"打开url: {url}")
        self.d.open_url(url)

    @property
    def battery_info(self):
        """电池信息"""
        info = self.d.battery_info()
        logger.info(f"电池信息: {info}")
        return info

    @property
    def device_info(self):
        """设备信息"""
        info = self.d.device_info()
        logger.info(f"设备信息: {info}")
        return info

    @property
    def scale(self):
        """获取分辨率"""
        scale = self.d.scale
        logger.info(f"设备分辨率: {scale}")
        return scale
