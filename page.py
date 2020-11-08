from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def go_to_yandex(driver, url='http://www.yandex.ru'):
	driver.get(url)
	assert 'Яндекс' in  driver.title #проверка на то что зашли на сайт Яндекс в заголовке сайта

def enter_to_search_field(driver, wait, findsrt):
	wait.until(EC.presence_of_element_located((By.ID, "text")))
	skb = driver.find_element_by_id("text")
	skb.send_keys(findsrt)
	return skb

def enter_and_check_suggest(driver, wait, findsrt):
	suggest = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='mini-suggest__popup-content']/li")))
	suggestvalue = driver.find_elements(By.XPATH, "//ul[@class='mini-suggest__popup-content']/li")
	is_str_preasent = False
	for element in suggestvalue:
		if findsrt in element.text.lower():
			is_str_preasent = True
	assert is_str_preasent #проверка на наличие строки в таблице с подсказками(suggest)

def click_enter(element):
	element.send_keys(Keys.RETURN)

def click_element(element):
	element.click()
	
def check_url(driver, wait, siteurl):
	wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='serp-list serp-list_left_yes']/li")))
	srresvalue = driver.find_elements(By.XPATH, "//ul[@class='serp-list serp-list_left_yes']/li/div")
	is_str_preasent = False
	for element in srresvalue[:5]:
		if siteurl in element.text.lower():
			is_str_preasent = True
	return is_str_preasent #

def search_img_link(driver, wait):
	wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='services-new__list']/a")))
	return driver.find_element_by_xpath('//a[@data-id="images"]')
	
def switch_active_window_check_url(driver, wait):
	driver.switch_to.window(driver.window_handles[-1])
	assert 'https://yandex.ru/images/?utm_source=main_stripe_big' in driver.current_url
	wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0 ImagesList-Item"]')))
	return driver.find_element_by_xpath('//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0 ImagesList-Item"]/a')
	
def img_link(driver, wait):
	wait.until(EC.presence_of_element_located((By.XPATH,'//a[@class="serp-item__link"]')))
	return driver.find_element_by_xpath('//a[@class="serp-item__link"]')
	
def active_nav_buttons_forvard(driver, wait):
	imagesrc = driver.find_elements_by_xpath('//img[@class="MMImage-Origin"]')
	for image in imagesrc:
		image = image
	actions = ActionChains(driver)
	actions.move_to_element(image)
	actions.perform()
	return wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="CircleButton CircleButton_type_next CircleButton_type MediaViewer-Button MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonNext MediaViewer_theme_fiji-ButtonNext"]/i')))
	
def active_nav_buttons_back(driver, wait):
	imagesrc = driver.find_elements_by_xpath('//img[@class="MMImage-Origin"]')
	for image in imagesrc:
		image = image
	actions = ActionChains(driver)
	actions.move_to_element(image)
	actions.perform()
	return wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="CircleButton CircleButton_type_prev CircleButton_type MediaViewer-Button MediaViewer_theme_fiji-Button MediaViewer-ButtonPrev MediaViewer_theme_fiji-ButtonPrev"]/i')))
	

def get_img_src(driver):
	imagesrc = driver.find_elements_by_xpath('//img[@class="MMImage-Origin"]')
	for image in imagesrc:
		img_src = image.get_attribute("src")
	return img_src