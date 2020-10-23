from selenium import webdriver

class WebDriver:
	def __new__(self, dev=False):
		driver_path = "C:/Users/Goofer/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver.exe"
		options = webdriver.ChromeOptions()

		if dev == False:
			options.add_argument('--window-size=10,10') 
			options.add_argument("--log-level=3")
			options.add_argument('--headless')
			options.add_argument('--hide-scrollbars')

		options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
		browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options)		
		return browser



