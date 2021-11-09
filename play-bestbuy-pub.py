import time
import subprocess
import smtplib, ssl
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import re
import sys

options = Options()

driver = webdriver.Chrome(options=options)  # Optional argument, if not specified will search path.

port = 465  # For SSL
password = "YOUR EMAIL PASSWORD" #change to your email password
sender_email = "YOUR EMAIL" #change to your email address
receiver_email = "YOUR EMAIL" #change to your email address


# Create a secure SSL context
context = ssl.create_default_context()


#the page where best buy lists the ps5
driver.get('https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')

pscommand = 'Invoke-Command $SMTPClient.Send($EmailFrom, $EmailTo, $Subject, $Body)'

def fmail():

    message2 = """\
    Subject: Playstation Available

    Playstation 5 Available at Best Buy

    https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149""".format()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("YOUR LOGIN", password) #change to your login*****************************************
        server.sendmail(sender_email, receiver_email, message2)

try:
    #the web element to find whether it is sold out or available
    content2 = driver.find_element_by_xpath('//button[@class="c-button c-button-disabled c-button-lg c-button-block add-to-cart-button"]').text
    if content2 == "Sold Out":
        print("the Playstation is unavailable")
#        fmail()
#    print(content2)
    else:
        fmail()
        #print(content2 = driver.find_element_by_xpath('//button[@class="c-button c-button-disabled c-button-lg c-button-block add-to-cart-button"]').text)
except:
    fmail()
    #print(content2 = driver.find_element_by_xpath('//button[@class="c-button c-button-disabled c-button-lg c-button-block add-to-cart-button"]').text)
#print(content2)'



'''
try:
        #content = driver.find_element_by_xpath('//a[@class="a-link-normal"]//span[@class="a-size-base a-color-price"]').text
    content = driver.find_element_by_xpath('//span[@class="price-characteristic"]').text #Get the Price as a string from amazon
    priceprep = content.replace(',','') #Remove Comma from string
    price = float(priceprep[0:8]) #Remove $ from string and convert to float

    if price > 551:
        print("no good deals", price)
        fmail(price)
#          print()
    else :
        fmail(price)
            #print("Good Deal! $",price)
#        time.sleep(3600)
except:
    print("Found incorrect content from webpage and couldn't parse")
'''

#print(price)
driver.quit()
sys.exit()
