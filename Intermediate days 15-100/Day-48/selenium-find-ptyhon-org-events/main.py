from selenium import webdriver
# because the \ is the escape key in python need to add an r in fromt of the driver path string
chrome_driver_path = r"C:\Users\Hackathon\Documents\chromedriver_win32\chromedriver.exe"
# instantiate the webdriver - initializing a new object with the executable path
driver= webdriver.Chrome(executable_path=chrome_driver_path)

# passing in the link to website
driver.get("https://www.python.org/")
# get the Event date and name from the web page and create a dictionary
# in div class event-widget time div


event_times = driver.find_elements_by_css_selector(".event-widget time")
# this returns a seleneum object so need to use a for loop to see what time is
# for time in event_times:
#     print(time.text)


event_names = driver.find_elements_by_css_selector(".event-widget li a")
# this returns a seleneum object so need to use a for loop to see what time is
# for name in event_names:
#     print(name.text)
## events dictionary to push to
events={}
for n in range(len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name": event_names[n].text,
    }


print(events)


driver.quit()