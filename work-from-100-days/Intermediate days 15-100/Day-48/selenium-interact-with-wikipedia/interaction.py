from selenium import webdriver
# need this to input enter key strike
from selenium.webdriver.common.keys import Keys
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articlecount=driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
article_count=driver.find_element_by_css_selector("#articlecount a")

# print(article_count.text)

# call the on click to click on the article count
# article_count.click()

# another way using find works well with links - wiki all portals
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# automating typeing into search field
search_field = driver.find_element_by_name("search")
# use send keys to search for python
search_field.send_keys("Python")
# hitting enter key need the selenium import for common keys
search_field.send_keys(Keys.ENTER)
python_link = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[3]/ul/li[2]/div[1]/a')
python_link.click()