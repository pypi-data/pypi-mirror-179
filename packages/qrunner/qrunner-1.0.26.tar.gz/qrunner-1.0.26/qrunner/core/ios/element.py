import inspect
from typing import Union

from wda import Selector

from qrunner.utils.exceptions import ElementNameEmptyException, NoSuchElementException
from qrunner.utils.log import logger
from qrunner.utils.config import config
from qrunner.core.ios.driver import IosDriver


class IosElement(object):
    """
    IOS原生元素定义
    """

    def __init__(self, *args, **kwargs):
        """
        param name,
        param label,
        param value,
        param text,
        param className,
        param xpath,
        param index: 索引,
        param desc: 控件名称
        """
        # 参数处理
        self._xpath = kwargs.get('xpath', None)
        self._index = kwargs.get('index', 0)
        self.desc = kwargs.pop('desc', None)
        if self.desc is None:
            raise ElementNameEmptyException("请设置控件名称")
        if len(args) > 0:
            self._driver = args[0]
        else:
            self._driver = kwargs.pop('driver', None)
        self._kwargs = kwargs

        # # 驱动初始化
        # _serial_no = config.get_item('ios', 'serial_no')
        # self._driver = IosDriver.get_instance(_serial_no)
        # self._d = self._driver.d

    def get_driver(self):
        if self._driver is None:
            serial_no = config.get_device()
            self._driver = IosDriver.get_instance(serial_no)
        return self._driver

    # def _find_element(self, retry=3, timeout=3):
    #     """
    #     循环查找元素，查找失败先处理弹窗后重试
    #     @param retry: 重试次数
    #     @param timeout: 单次查找超时时间
    #     @return:
    #     """
    #     self._element = self._d.xpath(self._xpath) if \
    #         self._xpath else self._d(**self._kwargs)[self._index]
    #     self.handle_alert()
    #     while not self._element.wait(timeout=timeout):
    #         if retry > 0:
    #             retry -= 1
    #             logger.warning(f'重试 查找元素： {self._kwargs}')
    #             self.handle_alert()
    #         else:
    #             frame = inspect.currentframe().f_back
    #             caller = inspect.getframeinfo(frame)
    #             logger.warning(f'【{caller.function}:{caller.lineno}】未找到元素 {self._kwargs}')
    #             return None
    #     return self._element

    def _find_element(self, retry=3, timeout=3, alert_list=None):
        """
        循环查找元素，查找失败先处理弹窗后重试
        @param retry: 重试次数
        @param timeout: 单次查找超时时间
        @return:
        """

        # 多线程处理异常弹窗
        def handle_alert(driver, alert_list):
            """
            根据不同定位方式进行点击
            @return:
            """

            def click_alert(loc):
                if "//" in loc:
                    element = driver.d.xpath(loc)
                else:
                    element = driver.d(label=loc)
                element.click_exists()

            # 多线程存在问题，目前没有使用多线程
            if alert_list:
                print(f"处理弹窗: {alert_list}")
                for alert in alert_list:
                    click_alert(alert)

        # 驱动初始化
        driver = self.get_driver()

        element = (
            driver.d.xpath(self._xpath)
            if self._xpath
            else driver.d(**self._kwargs)[self._index]
        )
        handle_alert(driver, alert_list)
        cur_retry = retry
        while not element.wait(timeout=timeout):
            if cur_retry > 0:
                logger.warning(
                    f"第{retry-cur_retry+1}次重试，查找元素： {self._kwargs},{self._index}"
                )
                cur_retry -= 1
                handle_alert(driver, alert_list)
            else:
                frame = inspect.currentframe().f_back
                caller = inspect.getframeinfo(frame)
                logger.warning(
                    f"【{caller.function}:{caller.lineno}】未找到元素 {self._kwargs}"
                )
                return None
        elements = (
            driver.d.xpath(self._xpath).find_elements()
            if self._xpath
            else driver.d(**self._kwargs)
        )
        return elements

    def get_elements(self, retry=3, timeout=3, alert_list=None):
        """
        针对元素定位失败的情况，抛出NoSuchElementException异常
        @param retry:
        @param timeout:
        @param alert_list
        @return:
        """
        driver = self.get_driver()

        elements: Union[Selector] = self._find_element(
            retry=retry, timeout=timeout, alert_list=alert_list
        )
        if elements is None:
            driver.screenshot(f"[控件 {self.desc}] 定位失败")
            raise NoSuchElementException(f"[控件 {self.desc}] 定位失败")
        else:
            driver.screenshot(self.desc)
        return elements

    # def __getitem__(self, index):
    #     elements = self.get_elements()
    #     return elements[index]

    def get_element(self, retry=3, timeout=3, alert_list=None):
        """
        针对元素定位失败的情况，抛出NoSuchElementException异常
        @param retry:
        @param timeout:
        @param alert_list
        @return:
        """
        elements = self.get_elements(
            retry=retry, timeout=timeout, alert_list=alert_list
        )
        return elements[self._index]

    @property
    def info(self):
        """获取元素信息"""
        logger.info(f"获取元素: {self._kwargs} 的所有属性")
        return self.get_element().info

    @property
    def text(self):
        """获取元素文本"""
        logger.info(f"获取元素: {self._kwargs} 的text属性")
        return self.get_element().text

    @property
    def className(self):
        """获取元素className"""
        logger.info(f"获取元素: {self._kwargs} 的className属性")
        return self.get_element().className

    @property
    def name(self):
        """获取元素name"""
        logger.info(f"获取元素: {self._kwargs} 的name属性")
        return self.get_element().name

    @property
    def visible(self):
        """获取元素visible属性"""
        logger.info(f"获取元素: {self._kwargs} 的visible属性")
        return self.get_element().visible

    @property
    def value(self):
        """获取元素value"""
        logger.info(f"获取元素: {self._kwargs} 的value属性")
        return self.get_element().value

    @property
    def label(self):
        """获取元素label"""
        logger.info(f"获取元素: {self._kwargs} 的label属性")
        return self.get_element().label

    @property
    def enabled(self):
        """获取元素enabled属性"""
        logger.info(f"获取元素: {self._kwargs} 的enabled属性")
        return self.get_element().enabled

    @property
    def displayed(self):
        """获取元素displayed属性"""
        logger.info(f"获取元素: {self._kwargs} 的displayed属性")
        return self.get_element().displayed

    @property
    def bounds(self):
        """获取元素bounds属性"""
        logger.info(f"获取元素: {self._kwargs} 的bounds属性")
        return self.get_element().bounds

    @property
    def rect(self):
        """获取元素左上角坐标和宽高"""
        logger.info(f"获取元素: {self._kwargs} 的左上角坐标和宽高")
        return [
            item * self.get_driver().d.scale for item in list(self.get_element().bounds)
        ]

    def exists(self, timeout=1):
        """
        判断元素是否存在当前页面
        @param timeout:
        @return:
        """
        logger.info(f"元素 {self._kwargs},{self._index} 是否存在:")
        element = self._find_element(retry=0, timeout=timeout)
        if element is None:
            # self._driver.screenshot(f'元素定位失败')
            return False
        return True

    def wait_gone(self, timeout=10):
        """等待元素消失"""
        logger.info(f"等待元素{self._kwargs}消失")
        flag = self.get_element().wait_gone(timeout=timeout)
        logger.info(flag)
        return flag

    def click(self, retry=3, timeout=3, alert_list=None):
        """
        单击
        @param: retry，重试次数
        @param: timeout，每次重试超时时间
        @param: alert_list，异常弹窗列表
        """
        logger.info(f"点击元素: {self._kwargs},{self._index}")
        self.get_element(retry=retry, timeout=timeout, alert_list=alert_list).click()

    # def click_no_retry(self):
    #     logger.info(f'点击元素: {self._kwargs},{self._index}')
    #     self.get_element(retry=0, timeout=1).click()

    def click_exists(self, timeout=3):
        """元素存在时点击"""
        logger.info(f"存在才点击元素: {self._kwargs},{self._index}")
        if self.exists(timeout=timeout):
            self.click()

    def clear_text(self):
        """清除文本"""
        logger.info("清除文本: {text}")
        self.get_element().clear_text()

    def set_text(self, text):
        """输入内容"""
        logger.info(f"输入框 {self._kwargs},{self._index} 输入: {text}")
        self.get_element().set_text(text)

    def scroll(self, direction=None):
        """
        scroll to make element visiable
        @param: direction，方向，"up", "down", "left", "right"
        @return:
        """
        if direction is not None:
            self.get_element().scroll(direction=direction)
        else:
            self.get_element().scroll()

    def swipe_left(self):
        """往左滑动"""
        self.get_element().swipe("left")

    def swipe_right(self):
        """往右滑动"""
        self.get_element().swipe("right")

    def swipe_up(self):
        """往上滑动"""
        self.get_element().swipe("up")

    def swipe_down(self):
        """往下滑动"""
        self.get_element().swipe("down")

    def child(self, *args, **kwargs):
        """获取兄弟节点，不能用于PageObject，会导致在应用启动前进行元素识别"""
        return self.get_element().child(*args, **kwargs)
