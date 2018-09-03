from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging

name = ""
passw = ""

logging.getLogger('').handlers = []
logging.basicConfig(
        format='%(asctime)s\n%(message)s',
        filename='Bot_likes.log',
        datefmt='%d/%m/%Y %H:%M:%S')

chrome_options = webdriver.ChromeOptions()
#chrome_options.set_headless()
#chrome_options.add_argument('--proxy-server=%s' % i)
chrome = webdriver.Chrome(chrome_options=chrome_options)

chrome.get('https://www.instagram.com/accounts/login/')
chrome.find_element_by_name("username").send_keys(name)
chrome.find_element_by_name("password").send_keys(passw)
chrome.find_element_by_class_name("_5f5mN").click()
time.sleep(3)

while True:
    try:
        chrome.get('http://biglike.org/')
        break
    except Exception:
        time.sleep(10)
        continue

chrome.find_element_by_class_name("btn").click()
time.sleep(1)
x = chrome.find_elements_by_class_name("btn-default")
x[2].click()
time.sleep(7)


while True:
    try:
        chrome.get('http://biglike.org/instalike')
    except Exception:
        time.sleep(10)
        continue

    kek = chrome.find_elements_by_id("tr_6563357")

    for z in kek:
        try:
            z.click()
            chrome.switch_to_window(chrome.window_handles[1])
        except Exception:
            continue

        time.sleep(3)
        
        try:
            chrome.find_element_by_xpath("//span[@aria-label='Нравится']").click()
            time.sleep(6)
        except Exception:
            time.sleep(2)
            chrome.close()
            chrome.switch_to_window(chrome.window_handles[0])
            continue

        chrome.close()
        chrome.switch_to_window(chrome.window_handles[0])
        time.sleep(1)
    
    x = chrome.find_element_by_id("points")
    print(x.text)
    logging.warning(str(x.text) + " points\n")

    zek = chrome.find_elements_by_class_name("btn-danger")
    for b in zek:
        try:
            b.click()
            time.sleep(1.5)
        except Exception:
            continue

    time.sleep(3)
