import logging
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from outlook_calendar_sync.utils import find_event, get_event

log = logging.getLogger(__name__)


def outlook_login(
    driver,
    username: str,
    password: str,
    calendar_uri: str,
    auth_code=None,
    requires_auth=True,
):
    password = password.strip()
    driver.get(calendar_uri)

    driver.implicitly_wait(10)

    log.debug("Started outlook login")
    username_field = driver.find_element(By.XPATH, r'//*[@id="i0116"]')
    signin_btn = driver.find_element(By.XPATH, r'//*[@id="idSIButton9"]')

    username_field.send_keys(username)
    signin_btn.click()

    log.debug("Submitted username %s", username)
    password_field = driver.find_element(By.XPATH, r'//*[@id="passwordInput"]')
    signin_btn_auth = driver.find_element(By.XPATH, r'//*[@id="submitButton"]')

    password_field.send_keys(password)
    signin_btn_auth.click()
    log.debug("Submitted password")

    if requires_auth:
        # Handle 2fa
        log.debug("Expecting 2fa authentication required")
        auth_code_field = driver.find_element(By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]')
        auth_code_submit = driver.find_element(By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]')

        auth_code = auth_code or input("Provide the authenticator code: ")

        log.debug("Using code '%s'", auth_code)
        auth_code_field.send_keys(auth_code)
        auth_code_submit.click()

    try:
        log.debug("Passed 'stay signed-in' prompt")
        stay_signed_in_btn = driver.find_element(By.ID, "idBtn_Back")
        stay_signed_in_btn.click()
    except NoSuchElementException:
        log.warning("No 'stay signed-in' dialogue presented. Continuing")
    finally:
        log.info("Completed outlook auth")
        return driver


def outlook_select_page_events(driver, days=1, delay=5):
    sleep(delay)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    log.debug("Collected page source for day 0")

    yield [get_event(i["aria-label"]) for i in soup.find_all(find_event)]

    for i in range(days - 1):
        next_page = driver.find_element(By.XPATH, '//*[@id="MainModule"]/div[3]/div/div[1]/div[1]/button[3]')
        next_page.click()
        sleep(delay)

        # Dump the page source into BS
        log.debug("Collected page source for day %d", i + 1)
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        yield [get_event(i["aria-label"]) for i in soup.find_all(find_event)]

        # Get the next page

    driver.quit()


def get_selenium_driver(debug=False):
    log.debug("Instantiating chrome selenium driver")
    chrome_opt = Options()
    if not debug:
        log.debug("Using --headless flag")
        chrome_opt.add_argument("--headless")
    driver_path = "executable_path=/usr/local/bin/chromedriver"
    log.debug("Using selenium driver from %s", driver_path)
    chrome_opt.add_argument(driver_path)
    return webdriver.Chrome(options=chrome_opt)
