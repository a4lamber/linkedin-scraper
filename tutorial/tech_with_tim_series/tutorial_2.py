'''
 # @ Author: Your name
 # @ Create Time: 2023-02-11 15:48:35
 # @ Modified by: Your name
 # @ Modified time: 2023-02-11 15:50:45
 # @ Description:
 
search priority:
    id > name > class_name 
    since id is more unique
explicit wait:
页面转换需要时间, 要explicit wait, 加一点tolerance;
 '''


from selenium import webdriver
# interact with text
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up the location of the chrome driver and website you want to go to
PATH = "./chromedriver"
url = "https://techwithtim.net"


# open chrome
driver =webdriver.Chrome(PATH)
# open the website
driver.get(url)

# print the title of the website
print(driver.title)

# search element by name "s"
search = driver.find_element_by_name("s")

# type "test" in the search bar
search.send_keys("test")

# 按enter
search.send_keys(Keys.RETURN)




# print the source code for the page it's at
# print(driver.page_source)


try:
    # web for maximum of 10 secs untils element is present
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"main"))
    # print the text of the main
    # print(main.text)
    
    # articles = main.find_elements_by_tag_name("article")
    # for article in articles:
    #     header = article.find_element_by_class_name("entry-title")
    #     print(header.text)
    )
finally:
    # close the browser
    driver.quit()


