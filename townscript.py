from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

def TownScript():
    PATH="C:\Program Files (x86)\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.townscript.com/in/online")

    driver.implicitly_wait(5)


    link=driver.find_element_by_xpath("/html/body/app-root/div/app-home-page/div[1]/app-online-digest-view/ts-header/nav[1]/div/div[6]/div")
    link.click()

    driver.implicitly_wait(5)

    email=driver.find_element_by_id("email")
    email.send_keys("aniket76342@gmail.com")
    email.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    pwd=driver.find_element_by_id("user-pwd")
    pwd.send_keys("Qwerty@123")
    pwd.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    button = driver.find_element_by_xpath("/html/body/app-root/div/app-home-page/div[1]/app-online-digest-view/ts-header/nav[1]/div/div[5]/a")
    driver.execute_script("arguments[0].click();", button)

    driver.implicitly_wait(5)

    event=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[2]/h5")
    event.click()

    driver.implicitly_wait(5)
#                                        First Page                                                    #
    event_name=driver.find_element_by_id("event-name")
    event_name.send_keys("NLP AI AUTOMATION")

    event_display=driver.find_element_by_id("displayName")
    event_display.send_keys("NLP AI AUTOMATION")

    ## Event is Public Automatically

    datepick=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/event-basics-details-edit/div/div/div/div/form/div[1]/div/div[4]/div/div[1]/app-ts-date-time-picker/div/div[1]/input")
    datepick.clear()
    datepick.send_keys("09 Sep 2021")


    time=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/event-basics-details-edit/div/div/div/div/form/div[1]/div/div[4]/div/div[1]/app-ts-date-time-picker/div/div[2]').click()
    driver.find_element_by_xpath("//*[contains(text(), '4:30 AM')]").click()




    timeend = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/event-basics-details-edit/div/div/div/div/form/div[1]/div/div[4]/div/div[2]/app-ts-date-time-picker/div/div[2]').click()
    driver.find_element_by_xpath("//*[contains(text(), '6:30 AM')]").click()

    driver.find_element_by_xpath("//button[contains(text(), 'Submit')]").click()

    driver.implicitly_wait(5)

    #                                                 Second page                                                  #
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/location-details-edit/div/div/div/form/div[1]/div/div[1]/div[2]/label/span[1]").click() #'Physical Location'
    evntlink=driver.find_element_by_name('eventLink')
    evntlink.send_keys("https://meet.google.com/mhe-dbyw-epn")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/location-details-edit/div/div/div/form/div[2]/button").click()

    driver.implicitly_wait(5)
#                                            Third Page                                         #
    desc=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/description-details-edit/div/div/div/form/div[1]/div/div/div[2]/div[3]/div[3]')
    desc.send_keys("A event on NLP AI Automation")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/description-details-edit/div/div/div/form/div[2]/button").click()
    driver.implicitly_wait(5)
#                                                  Fourth Page                                                  #

    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/photos-edit/div/div[1]/div/div/div/i").click()
    driver.find_element_by_name("cover").send_keys(os.getcwd()+'/aniket.jpg')
    driver.find_element_by_id('image-upload-start').click()
    driver.implicitly_wait(5)
    #mobile
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/photos-edit/div/div[1]/div/div[2]/a")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/photos-edit/div/div[2]/div/div/div/i").click()
    driver.find_element_by_name("card").send_keys(os.getcwd() + '/aniket.jpg')
    driver.find_element_by_id('image-upload-start').click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/photos-edit/div/div[2]/div/div[2]/a")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/photos-edit/div/div[3]/a/button").click()
    driver.implicitly_wait(5)
 #                                             Ticket
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[2]/div/div/app-add-ticket-step-1/div/div/div/div/div/i").click()
    ticketName=driver.find_element_by_id("ticketName")
    ticketName.send_keys("Early Birds")

    totalticket=driver.find_element_by_id("totalTickets")
    totalticket.send_keys("100")

    totalprice = driver.find_element_by_id("ticketPrice")
    totalprice.send_keys("1000")

    ticketdate = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[2]/div/div/app-add-ticket-step-2/div/div/form/div[4]/div[1]/app-ts-date-time-picker/div/div[1]/input")
    ticketdate.clear()
    ticketdate.send_keys("09 May 2021")

    ticketend = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[2]/div/div/app-add-ticket-step-2/div/div/form/div[4]/div[2]/app-ts-date-time-picker/div/div[1]/input")
    ticketend.clear()
    ticketend.send_keys("09 Aug 2021")

    ticketstarttime = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[2]/div/div/app-add-ticket-step-2/div/div/form/div[4]/div[1]/app-ts-date-time-picker/div/div[2]/i[2]").click()
    driver.find_element_by_xpath("//*[contains(text(), '4:30 AM')]").click()

    ticketendtime = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[2]/div/div/app-add-ticket-step-2/div/div/form/div[4]/div[2]/app-ts-date-time-picker/div/div[2]/i[2]").click()
    driver.find_element_by_xpath("//*[contains(text(), '11:30 PM')]").click()


    driver.find_element_by_id("ticketAddButton").click()

    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[2]/div[2]/div/div/div[2]/span/div/mat-radio-group/mat-radio-button[2]/label/div[1]/div[2]").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/add-ticket-view/div/div/div[3]/button").click()

    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/button").click()

    link=driver.find_element_by_id("eventURL").text
    print(link)

if __name__=="__main__":
    TownScript()




