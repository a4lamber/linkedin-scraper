'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-02-11 15:39:10
 # @ Modified by: Your name
 # @ Modified time: 2023-02-11 15:50:30
 # @ Description:
 '''


from selenium import webdriver

path = "./chromedriver"
url = "https://techwithtim.net"


driver = webdriver.Chrome(executable_path = path)

driver.get(url)

# close the current tab
# driver.close()

# # close the browser
# driver.quit()

print(driver.title)