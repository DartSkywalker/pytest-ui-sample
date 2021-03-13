from selenium.webdriver.common.by import By

SIGN_IN_URL = "https://eos.com/crop-monitoring/login/auth"

EMAIL_AUTH = (By.CSS_SELECTOR, 'input#email')

PASS_AUTH = (By.CSS_SELECTOR, 'input#password')

SIGN_IN_BTN = (By.CSS_SELECTOR, "button[data-id='sign-in-btn']")
