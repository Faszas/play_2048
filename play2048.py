from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import requests
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path = 'geckodriver.exe')
driver.get('https://play2048.co/')

# soup = BeautifulSoup(driver.find_element_by_class_name('best-container').get_attribute('innerHTML'), features = 'lxml')
#
# print(soup.text)


gamePause = False


try:
    while True:
        getscore = 0
        link = driver.find_element_by_tag_name('body')

        link.send_keys(Keys.ARROW_LEFT)
        link.send_keys(Keys.ARROW_DOWN)
        link.send_keys(Keys.ARROW_UP)
        link.send_keys(Keys.ARROW_RIGHT)
        try:
            retry = driver.find_element_by_class_name('retry-button')
            getscore = BeautifulSoup(link.find_element_by_class_name('score-container').get_attribute('innerHTML'), features = 'lxml').text
            retry.click()
            gamePause = True
        except:
            pass

        if gamePause:

            with open('score_2048.txt', 'a') as f:

                text = "Score: {} {}\n".format(getscore, str(datetime.datetime.now()))
                f.write(text)
                f.close()

            print(text)
            gamePause = False

except Exception as error:
    print(error)