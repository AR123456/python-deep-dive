from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

# passing in the link to the pressure cooker
driver.get("https://www.python.org/")

logo = driver.find_element_by_class_name("python-logo")
print(logo)
print(logo.size)
driver.quit()