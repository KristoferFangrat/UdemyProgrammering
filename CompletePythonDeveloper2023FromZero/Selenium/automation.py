from selenium import webdriver

# Specify the path to the geckodriver executable
driver_path = './geckodriver'

# Create options for Firefox
options = webdriver.FirefoxOptions()
options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'  # Replace with your Firefox binary location

# Initialize the Firefox WebDriver with the specified options
firefox_browser = webdriver.Firefox(options=options)
firefox_browser.maximize_window()
firefox_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in firefox_browser.title
element = firefox_browser.find_element_by_class_name('btn-default')
print(element)

# Now you can use 'firefox_browser' for your automation tasks
