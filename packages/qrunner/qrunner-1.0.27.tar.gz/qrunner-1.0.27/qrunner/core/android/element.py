import inspect
import typing

from uiautomator2 import UiObject
from uiautomator2.xpath import XPathSelector

from qrunner.core.android.driver import AndroidDriver
from qrunner.utils.config import config
from qrunner.utils.exceptions import ElementNameEmptyException, NoSuchElementException
from qrunner.utils.log import logger


class AndroidElement(object):
    """
    安卓元素定义
    """

    def __init__(self, *args, **kwargs):
        """
        param resourceId,
        param className,
        param text,
        param xpath,
        param desc：控件名称,
        param index: 控件索引
        """
        # 参数处理
        self._pkg_name = config.get_pkg()
        id_ = kwargs.get('resourceId', None)
        if id_ is not None:
            kwargs["resourceId"] = f"{self._pkg_name}:{id_}"
        self._xpath = kwargs.get('xpath', None)
        self.desc = kwargs.pop('desc', None)
        if self.desc is None:
            raise ElementNameEmptyException("请设置控件名称")
        self._index = kwargs.get('index', 0)
        if len(args) > 0:
            self._driver = args[0]
        else:
            self._driver = kwargs.pop('driver', None)
        self._kwargs = kwargs

        # # 驱动初始化
        # _serial_no = config.get_item('android', 'serial_no')
        # self._driver = AndroidDriver.get_instance(_serial_no)
        # self._d = self._driver.d

    # def find_element(self, retry=3, timeout=3):
    #     """class_name
    #     循环查找元素，查找失败先处理弹窗后重试，后面再考虑xpath要不要用.all()改造一下
    #     @param retry: 重试次数
    #     @param timeout: 每次查找超时时间
    #     @param alert_check: 是否监控弹窗
    #     @return: 找到的元素列表
    #     """
    #     logger.info(f'查找元素: {self._kwargs},{self._index}')
    #     _element = self._d.xpath(self._xpath) if \
    #         self._xpath else self._d(**self._kwargs)[self._index]
    #     while not _element.wait(timeout=timeout):
    #         if retry > 0:
    #             retry -= 1
    #             logger.warning(f'重试 查找元素： {self._kwargs},{self._index}')
    #         else:
    #             frame = inspect.currentframe().f_back
    #             caller = inspect.getframeinfo(frame)
    #             logger.warning(f'【{caller.function}:{caller.lineno}】未找到元素 {self._kwargs}')
    #             return None
    #     return _element

    def get_driver(self):
        if self._driver is None:
            serial_no = config.get_device()
            self._driver = AndroidDriver.get_instance(serial_no)
        return self._driver

    def find_element(self, retry=3, timeout=3, alert_list=None):
        """
        循环查找元素，查找失败先处理弹窗后重试，后面再考虑xpath要不要用.all()改造一下
        @param retry: 重试次数
        @param timeout: 每次查找超时时间
        @param alert_list
        @return: 找到的元素列表
        """

        def handle_alert(driver, alert_list):
            """
            根据不同定位方式进行点击
            @return:
            """

            def click_alert(loc):
                if "id/" in loc:
                    element = driver(resourceId=f"{self._pkg_name}:{loc}")
                elif "//" in loc:
                    element = driver.xpath(loc)
                else:
                    element = driver(text=loc)
                element.click_exists(timeout=1)

            # 多线程执行点击过程
            # alert_list = config.get_item('app', 'android_alert')
            # pool = ThreadPool(len(alert_list))
            # if alert_list:
            #     pool.map(click_alert, alert_list)
            if alert_list:
                print(f"处理弹窗: {alert_list}")
                for alert in alert_list:
                    click_alert(alert)
                logger.debug("处理异常弹窗完成")

        driver = self.get_driver()

        logger.info(f"查找元素: {self._kwargs},{self._index}")
        _element = (
            driver.d.xpath(self._xpath)
            if self._xpath
            else driver.d(**self._kwargs)[self._index]
        )
        handle_alert(driver.d, alert_list)  # 处理异常弹窗
        cur_retry = retry
        while not _element.wait(timeout=timeout):
            if cur_retry > 0:
                logger.warning(f"第{retry-cur_retry+1}次重试，查找元素： {self._kwargs}")
                cur_retry -= 1
                handle_alert(driver.d, alert_list)  # 处理异常弹窗
            else:
                frame = inspect.currentframe().f_back
                caller = inspect.getframeinfo(frame)
                logger.warning(
                    f"【{caller.function}:{caller.lineno}】未找到元素 {self._kwargs}"
                )
                return None
        _elements = (
            driver.d.xpath(self._xpath).all()
            if self._xpath
            else driver.d(**self._kwargs)
        )
        return _elements

    # def find_elements(self, retry=3, timeout=3, alert_list=None):
    #     """
    #     循环查找元素，查找失败先处理弹窗后重试，后面再考虑xpath要不要用.all()改造一下
    #     @param retry: 重试次数
    #     @param timeout: 每次查找超时时间
    #     @param alert_list
    #     @return: 找到的元素列表
    #     """
    #     logger.info(f'查找元素列表: {self._kwargs}')
    #     if not self._xpath:
    #         _elements = self._d(**self._kwargs)
    #     else:
    #         raise AssertionError('find_elements方法不支持xpath定位')
    #     self.handle_alert(alert_list)  # 处理异常弹窗
    #     cur_retry = retry
    #     while not _elements.wait(timeout=timeout):
    #         if cur_retry > 0:
    #             logger.warning(f'第{retry-cur_retry+1}次重试，查找元素： {self._kwargs}')
    #             cur_retry -= 1
    #             self.handle_alert(alert_list)  # 处理异常弹窗
    #         else:
    #             frame = inspect.currentframe().f_back
    #             caller = inspect.getframeinfo(frame)
    #             logger.warning(f'【{caller.function}:{caller.lineno}】未找到元素 {self._kwargs}')
    #             return None
    #     return _elements

    def get_elements(self, retry=3, timeout=3, alert_list=None):
        """
        获取元素列表
        @param retry:
        @param timeout:
        @param alert_list
        @return:
        """
        driver = self.get_driver()
        elements = self.find_element(
            retry=retry, timeout=timeout, alert_list=alert_list
        )
        if elements is None:
            driver.screenshot(f"[控件 {self.desc} 定位失败]")
            raise NoSuchElementException(f"[控件 {self.desc} 定位失败]")
        else:
            driver.screenshot(self.desc)
        return elements

    # def __getitem__(self, index):
    #     elements = self.get_elements()
    #     return elements[index]

    def get_element(self, retry=3, timeout=3, alert_list=None):
        """
        获取指定一个元素
        @param retry:
        @param timeout:
        @param alert_list
        @return:
        """
        # element = self.find_element(retry=retry, timeout=timeout, alert_list=alert_list)
        # if element is None:
        #     self._driver.screenshot(f'[控件 {self.desc} 定位失败]')
        #     raise NoSuchElementException(f'[控件 {self.desc} 定位失败]')
        elements = self.get_elements(
            retry=retry, timeout=timeout, alert_list=alert_list
        )
        return elements[self._index]

    @property
    def info(self):
        """获取元素信息"""
        logger.info(f"获取元素: {self._kwargs} 的所有信息")
        return self.get_element().info

    @property
    def text(self):
        """获取元素文本属性"""
        logger.info(f"获取元素: {self._kwargs} 的文本")
        return self.get_element().info.get("text")

    @property
    def bounds(self):
        """获取元素坐标"""
        logger.info(f"获取元素: {self._kwargs} 的坐标")
        return self.get_element().info.get("bounds")

    @property
    def rect(self):
        """获取元素左上角的坐标以及宽高"""
        logger.info(f"获取元素: {self._kwargs} 左上角的坐标以及宽高")
        bounds = self.get_element().info.get("bounds")
        x = bounds["left"]
        y = bounds["top"]
        width = bounds["right"] - x
        height = bounds["bottom"] - y
        return [x, y, width, height]

    @property
    def visibleBounds(self):
        """获取元素可见坐标"""
        logger.info(f"获取元素: {self._kwargs} 的可见坐标")
        return self.get_element().info.get("visibleBounds")

    @property
    def focusable(self):
        """获取元素是否聚焦"""
        logger.info(f"获取元素: {self._kwargs} 是否聚焦")
        return self.get_element().info.get("focusable")

    @property
    def selected(self):
        """获取元素是否选中"""
        logger.info(f"获取元素: {self._kwargs} 是否选中")
        return self.get_element().info.get("selected")

    def child(self, *args, **kwargs):
        """获取元素儿子节点，不能用于PageObject，会导致在应用启动前进行元素识别"""
        logger.info(f"获取元素 {self._kwargs},{self._index} 的子元素{kwargs}")
        return self.get_element().child(*args, **kwargs)

    def brother(self, *args, **kwargs):
        """获取兄弟元素"""
        logger.info(f"获取元素 {self._kwargs},{self._index} 的兄弟元素{kwargs}")
        return self.get_element().sibling(*args, **kwargs)

    def left(self, *args, **kwargs):
        """获取左边元素"""
        logger.info(f"获取元素 {self._kwargs} 左边的元素 {kwargs}")
        return self.get_element().left(*args, **kwargs)

    def right(self, *args, **kwargs):
        """获取右边元素"""
        logger.info(f"获取元素 {self._kwargs} 右边的元素 {kwargs}")
        return self.get_element().right(*args, **kwargs)

    def up(self, *args, **kwargs):
        """获取上边的元素"""
        logger.info(f"获取元素 {self._kwargs} 上边的元素 {kwargs}")
        return self.get_element().up(*args, **kwargs)

    def down(self, *args, **kwargs):
        """获取下边的元素"""
        logger.info(f"获取元素 {self._kwargs} 下边的元素 {kwargs}")
        return self.get_element().down(*args, **kwargs)

    def exists(self, timeout=1):
        """判断元素是否存在"""
        logger.info(f"判断元素是否存在: {self._kwargs},{self._index}")
        element = self.find_element(retry=0, timeout=timeout)
        if element is None:
            # self._driver.screenshot(f'元素定位失败')
            return False
        return True

    @staticmethod
    def _adapt_center(e: typing.Union[UiObject, XPathSelector], offset=(0.5, 0.5)):
        if isinstance(e, UiObject):
            return e.center(offset=offset)
        else:
            return e.offset(offset[0], offset[1])

    def click(self, retry=3, timeout=3, alert_list=None):
        """
        @param: retry，重试次数
        @param: timeout，每次重试超时时间
        @param: alert_list，异常弹窗列表
        """
        logger.info(f"点击元素: {self._kwargs},{self._index}")
        element = self.get_element(retry=retry, timeout=timeout, alert_list=alert_list)
        # 这种方式经常点击不成功，感觉是页面刷新有影响
        # element.click()
        x, y = self._adapt_center(element)
        self.get_driver().d.click(x, y)
        logger.debug("点击成功")

    # def click_no_retry(self, offset=(0.5, 0.5), timeout=1):
    #     logger.info(f'点击元素: {self._kwargs},{self._index}')
    #     element = self.get_element(timeout=timeout)
    #     x, y = self._adapt_center(element, offset=offset)
    #     self._d.click(x, y)
    #     logger.debug('点击成功')

    def click_exists(self, timeout=3):
        """元素存在才点击"""
        logger.info(f"存在才点击元素: {self._kwargs},{self._index}")
        if self.exists(timeout=timeout):
            self.click()

    def click_gone(self):
        """等元素消失后再点击"""
        logger.info(f"等元素 {self._kwargs} 消失后再点击")
        flag = self.get_element().click_gone()
        logger.info(flag)
        return flag

    def wait_gone(self, timeout=3):
        """等待元素消失"""
        logger.info(f"等元素 {self._kwargs} 消失")
        flag = self.get_element().wait_gone(timeout=timeout)
        logger.info(flag)
        return flag

    def long_click(self):
        """长按"""
        logger.info(f"长按元素 {self._kwargs}")
        self.get_element().long_click()

    def set_text(self, text):
        """输入文本"""
        logger.info(f"输入文本: {text}")
        self.get_element().set_text(text)

    def clear_text(self):
        """清除文本"""
        logger.info("清除文本")
        self.get_element().clear_text()

    def drag_to(self, *args, **kwargs):
        """拖动到另外一个元素的位置"""
        logger.info(f"从当前元素{self._kwargs},{self._index}, 拖动到元素: {kwargs}")
        self.get_element().drag_to(*args, **kwargs)

    def swipe_left(self):
        """向左滑动"""
        logger.info(f"往左滑动元素: {self._kwargs},{self._index}")
        self.get_element().swipe("left")

    def swipe_right(self):
        """向右滑动"""
        logger.info(f"往右滑动元素: {self._kwargs},{self._index}")
        self.get_element().swipe("right")

    def swipe_up(self):
        """向上滑动"""
        logger.info(f"往上滑动元素: {self._kwargs},{self._index}")
        self.get_element().swipe("up")

    def swipe_down(self):
        """向下滑动"""
        logger.info(f"往下滑动元素: {self._kwargs},{self._index}")
        self.get_element().swipe("down")
