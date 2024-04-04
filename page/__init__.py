from selenium.webdriver.common.by import By
"""tpshop临时服务器url"""
url = "http://localhost"
"""以下为登录模块配置数据"""
# 登录连接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 异常提示信息
login_error_info = By.CSS_SELECTOR, ".layui-layer-content"
# 异常提示框 确定
login_error_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
# 获取昵称
login_nickname = By.CSS_SELECTOR, ".userinfo"
# 安全退出
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"

"""以下为购物车配置数据"""
# 回到首页
cart_index = By.CSS_SELECTOR, ".logo>img"
# 输入商品
cart_input_goods = By.CSS_SELECTOR, "#q"
# 点击搜索按钮
cart_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# 添加购物车 --》跳转详情
cart_add_cart_info = By.CSS_SELECTOR, ".p-btn>a"
# 添加购物车
cart_add_cart = By.CSS_SELECTOR, "#join_cart"
# 获取添加提示信息
cart_add_result = By.CSS_SELECTOR, ".conect-title>span"
# 关闭提示窗口
cart_close_window = By.CSS_SELECTOR, ".layui-layer-close"
# frame 窗口id 此处是个变量
cart_iframe_id = "layui-layer-iframe1"
# frame 窗口name 此处是元素
cart_iframe_element = By.CSS_SELECTOR, "#layui-layer-iframe1"
#  点击首页按钮
cart_shouye = By.XPATH, "//div//li/a[text()='首页']"
# 未输入搜索词搜索后信息提示
not_input_search_goods_message = By.XPATH, "//div/span[contains(text(),'请输入搜索词')]"
# 输入商品搜索不到给的文本提示
input_not_search_goods_message = By.CSS_SELECTOR, ".ncyekjl"


