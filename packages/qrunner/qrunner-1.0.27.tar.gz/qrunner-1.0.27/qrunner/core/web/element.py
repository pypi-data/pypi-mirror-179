import inspect
import platform

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from qrunner.utils.exceptions import ElementNameEmptyException, NoSuchElementException
from qrunner.utils.log import logger
from qrunner.utils.config import config
from qrunner.core.web.driver import WebDriver

# 支持的定位方式
LOC_LIST = {
    "id": By.ID,
    "name": By.NAME,
    "link_text": By.LINK_TEXT,
    "tag_name": By.TAG_NAME,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
    "class_name": By.CLASS_NAME,
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
}


class WebElement:
    """
    根据定位方式定位元素并进行操作
    """

    def __init__(self, *args, **kwargs):
        """
        param id: 标签的id
        param name: 标签的name属性,
        param ltext: a标签的文本，精准匹配,
        param pltext: a标签的文本，模糊匹配,
        param tname: 标签名,
        param cname: 标签的class属性,
        param xpath,
        param css,
        param index: 索引,
        param desc: 控件名称
        """
        # 参数处理
        self._index = kwargs.get('index', 0)
        self.desc = kwargs.pop('desc', None)
        if self.desc is None:
            raise ElementNameEmptyException("请设置控件名称")

        if len(args) > 0:
            self._driver = args[0]
        else:
            self._driver = kwargs.pop('driver', None)
        self.k, self.v = next(iter(kwargs.items()))
        self._kwargs = kwargs

        # 驱动初始化
        # browser_name = config.get_item('web', 'browser_name')
        # self.driver = WebDriver.get_instance(browser_name)
        # self.d = self.driver.d

    def get_driver(self):
        if self._driver is None:
            browser_name = config.get_browser()
            self._driver = WebDriver.get_instance(browser_name)
        return self._driver

    def _wait(self, timeout=3):
        try:
            WebDriverWait(self.get_driver().d, timeout=timeout).until(
                EC.visibility_of_element_located((LOC_LIST[self.k], self.v))
            )
            return True
        except Exception:
            return False

    def _find_element(self, retry=3, timeout=5):
        cur_retry = retry
        while not self._wait(timeout=timeout):
            if cur_retry > 0:
                logger.warning(f"第{retry-cur_retry+1}次重试，查找元素： {self._kwargs}")
                cur_retry -= 1
            else:
                frame = inspect.currentframe().f_back
                caller = inspect.getframeinfo(frame)
                logger.warning(
                    f"【{caller.function}:{caller.lineno}】Not found element {self._kwargs}"
                )
                return None
        elements = self.get_driver().d.find_elements(LOC_LIST[self.k], self.v)
        return elements

    def get_elements(self, retry=3, timeout=3):
        elements = self._find_element(retry=retry, timeout=timeout)
        if elements is None:
            self.get_driver().screenshot(f"[控件 {self.desc} 定位失败]")
            raise NoSuchElementException(f"[控件 {self.desc} 定位失败]")
        else:
            # if self._index is None:
            #     for element in elements:
            #         self.get_driver().mark(element)
            # else:
            #     self.get_driver().mark(elements[self._index])
            self.get_driver().screenshot(self.desc)
        return elements

    # def __getitem__(self, index):
    #     elements = self.get_elements()
    #     return elements[index]

    def get_element(self, retry=3, timeout=3):
        # elements = self._find_element(retry=retry, timeout=timeout)
        # if elements is None:
        #     self.driver.screenshot(f'[控件 {self.desc} 定位失败]')
        #     raise NoSuchElementException(f'[控件 {self.desc} 定位失败]')
        # else:
        #     element = elements[self._index]
        #     self.driver.execute_js("arguments[0].style.border='3px solid red'", element)
        #     self.driver.screenshot(self.desc)
        # return element
        elements = self.get_elements(retry=retry, timeout=timeout)
        return elements[self._index]

    def exists(self, timeout=1):
        logger.info(f"判断元素: {self._kwargs} 是否存在")
        element = self._find_element(retry=0, timeout=timeout)
        if element is None:
            # self.driver.screenshot(f'元素定位失败')
            return False
        return True

    def click(self, retry=3, timeout=5):
        logger.info(f"点击元素: {self._kwargs}")
        self.get_element(retry=retry, timeout=timeout).click()

    def click_exists(self, timeout=1):
        logger.info(f"存在才点击元素: {self._kwargs},{self._index}")
        if self.exists(timeout=timeout):
            self.click()

    def slow_click(self):
        logger.info(f"移动到元素{self._kwargs}，然后点击")
        elem = self.get_element()
        ActionChains(self.get_driver().d).move_to_element(elem).click(elem).perform()

    def right_click(self):
        logger.info(f"右键元素{self._kwargs}")
        elem = self.get_element()
        ActionChains(self.get_driver().d).context_click(elem).perform()

    def move_to_elem(self):
        logger.info(f"鼠标移动到元素{self._kwargs}上")
        elem = self.get_element()
        ActionChains(self.get_driver().d).move_to_element(elem).perform()

    def click_and_hold(self):
        logger.info(f"长按元素: {self._kwargs}")
        elem = self.get_element()
        ActionChains(self.get_driver().d).click_and_hold(elem).perform()

    def drag_and_drop(self, x, y):
        logger.info(f"拖动元素{self._kwargs}到坐标{x},{y}")
        elem = self.get_element()
        action = ActionChains(self.get_driver().d)
        action.drag_and_drop_by_offset(elem, x, y).perform()

    def double_click(self):
        logger.info(f"双击元素: {self._kwargs}")
        elem = self.get_element()
        ActionChains(self.get_driver().d).double_click(elem).perform()

    def set_text(self, text):
        logger.info(f"点击元素: {self._kwargs}，然后输入: {text}")
        self.get_element().send_keys(text)

    def set_and_enter(self, text):
        logger.info(f"往 {self._kwargs} 输入 {text} 并回车")
        element = self.get_element()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def clear_text(self):
        logger.info(f"清空文本")
        self.get_element().clear()

    def enter(self):
        logger.info(f"选中元素{self._kwargs}点击enter")
        self.get_element().send_keys(Keys.ENTER)

    def select_all(self) -> None:
        logger.info(f"选中元素{self._kwargs}, ctrl+a.")
        if platform.system().lower() == "darwin":
            self.get_element().send_keys(Keys.COMMAND, "a")
        else:
            self.get_element().send_keys(Keys.CONTROL, "a")

    def cut(self) -> None:
        logger.info(f"选中元素{self._kwargs}, ctrl+x.")
        if platform.system().lower() == "darwin":
            self.get_element().send_keys(Keys.COMMAND, "x")
        else:
            self.get_element().send_keys(Keys.CONTROL, "x")

    def copy(self) -> None:
        logger.info(f"选中元素{self._kwargs}, ctrl+c.")
        if platform.system().lower() == "darwin":
            self.get_element().send_keys(Keys.COMMAND, "c")
        else:
            self.get_element().send_keys(Keys.CONTROL, "c")

    def paste(self) -> None:
        logger.info(f"选中元素{self._kwargs}, ctrl+v.")
        if platform.system().lower() == "darwin":
            self.get_element().send_keys(Keys.COMMAND, "v")
        else:
            self.get_element().send_keys(Keys.CONTROL, "v")

    def backspace(self) -> None:
        logger.info(f"选中元素{self._kwargs}, backspace.")
        self.get_element().send_keys(Keys.BACKSPACE)

    def delete(self) -> None:
        logger.info(f"选中元素{self._kwargs}, delete.")
        self.get_element().send_keys(Keys.DELETE)

    def tab(self) -> None:
        logger.info(f"选中元素{self._kwargs}, tab.")
        self.get_element().send_keys(Keys.TAB)

    def space(self) -> None:
        logger.info(f"选中元素{self._kwargs}, space.")
        self.get_element().send_keys(Keys.SPACE)

    @property
    def rect(self):
        """获取的坐标位置不对，截图会偏"""
        logger.info(f"获取元素 {self._kwargs}的坐标")
        bounds = self.get_element().rect
        logger.debug(f"rect: {bounds}")
        x = bounds["x"] * 2
        y = bounds["y"] * 2
        width = bounds["width"] * 2
        height = bounds["height"] * 2
        return [x, y, width, height]
        # return None

    def get_attr(self, attr_name):
        logger.info(f"获取属性{attr_name}的值")
        value = self.get_element().get_attribute(attr_name)
        logger.info(value)
        return value

    def get_display(self):
        logger.info(f"获取元素{self._kwargs}的display属性")
        displayed = self.get_element().is_displayed()
        logger.info(displayed)
        return displayed

    @property
    def text(self):
        logger.info(f"获取元素 {self._kwargs} 文本")
        element = self.get_element()
        text = element.text
        logger.info(text)
        return text

    def select_index(self, index):
        logger.info(f"选择第 {index} 个下拉列表")
        element = self.get_element()
        select = Select(element)
        select.select_by_index(index)

    def select_value(self, value):
        logger.info(f"选择id为 {value} 的下拉列表")
        element = self.get_element()
        select = Select(element)
        select.select_by_value(value)

    def select_text(self, text):
        logger.info(f"选择下拉列表 {text} 选项")
        element = self.get_element()
        select = Select(element)
        select.select_by_value(text)

    def submit(self):
        logger.info(f"提交表单: {self._kwargs}")
        elem = self.get_element()
        elem.submit()

    # def screenshot(self, file_name):
    #     """
    #     截图并保存到预定路径并上传到allure报告
    #     @param file_name: foo.png or fool
    #     @return:
    #     """
    #     # 把文件名处理成test.png的样式
    #     if '.' in file_name:
    #         file_name = file_name.split(r'.')[0]
    #     # 截图并保存到当前目录的images文件夹中
    #     img_dir = os.path.join(os.getcwd(), 'images')
    #     if os.path.exists(img_dir) is False:
    #         os.mkdir(img_dir)
    #     time_str = time.strftime('%Y%m%d%H%M%S')
    #     file_path = os.path.join(img_dir,
    #                              f'{file_name}-{time_str}.png')
    #     logger.info(f'截图保存至: {file_path}')
    #     self.get_element().screenshot(file_path)
    #     # 截图并上传到allure报告
    #     logger.info(f'截图上传至allure报告')
    #     allure.attach.file(file_path,
    #                        attachment_type=allure.attachment_type.PNG,
    #                        name=f'{file_name}-{time_str}')
