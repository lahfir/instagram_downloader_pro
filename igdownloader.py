import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime as dt
import download
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome(
    "C://chromedriver_win32//chromedriver.exe"
)
delay = 10
# driver.maximize_window()

driver.get("https://www.instagram.com/")

WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[name='username']")))

un = driver.find_element_by_css_selector("input[name='username']")
pd = driver.find_element_by_css_selector("input[name='password']")

un.send_keys('USER')
pd.send_keys('PD')
# need to send un pd values


WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[3]/button').click()  # Log In

WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div/div/div/button'
).click()  # not now 1

WebDriverWait(driver, delay).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

accounts = ['https://www.instagram.com/24hoursuccess/', 'https://www.instagram.com/fuck_failure/',
            'https://www.instagram.com/motivationmafia/', 'https://www.instagram.com/the.success.club/',
            'https://www.instagram.com/addicted2success/', 'https://www.instagram.com/millionaire_mentor/',
            'https://www.instagram.com/ambitioncircle/', 'https://www.instagram.com/before5am/',
            'https://www.instagram.com/luxquotes/', 'https://www.instagram.com/motivation_mondays/',
            'https://www.instagram.com/millionaire.dream/', 'https://www.instagram.com/success.slogans/',
            'https://www.instagram.com/6amsuccess/', 'https://www.instagram.com/word_of_wizard/',
            'https://www.instagram.com/foundr/', 'https://www.instagram.com/tombilyeu/',
            'https://www.instagram.com/age_of_attitude/', 'https://www.instagram.com/entrepreneurshipfacts/',
            'https://www.instagram.com/300xsuccess/']
links = []

# for m in accounts:
#     driver.get(m)
#     time.sleep(3)
#     for i in range(100):
#         for j in range(1, 4):
#             try:
#                 baseclass = driver.find_element_by_xpath(
#                     '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div['+str((i+1))+']/div['+str(j)+']/a/div[2]')
#             except:
#                 try:
#                     baseclass = driver.find_element_by_xpath(
#                         '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div['+str((i+1))+']/div['+str(j)+']/a/div/div[1]/img')
#                     download.download_image(baseclass.get_attribute(
#                         'src'), 'D:\\ContentC\\Animesh\\SinglePosts\\raw\\')
#                     ocr.load_image('D:\\ContentC\\Animesh\\SinglePosts\\raw\\')
#                     links.append(baseclass.get_attribute('src'))
#                 except Exception as e:
#                     pass

scroll_dist = 15


def scroll(account):
    if m == 'https://www.instagram.com/motivation_mondays/':
        scroll_pos = 2000
        for i in range(50):
            driver.execute_script("window.scrollTo(0,"+str(scroll_pos)+")")
            scroll_pos += 1300
            time.sleep(1)
    else:
        scroll_pos = 2000
        for i in range(scroll_dist):
            driver.execute_script("window.scrollTo(0,"+str(scroll_pos)+")")
            scroll_pos += 1300
            time.sleep(1)


def accountclick():
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[10]/div[1]/a/div/div[2]').click()
    except:
        try:
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[10]/div[1]/a/div/div[2]').click()
        except:
            pass


time.sleep(2)

likewise = False
postwise = True
likes = 0
for m in ['https://www.instagram.com/300xsuccess/']:
    print(m[26:])
    driver.get(m)
    time.sleep(3)
    try:
        # scroll(m)
        try:
            # accountclick()
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
        except:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
            except:
                try:
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                except:
                    driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
        time.sleep(2)
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='g47SY ']")))
        posts = driver.find_element_by_xpath("//span[@class='g47SY ']").text
        for i in range(10):
            try:
                driver.find_element_by_link_text("Next").click()
                time.sleep(0.5)
            except NoSuchElementException:
                break
            try:
                try:
                    driver.find_element_by_xpath(
                        '//button[text()="Toggle audio"]')
                    print('video')
                    continue
                except:
                    driver.find_element_by_xpath(
                        '//video[type="video/mp4"]')
                    print('IGTV')
                    continue
            except:
                try:
                    driver.find_element_by_xpath(
                        '//div[@class="    coreSpriteRightChevron  "]')
                    print('carousel')
                    continue
                except:
                    try:
                        baseclass = ''
                        likes = ''
                        try:
                            baseclass = driver.find_element_by_xpath(
                                '/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/img')
                            if likewise:
                                try:
                                    likes = driver.find_element_by_xpath(
                                        '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div[2]/button/span').text
                                except:
                                    likes = driver.find_element_by_xpath(
                                        '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button/span').text
                                    time.sleep(0.7)
                        except:
                            try:  # Getting images and likes
                                baseclass = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                                    (By.XPATH, '//div[@class="KL4Bh"]/img')))
                                baseclass = driver.find_element_by_xpath(
                                    '//div[@class="KL4Bh"]/img')
                                if likewise:
                                    try:
                                        likes = driver.find_element_by_xpath(
                                            '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div[2]/button/span').text
                                    except:
                                        likes = driver.find_element_by_xpath(
                                            '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button/span').text
                                        time.sleep(0.7)
                            except:
                                print('Video or Any  other file or cannot grab likes')
                        if likewise:
                            print(i, likes)
                        print(i, 'driver', 'img', end=' ')
                        alt = random.choice([g for g in range(1000)])
                        try:
                            alt = baseclass.get_attribute('alt')
                            alt = str(alt)
                            print(i, 'alt')
                        except:
                            pass
                        if likewise:
                            likes = likes.replace(',', '')
                            like = int(likes.strip())
                            loc = ''
                            if like >= 5000 and like <= 10000:
                                download.download_image(str(baseclass.get_attribute(
                                    'src')), 'D:/ContentC/VideoContents for D4B/Unicorn/Above 5000/', alt)
                                print('passed')
                            elif like >= 10000 and like <= 15000:
                                download.download_image(str(baseclass.get_attribute(
                                    'src')), 'D:/ContentC/VideoContents for D4B/Unicorn/Above 10000/', alt)
                                print('passed')
                            elif like >= 15000 and like <= 20000:
                                download.download_image(str(baseclass.get_attribute(
                                    'src')), 'D:/ContentC/VideoContents for D4B/Unicorn/Above 15000/', alt)
                                print('passed')
                            else:
                                download.download_image(str(baseclass.get_attribute(
                                    'src')), 'D:/ContentC/VideoContents for D4B/Unicorn/Above 20000/', alt)
                                print('passed')
                            links.append(baseclass.get_attribute('src'))
                            time.sleep(2)
                        if postwise:
                            download.download_image(str(baseclass.get_attribute(
                                'src')), 'D:/ContentC/VideoContents for D4B/Unicorn/Business/', str(alt))
                            print('passed')
                    except Exception as e:
                        print(e, end='\n')
                        print(i, 'Taking time to load')
                        pass
            time.sleep(5)
    except KeyboardInterrupt:
        break
    print('\n')

print(len(links))
