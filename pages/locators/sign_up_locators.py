from selenium.webdriver.common.by import By

SIGN_UP_URL = "https://eos.com/crop-monitoring/login"

FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#first_name")

LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#last_name")

EMAIL_INPUT = (By.CSS_SELECTOR, "input#email")

PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")

POLICY_CONFIRM_CHECKBX = (By.CSS_SELECTOR, "input#policy_confirm-input")

SIGN_UP_BTN = (By.CSS_SELECTOR, "button[data-id='sign-up-btn']")

CONFIRM_CODE = (By.CSS_SELECTOR, "input#confirm-code-input")
