from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)
# can now run the driver and open amazon
driver.get("https://www.amazon.com")
# this closes the page or tab that is open
# driver.close()
# this actualy quits the entire browser all tabs the entier program
driver.quit()