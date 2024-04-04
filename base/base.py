import time

from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入元素
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本值
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 判断元素是否存在
    def base_if_isnot_exsit(self, loc):
        try:
            self.base_find_element(loc)
            return True
        except:
            return False

    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 切换iframe
    def base_switch_to_iframe(self, frame):
        self.driver.switch_to.frame(frame)

    # 恢复默认目录方法
    def base_switch_to_default_context(self):
        self.driver.switch_to.default_content()

    # 打开首页方法
    def base_click_index(self):
        self.driver.get("http://localhost")