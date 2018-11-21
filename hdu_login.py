# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import argparse
parser = argparse.ArgumentParser(description="hdu_login")
parser.add_argument("--name", help="hdu用户名", type=str)
parser.add_argument("--pwd", help="hdu密码", type=str)
args = parser.parse_args()
with webdriver.PhantomJS() as driver:
    driver.get("http://2.2.2.2/ac_portal/default/pc.html?tabs=pwd")
    time.sleep(1)
    driver.find_element_by_css_selector("#password_name").send_keys(args.name)
    time.sleep(1)
    driver.find_element_by_css_selector("#password_pwd").send_keys(args.pwd)
    time.sleep(1)
    driver.find_element_by_css_selector("#password_submitBtn").click()
    time.sleep(2)
    print(driver.find_element_by_css_selector("#mode_logout > div > div.login_head").text)
    print("登陆成功！！！")
