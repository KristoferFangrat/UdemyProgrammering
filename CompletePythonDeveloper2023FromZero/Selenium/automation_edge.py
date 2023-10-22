from selenium import webdriver

# Initialize the Edge driver
driver = webdriver.Edge()

# Open a webpage
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
webdriver.Edge.maximize_window()
# Print the page title
print("Page title is: %s" % (driver.title))

# Close the browser
# driver.quit()


