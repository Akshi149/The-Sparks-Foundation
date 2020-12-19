import unittest 
from selenium import webdriver 
import time

# inherit TestCase Class and create a new test class 
class The_Sparks_Foundation_TestCase(unittest.TestCase): 

	# initialization of webdriver 
	def setUp(self): 
		self.driver = webdriver.Chrome(r'E:\SeleniumTests\browsers\chromedriver.exe')
		self.driver.maximize_window()


	def test_ContactUs_page(self): 
		driver = self.driver # get driver 	
		driver.get("https://www.thesparksfoundationsingapore.org/") # get the sparksfoundationsingapore.org using selenium 
		self.assertIn("The Sparks Foundation | Home", driver.title) # assertion to confirm if title has the sparks foundation keyword in it 
		elem1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[6]/a')
		elem1.click()
		driver.execute_script("window.scrollTo(0,500)")
		time.sleep(3)


	def test_Navbar_and_logo_redirect(self):
		driver = self.driver 
		driver.get("https://www.thesparksfoundationsingapore.org/") 
		elem2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/h1/a')
		elem2.click()
		driver.execute_script("window.scrollTo(0,1000)")
		time.sleep(3)


	def test_know_more_buttons(self):
		driver = self.driver 
		driver.get("https://www.thesparksfoundationsingapore.org/")
		driver.execute_script("window.scrollTo(0,500)") 
		time.sleep(3)
		elem3= driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/a')
		elem3.click()
		time.sleep(3)


	def test_Navbar_dropdown(self):
		driver = self.driver 
		driver.get("https://www.thesparksfoundationsingapore.org/") 
		elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/a')
		elem4.click()
		time.sleep(3)
		elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/ul/li[1]/a')
		elem4.click()
		time.sleep(3)
		driver.execute_script("window.scrollTo(0,1000)")

	
	def test_carousel_button(self):
		driver = self.driver 
		driver.get("https://www.thesparksfoundationsingapore.org/") 
		time.sleep(1)
		elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a')
		elem4.click()
		time.sleep(3)

	
	def test_joinUs_pages(self):
		driver = self.driver 
		driver.get("https://www.thesparksfoundationsingapore.org/") 
		elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/a')
		elem4.click()
		time.sleep(3)
		elem4 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/ul/li[5]/a')
		elem4.click()
		driver.execute_script("window.scrollTo(0,400)")
		time.sleep(3)
		elem4 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul/li[3]/a')
		elem4.click()
		time.sleep(3)
	

	def test_footer_socialmedia_links(self):
		driver = self.driver 
		driver.get("https://www.thesparksfoundationsingapore.org/") 
		p = driver.current_window_handle
		chwd = driver.window_handles
		driver.execute_script("window.scrollTo(0,3000)")
		time.sleep(3)
		elem5 = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a') # linkedin link
		elem5.click()
		time.sleep(3)
		for w in chwd:
			if(w!=p):
				driver.switch_to.window(p)
		
		elem5 = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[3]/a') # medium link
		elem5.click()
	
		
	# cleanup method called after every test performed
	def tearDown(self): 
		self.driver.close() 


# execute the script 
if __name__ == "__main__": 
	unittest.main() 