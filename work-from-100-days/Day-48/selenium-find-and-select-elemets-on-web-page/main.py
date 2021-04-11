from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

# passing in the link to the pressure cooker
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_2?dchild=1&keywords=instant+pot+duo+evo+plus+9-in-1+electric+pressure+cooker%2C+6-qt&qid=1612528757&sr=8-2")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.quit()