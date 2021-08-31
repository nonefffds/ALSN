#coding=utf-8
from selenium import webdriver
import time
import re
 
 
opt = webdriver.ChromeOptions()                 #创建浏览器
# opt.set_headless()                            #无窗口模式
driver = webdriver.Chrome(options=opt)          #创建浏览器对象
driver.get('login.html')   #打开网页
# driver.maximize_window()                      #最大化窗口
time.sleep(2)                                   #加载等待
 
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/input").send_keys("username")    #利用xpath查找元素进行输入文本
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/input").send_keys("password")


driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button[2]").click()#点击按钮

# driver.find_element_by_xpath("//input[@value='百度一下']").click()#候选方法
# driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input[type='submit'][value='百度一下']").click()#候选方法,多条件匹配
#Reference:https://blog.csdn.net/www89574622/article/details/87974931