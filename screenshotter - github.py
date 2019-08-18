# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 23:42:33 2019

@author: User
"""

#https://stackoverflow.com/questions/39600245/how-to-capture-website-screenshot-in-high-resolution

#https://stackoverflow.com/questions/6775351/clicking-at-coordinates-without-identifying-element
import numpy as np
from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.firefox.options import Options
options = Options()
options.set_preference("dom.webnotifications.enabled", False)

driver=webdriver.Firefox(executable_path=r'C:\Users\User\Desktop\fonctions_python\geckodriver.exe',log_path=r'C:\Users\User\Desktop\fonctions_python\geckodriver.log',firefox_options=options)
#driver=webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\fonctions_python\chromedriver.exe')
"""
driver.get('https://www.google.com/search?q=animals&client=firefox-b-d&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi17Y-r94rkAhVNdhoKHe5vAgAQ_AUIESgB&biw=1138&bih=545')

time.sleep(3)

from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_by_offset(1360,384).click().perform()

time.sleep(5)

"""
driver.get('https://biblio.manuel-numerique.com/')

time.sleep(10)

emailelement=driver.find_element(By.XPATH,'.//*[@id="loginField"]')
emailelement.send_keys('insert login details here')

passelement=driver.find_element(By.XPATH,'.//*[@id="passwordField"]')
passelement.send_keys('insert login details here')

buttons=driver.find_elements_by_tag_name('button')

for button in buttons:
    if button.text=='Connexion':
        button.click()

time.sleep(5)

from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
#1366,654
actions.move_by_offset(100,350).click().perform()

time.sleep(7)


from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

for i in range(654):
    #driver.save_screenshot(str(i)+'.png')
    #time.sleep(1)
    #actions.send_keys(Keys.ARROW_RIGHT).perform()
    #unused because causes weird behavior
    actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'),0,0)
    actions.move_by_offset(1360,375).click().perform()
    time.sleep(10)




#actions = ActionChains(driver)
#actions.move_by_offset(200,400).click().perform()



#driver.save_screenshot('screenie.png')

time.sleep(5)

driver.quit()


#driver.set_window_size(3000,800)

#driver.execute_script("document.body.style.zoom='250%'")

#browser.execute_script("document.body.style.webkitTransform = 'scale(2.5)'")
