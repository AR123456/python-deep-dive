from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

# passing in the link to website
driver.get("https://www.python.org/")
# Xpath provides a way of addressing or pointing to different parts of an XML document, can be used to
# traverse the DOM
# in dev tools copy the path then paste

bug_link = driver.find_element_by_xpath('//*[@id="container"]/li[8]/ul/li[2]/a')
print(bug_link.text)
driver.quit()