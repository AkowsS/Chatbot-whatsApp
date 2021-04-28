from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

class botinho:
    def __init__(self):
        
        self.driver = webdriver.Chrome(executable_path=r"")
    def home(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        time.sleep(15)

        while(1):
            if ( len((driver.find_elements_by_class_name("_38M1B"))) > 0 ): 

                campo_msg = driver.find_element_by_class_name("_38M1B")
                print("mensagem printada: ",campo_msg)
                campo_msg.click()
                time.sleep(3)

                if ( len((driver.find_elements_by_xpath("//footer[@class='_3uxr9']"))) > 0 ):
                    print("possui chat")
                    envia_msg = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
                    envia_msg.send_keys('Hi -bot')
                    envia_msg.send_keys(Keys.ENTER)
                    time.sleep(5) 

                else:
                    print("naao possui chat")
                    time.sleep(2)
            else:
                time.sleep(15)
    
bot = botinho()
bot.home()
