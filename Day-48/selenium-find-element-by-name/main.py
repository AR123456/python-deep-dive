from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

# passing in the link to the pressure cooker
driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")
# returns a selenium element , not html

print(search_bar)
# to get to attributes, tag names ect  use . notation
print(search_bar.tag_name)
# get specifice attrubute
print(search_bar.get_attribute("placeholder"))
driver.quit()