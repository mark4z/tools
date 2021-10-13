import json
import logging
import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import wait


def send(driver, cmd, params=None):
    if params is None:
        params = {}
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    if response['status']:
        raise Exception(response.get('value'))
    return response.get('value')


def process(url_str, options):
    with webdriver.Remote(
            options=options,
            command_executor='http://127.0.0.1:4444/wd/hub'
    ) as driver:
        # with webdriver.Chrome(
        #         options=options
        # ) as driver:
        print(send(driver, 'Emulation.setNavigatorOverrides', {"platform": "iPhone"}))
        # driver.execute_cdp_cmd('Emulation.setNavigatorOverrides', {"platform": "iPhone"})

        driver.set_window_size(376, 812)
        driver.get(url_str)

        print('scroll')
        for i in range(0, 3):
            TouchActions(driver).scroll(150, 200).perform()
        print('scroll end')

        images = driver.find_elements(by=By.TAG_NAME, value="img")
        print(images)

        for i in range(0, len(images)):
            try:
                ActionChains(driver).click()
                print('pass')
                break
            except AttributeError as err:
                print(err)
                pass
        driver.save_screenshot("./10.png")


if __name__ == '__main__':
    # url = "http://47.100.220.7/"
    url = "https://bhjtomghwqdvm.kuaizhan.com/?sif=1e927p7ajg9ijg168q2ib2i969"
    # url = "https://www.baidu.com"

    option = webdriver.ChromeOptions()
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')

    experimentalFlags = [
        "same-site-by-default-cookies@2",
        "cookies-without-same-site-must-be-secure@2", ]
    chromeLocalStatePrefs = {"browser.enabled_labs_experiments": experimentalFlags}
    option.add_experimental_option("localState", chromeLocalStatePrefs)

    option.add_experimental_option('w3c', False)

    UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
         'Mobile/15E148 MicroMessenger/8.0.15(0x18000f24) NetType/WIFI Language/zh_CN '
    mobileEmulation = {"deviceMetrics": {"width": 376, "height": 812, "pixelRatio": 2.0}, "userAgent": UA}
    option.add_experimental_option('mobileEmulation', mobileEmulation)

    # PROXY = "175.146.212.92:4256"
    # option.set_capability("proxy", {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "proxyType": "MANUAL",
    # })

    now = (int(round(time.time() * 1000)))
    for i in range(0, 100):
        process(url, option)
    now2 = (int(round(time.time() * 1000)))
    print(now2 - now)
