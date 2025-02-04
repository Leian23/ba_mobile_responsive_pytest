from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    #click person icon
    person_icon = (By.XPATH, "//*[@class='qx-login']")
    #Fill in textboxes
    user_name = (By.XPATH, "//*[@id='login-dropdown']/form/div[1]/div/input")
    password = (By.XPATH, "//*[@id='login-dropdown']/form/div[2]/div/div/input")
    #Submit button
    submit_btn = (By.XPATH, "//*[@id='login-dropdown']/form/div[3]/button")
    #Click Hamburger Menu
    ham_menu = (By.XPATH, "//*[@id='qx-header']/div[1]/div[2]/a")
    #Click Customizer
    customizer = (By.XPATH, "//*[@id='mobile-sidebar-navigation']/div/div/ul/li[1]/a")


    #Reusable methods for getting the data

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def wait_driver(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_click_driver(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_invisibility(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.invisibility_of_element_located(locator))

    def wait_visibility(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_elements(self, locator):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.presence_of_all_elements_located(locator))
    


    def get_icon(self):
        return self.driver.find_element(*BasePage.person_icon)
    def get_username(self):
        return self.driver.find_element(*BasePage.user_name)
    def get_password(self):
        return self.driver.find_element(*BasePage.password)
    def get_submit(self):
        return self.driver.find_element(*BasePage.submit_btn)
    def get_hamburger_menu(self):
        return self.driver.find_element(*BasePage.ham_menu)
    def get_customizer(self):
        return self.driver.find_element(*BasePage.customizer)
    
    
    
    


    