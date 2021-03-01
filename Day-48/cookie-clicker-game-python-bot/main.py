from selenium import webdriver
# need this to input enter key strike
from selenium.webdriver.common.keys import Keys
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
GRANDMA_COUNTER = 0


for i in range(1,202):
    single_click = driver.find_element_by_xpath('//*[@id="bigCookie"]')
    single_click.click()
#     GRANDMA_COUNTER = GRANDMA_COUNTER +1

#     print(GRANDMA_COUNTER)


# for GRANDMA_COUNTER in range(1, 202):
#     if(GRANDMA_COUNTER % 100 ):
#         grandma = driver.find_element_by_xpath('//*[@id="product1"]')
#         grandma.click()

# cursor = driver.find_element_by_xpath('//*[@id="product0"]')
# cursor.click()