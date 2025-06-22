import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# Ganti dengan link default TikTok
VIDEO_URL = 'https://vm.tiktok.com/ZSkvTRQ9J/'

views_sent = 0
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=800,660')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get('https://vipto.de/')

print('[!] Waiting for captcha (manual solve may still be needed in headless)...')
captcha = True

while captcha:
    try:
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div[4]/div/button').click()
    except (NoSuchElementException, ElementClickInterceptedException):
        continue
    captcha = False
    print('[!] Captcha solved, proceeding...')

driver.set_window_position(-10000, 0)

# Masukkan URL ke kolom
driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div/div/form/div/input').send_keys(VIDEO_URL)

while True:
    driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div/div/form/div/div/button').click()
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div/div/div/div/div[1]/div/form/button').click()
    except NoSuchElementException:
        print('[!] Invalid URL or captcha not completed. Exiting...')
        driver.quit()
        break
    else:
        views_sent += 1000
        print(f'[+] Views sent: {views_sent}')

        seconds = 62
        while seconds > 0:
            print(f'[i] Waiting {seconds} sec before next batch...', end='\r')
            seconds -= 1
            time.sleep(1)
