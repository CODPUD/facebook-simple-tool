from selenium import webdriver
import time
from spintax import spin
from random import randint


post_link = ""


def Auth(username, password):

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument(f"user-data-dir=profiles/{username}")
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    driver.get(post_link)


    try:
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        time.sleep(2)
        driver.find_element_by_id('loginbutton').click()
    except:
        pass
    time.sleep(3)
    LikeComment(driver)

def ScrollWeb(driver, scroll):
    try:
        driver.execute_script(f"window.scrollTo(0, {scroll})")
    except:
        pass

def LikeComment(driver):
    driver.get(post_link)
    time.sleep(1)

    comment_fields = driver.find_elements_by_xpath('//div[@aria-label="Comment on post"]')

    count = 100
    for i in range(20):
        like_buttons = driver.find_elements_by_xpath('//div[@aria-label="Like"]')
        try:
            like_buttons[1].click()
        except:
            pass
        if(len(comment_fields) == 0):
            ScrollWeb(driver, count)
            comment_fields = driver.find_elements_by_xpath('//div[@aria-label="Comment on post"]')
            count += 100
        else:
            break

    time.sleep(3)


    with open("comment.txt", "r") as file:
        comments = file.readlines()

    comment = comments[randint(0, len(comments)-1)].rstrip("\n")

    try:
        comment_fields[0].send_keys(spin(f"{comment}\n"))
    except:
        pass

    time.sleep(5)
    #Quit(driver)

def Quit(driver):
    driver.close()

def main():
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()

    for acc in accounts:
        data = acc.rstrip("\n").split(":")
        username = data[0]
        password = data[1]
        print(username, password)
        Auth(username, password)

if __name__ == '__main__':
    main()
