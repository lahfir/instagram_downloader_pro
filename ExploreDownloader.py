import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime as dt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import download
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(
    "C://chromedriver_win32//chromedriver.exe"
)  # PATH TO YOUR CHROMDRIVER
delay = 10
driver.maximize_window()

driver.get("https://www.instagram.com/")

WebDriverWait(driver, delay).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
)

un = driver.find_element_by_css_selector("input[name='username']")
pd = driver.find_element_by_css_selector("input[name='password']")

un.send_keys("")  # INSTAGRAM USERNAME
pd.send_keys("")  # INSTAGRAM PASSWORD
# need to send un pd values


WebDriverWait(driver, delay).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()  # Log In

WebDriverWait(driver, delay).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
    )
)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div/div/div/button'
).click()  # not now 1

WebDriverWait(driver, delay).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")
    )
)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

driver.get("https://www.instagram.com/explore/")

WebDriverWait(driver, delay).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[1]',
        )
    )
)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]'
).click()

WebDriverWait(driver, delay).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/img")
    )
)

for i in range(100):
    try:
        driver.find_element_by_link_text("Next").click()
        time.sleep(0.5)
    except NoSuchElementException:
        break
    try:
        try:
            driver.find_element_by_xpath('//button[text()="Toggle audio"]')
            print("video")
            continue
        except:
            driver.find_element_by_xpath('//video[type="video/mp4"]')
            print("IGTV")
            continue
    except:
        try:
            driver.find_element_by_xpath('//div[@class="    coreSpriteRightChevron  "]')
            print("carousel")
            continue
        except:
            try:
                baseclass = ""
                likes = ""
                try:
                    baseclass = driver.find_element_by_xpath(
                        "/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/img"
                    )
                except:
                    try:  # Getting images and likes
                        baseclass = WebDriverWait(driver, delay).until(
                            EC.presence_of_element_located(
                                (By.XPATH, '//div[@class="KL4Bh"]/img')
                            )
                        )
                        baseclass = driver.find_element_by_xpath(
                            '//div[@class="KL4Bh"]/img'
                        )
                        time.sleep(0.7)
                    except:
                        print("Video or Any  other file or cannot grab likes")

                alt = random.choice([g for g in range(1000)])

                try:
                    alt = baseclass.get_attribute("alt")
                    alt = str(alt)
                    print(i, "alt")
                except:
                    pass

                download.download_image(
                    str(baseclass.get_attribute("src")),
                    "D:/ContentC/VideoContents for D4B/Unicorn/Explore/",
                    str(alt),
                )
                print("passed")
            except Exception as e:
                print(e)
    time.sleep(3)
