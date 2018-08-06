print ("hello world")
if True:
    print("1")
    print("2")

else:
    print("0")

    print("next statement")
for x in range(6):
         print(x)
print("next statement")
for x in range(2, 6):
  print(x)
print("next stsatement")
for y in range(2, 8, 9):
      print(y)
'''
print("recurssion")

def tri_recursion(k):

    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
         result = 0
         return result
print("\n\nRecursion Example Results")
tri_recursion(6)
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('D:\study\python\chromedriver_win32')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Friend\'s Name"'
 
# Replace the below string with your own message
string = "Message sent using Python!!!"
 
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
