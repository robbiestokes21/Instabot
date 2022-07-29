from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
    browser.get("https://www.instagram.com/?hl=en")
    time.sleep(5)
    
    #This was used before Selenium  4.3.0
    #username = browser.find_element_by_css_selector("[name='username']")
    #password = browser.find_element_by_css_selector("[name='password']")
    #login = browser.find_element_by_css_selector("button")
    
    #The new semtex after Selenium 4.3.0
    username = browser.find_element(By.NAME, 'username')
    password = browser.find_element(By.NAME, 'password')
    login = browser.find_element(By.CSS_SELECTOR , 'button')

    #YOUR USERNAME GOES HERE
    username.send_keys("username")
    #YOUR Password GOES HERE
    password.send_keys("password")
    login.click()



    time.sleep(5)


def Visit_Tag(browser, url):
    sleepy_time = 5
    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements(By.XPATH, "//div[@class='_aagu']")

    image_count = 0

    for picture in pictures:
        if image_count >= 3:
            break

        picture.click()
        time.sleep(sleepy_time)

        heart = browser.find_element(By.XPATH, "//span[@class='_aamw']")
        heart.click()
        time.sleep(sleepy_time)

        close = browser.find_element(By.CSS_SELECTOR, "svg[aria-label='Close']")
        close.click()
        time.sleep(sleepy_time)

        image_count += 1
        time.sleep(sleepy_time)

def main():

    # Used for Firefox
    browser = webdriver.Firefox()

    # Used for Chrome
    #browser = webdriver.Chrome()

    # Used for Edge
    #browser = webdriver.Edge()

    # Used for ChromiumEdge
    #browser = webdriver.ChromiumEdge()

    # Used for Ie
    #browser = webdriver.Ie()

    # Used for Safari
    #browser = webdriver.Safari()

    login(browser)

    tags = [ 
        "programming",
        "softwaredeveloper",
        "programminglife",
        "programmerslife",
        "programmerlife",
        "developerlife",
        "programmers",
    ]

    while True:
        for tag in tags:
            Visit_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)

main()
