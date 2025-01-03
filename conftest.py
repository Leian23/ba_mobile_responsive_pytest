import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def setup(request, URL):
    driver = webdriver.Chrome()
    driver.get(URL)  
    request.session.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def URL():
    return "https://game-one-customizer-stg.qstrike.net/"

@pytest.fixture(scope="class", autouse=True)
def setup_class(request, setup, URL):
    request.cls.driver = setup
    request.cls.url_name = URL
