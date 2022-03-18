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
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

driver = webdriver.Chrome(
    "C://chromedriver_win32//chromedriver.exe"
)  # PATH TO CHROMEDRIVER
delay = 10
# driver.maximize_window()

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

accounts = [
    "https://www.instagram.com/24hoursuccess/",
    "https://www.instagram.com/motivationmafia/",
    "https://www.instagram.com/the.success.club/",
    "https://www.instagram.com/addicted2success/",
    "https://www.instagram.com/millionaire_mentor/",
    "https://www.instagram.com/ambitioncircle/",
    "https://www.instagram.com/before5am/",
    "https://www.instagram.com/luxquotes/",
    "https://www.instagram.com/motivation_mondays/",
    "https://www.instagram.com/millionaire.dream/",
    "https://www.instagram.com/success.slogans/",
    "https://www.instagram.com/6amsuccess/",
    "https://www.instagram.com/word_of_wizard/",
    "https://www.instagram.com/foundr/",
    "https://www.instagram.com/tombilyeu/",
    "https://www.instagram.com/age_of_attitude/",
    "https://www.instagram.com/entrepreneurshipfacts/",
    "https://www.instagram.com/300xsuccess/",
]  # list of accounts from which to download
links = []


def scroll(scroll_pos):
    driver.execute_script("window.scrollTo(0," + str(scroll_pos) + ")")
    scroll_pos += 1300
    time.sleep(2)
    return scroll_pos


def fetch():
    video = False
    carousel = False
    error = False
    for i in range(1, 11):
        for j in range(1, 4):
            baseclass = 0
            try:  # If highlights are present
                try:
                    baseclass = driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div['
                        + str(i)
                        + "]/div["
                        + str(j)
                        + "]/a/div/div[1]/img"
                    )
                    if driver.find_element_by_xpath("//span[@aria-label='Video']"):
                        video = True
                    elif driver.find_element_by_xpath("//span[@aria-label='Carousel']"):
                        carousel = True
                except:
                    try:
                        baseclass = driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div["
                            + str(i)
                            + "]/div["
                            + str(j)
                            + "]/a/div/div[1]/img"
                        )
                    except:
                        try:  # If highlights are not present
                            baseclass = driver.find_element_by_xpath(
                                '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div['
                                + str(i)
                                + "]/div["
                                + str(j)
                                + "]/a/div/div[1]/img"
                            )
                            if driver.find_element_by_xpath(
                                "//span[@aria-label='Video']"
                            ):
                                video = True
                            elif driver.find_element_by_xpath(
                                "//span[@aria-label='Carousel']"
                            ):
                                carousel = True
                        except:
                            try:
                                baseclass = driver.find_element_by_xpath(
                                    "/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div["
                                    + str(i)
                                    + "]/div["
                                    + str(j)
                                    + "]/a/div/div[1]/img"
                                )
                                if driver.find_element_by_xpath(
                                    "//span[@aria-label='Video']"
                                ):
                                    video = True
                                elif driver.find_element_by_xpath(
                                    "//span[@aria-label='Carousel']"
                                ):
                                    carousel = True
                            except:
                                try:
                                    baseclass = driver.find_element_by_xpath(
                                        '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div['
                                        + str(i)
                                        + "]/div["
                                        + str(j)
                                        + "]/a/div/div[1]/img"
                                    )
                                    if driver.find_element_by_xpath(
                                        "//span[@aria-label='Video']"
                                    ):
                                        video = True
                                    elif driver.find_element_by_xpath(
                                        "//span[@aria-label='Carousel']"
                                    ):
                                        carousel = True
                                except:
                                    baseclass = driver.find_element_by_xpath(
                                        "/html/body/div[1]/section/main/div/div[3]/article/div/div/div["
                                        + str(i)
                                        + "]/div["
                                        + str(j)
                                        + "]/a/div/div[1]/img"
                                    )
                                    if driver.find_element_by_xpath(
                                        "//span[@aria-label='Video']"
                                    ):
                                        video = True
                                    elif driver.find_element_by_xpath(
                                        "//span[@aria-label='Carousel']"
                                    ):
                                        carousel = True
            except Exception as e:
                print(i, j, e, "error")
                error = True
            if not (video) and not (carousel) and not (error):
                download.download_image(
                    str(baseclass.get_attribute("src")),
                    "D:/ContentC/VideoContents for D4B/Unicorn/Business/",
                    str(baseclass.get_attribute("alt")),
                )
            if i % 5 == 0:
                scroll()


fine = False


for acc in accounts[:3]:

    req_images = 120

    scroll_pos = 2000

    driver.get(acc)

    # To check if the posts are loaded
    WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="KL4Bh"]/img'))
    )

    no_of_posts = str(driver.find_element_by_xpath("//span[@class='g47SY ']").text)

    no_of_posts = no_of_posts.replace(",", "")
    no_of_posts = int(no_of_posts.strip())

    if req_images < no_of_posts:
        pass
    else:
        req_images = no_of_posts

    src = []
    alt = []

    images = driver.find_elements_by_xpath('//div[@class="KL4Bh"]/img')

    src = [i.get_attribute("src") for i in images]
    alt = [i.get_attribute("alt") for i in images]

    while True:
        if len(images) <= req_images:
            scroll_pos = scroll(scroll_pos)

            im = driver.find_elements_by_xpath('//div[@class="KL4Bh"]/img')

            imgs = [v for v in im if v not in images]

            sr, al = [], []

            for j in imgs:
                sr.append(j.get_attribute("src"))
                al.append(j.get_attribute("alt"))

            src.extend(sr)
            alt.extend(al)

            images.extend(imgs)

            try:
                for index, im in enumerate(images):
                    if im.find_element_by_xpath("//span[@aria-label='Video']"):
                        del images[index]
                        del src[index]
                        del alt[index]
                    elif im.find_element_by_xpath("//span[@aria-label='Carousel']"):
                        del images[index]
                        del src[index]
                        del alt[index]
            except:
                pass
        else:
            break

    driver.execute_script("window.scrollTo(0,0)")

    for sr, al in zip(src, alt):
        download.download_image(sr, "PATH TO DOWNLOAD", al)
