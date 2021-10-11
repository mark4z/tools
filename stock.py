import time

from selenium import webdriver


def process(url_str, options):
    with webdriver.Remote(
            options=options,
            command_executor='http://127.0.0.1:4444/wd/hub'
    ) as driver:
        # with webdriver.Chrome(
        #         options=options,
        # ) as driver:
        driver.get(url_str)

        cookies = driver.get_cookies()
        print(cookies)

        driver.get('http://cnzz.mmstat.com')
        cookies = driver.get_cookies()
        print(cookies)


if __name__ == '__main__':
    url = "http://47.100.220.7/index2.html"
    # url = "http://www.baidu.com"

    option = webdriver.ChromeOptions()
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')

    experimentalFlags = [
        "same-site-by-default-cookies@2",
        "cookies-without-same-site-must-be-secure@2", ]
    chromeLocalStatePrefs = {"browser.enabled_labs_experiments": experimentalFlags}
    option.add_experimental_option("localState", chromeLocalStatePrefs)

    UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

    mobileEmulation = {"deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 2.0}, "userAgent": UA}
    option.add_experimental_option('mobileEmulation', mobileEmulation)

    # PROXY = "175.146.212.92:4256"
    # option.set_capability("proxy", {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "proxyType": "MANUAL",
    # })

    now = (int(round(time.time() * 1000)))
    for i in range(0, 1):
        process(url, option)
    now2 = (int(round(time.time() * 1000)))
    print(now2 - now)
