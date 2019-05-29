from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.yigongla.com/")
driver.find_element_by_xpath("//a[@href='/index/index/index']").click()
driver.find_element_by_xpath("//a[@href='/index/qyserve/qyserve']").click()

driver.assert_exist("/html/body/div[3]/div/h3", "xpath", "我的价值")

driver.find_element_by_xpath("//a[@href='/index/inquiry/inquiry']").click()
driver.find_element_by_xpath("//a[@href='/index/about/about']").click()
driver.find_element_by_xpath("/html/body/div/div[2]/a/button").click()
driver.assert_exist("/html/body/div/div/div/div/div/div", "xpath", "密码登录")
driver.assert_exist("/html/body/div/div/div/div/div/div[2]", "xpath", "验证码登录")
driver.assert_exist("/html/body/div/div/div/div[3]/p", "xpath", "还没有易工账号")
driver.assert_exist("/html/body/div/div/div/div[3]/div/a/span", "xpath", "立即注册")
driver.assert_exist("passwordLogin", "id", "登录")
driver.assert_exist("/html/body/div[2]/p", "xpath", "从蓝领招聘开始解决缺工现象.")

driver.quit()