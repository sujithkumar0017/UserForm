import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://prasanna-narayanan24.github.io/user-form-updation-react/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()


