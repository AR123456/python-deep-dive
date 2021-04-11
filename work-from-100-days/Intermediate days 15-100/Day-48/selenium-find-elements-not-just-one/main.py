from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

# passing in the link to the pressure cooker
driver.get("https://www.python.org/")
# on this web site inside the div with class documentation-widgets
# there is a version elements for all the find element methods
documentation_link = driver.find_elements_by_css_selector(".documentation-widget ")
print(documentation_link)
driver.quit()