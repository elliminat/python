import pytest
import page
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("chromedriver.exe", options=options)    
wait = WebDriverWait(driver, 10)

findsrt = 'совкомбанк'
siteurl = 'sovcombank.ru'

def test_search():
    page.go_to_yandex(driver)
    search_field = page.enter_to_search_field(driver, wait, findsrt)
    page.enter_and_check_suggest(driver, wait, findsrt)
    page.click_enter(search_field)
    assert page.check_url(driver, wait, siteurl) #проверка на то что в результатах есть ссылка на сайт банка
     

def test_img():
    page.go_to_yandex(driver)
    link = page.search_img_link(driver, wait)
    page.click_element(link)
    category = page.switch_active_window_check_url(driver, wait)
    page.click_element(category)
    image = page.img_link(driver, wait)
    page.click_element(image)
    button_next = page.active_nav_buttons_forvard(driver, wait)
    img_src_first = page.get_img_src(driver)
    page.click_element(button_next)
    img_src_second = page.get_img_src(driver)
    assert img_src_first != img_src_second #проверка ссылок на первое изображение и изображение после нажатия на кнопку смены изображений
    button_back = page.active_nav_buttons_back(driver, wait)
    page.click_element(button_back)
    img_src_second = page.get_img_src(driver)
    assert img_src_first == img_src_second #проверка ссылок на первое изображение до и после смены изображений
    driver.quit()
