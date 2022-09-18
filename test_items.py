from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button(browser):
    browser.get(link)
    text_button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert text_button, 'Card button not find'

