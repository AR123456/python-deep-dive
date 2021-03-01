from selenium import webdriver
# need this to input enter key strike
from selenium.webdriver.common.keys import Keys
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# automating typeing into first name  field
first_name = driver.find_element_by_name("fName")
# use send keys to search for python
first_name.send_keys("Sally")

first_name.send_keys(Keys.TAB)
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Smith")
last_name.send_keys(Keys.TAB)
form_email = driver.find_element_by_name("email")
form_email.send_keys("test@test.com")


python_link = driver.find_element_by_xpath('/html/body/form/button')
python_link.click()