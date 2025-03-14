import pytest
import logging
import os
from selenium import webdriver

@pytest.fixture
def driver():
 #Fixture  WebDriver hamar. bacuma Chrome u paguma testic heto
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
# Save anum screnshotery testeri yngneluc u save anum logerum
    outcome = yield
    report = outcome.get_result()
    logger = logging.getLogger(__name__)

    if report.failed:
        driver = item.funcargs.get("driver", None)  # fixturic stanum enq WebDriver
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)  #sarqum enq papka screnshoti ete bacakayuma
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")

            driver.save_screenshot(screenshot_path)  # Screnshota anum
            logger.error(f"📸 Screenshot save: {screenshot_path}")


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
 # LOgeri kargavorumnery pytesti hamar
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  #Logeri papki stextsum ete papka chka
    log_file = os.path.join(log_dir, "test.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode='w'),
            logging.StreamHandler()  # logery cuca talis terminalum
        ]
    )
