import time

from selenium.webdriver.common.by import By


class user_information:
    img_profile_Xpath='//img[@src="/user-form-updation-react/static/media/man.6f2bab19.png"]'
    txt_name_cssSelectors = "div[class='user-heading'] h3"
    txt_location_Xpath = "//span[@class='help-block']"
    txt_dob_Xpath = '//*[@id="information"]/div[1]/span'
    txt_bio_CssSelectors = "div[id='information'] p"
    nav_settings_xpath = '//a[@href="#settings"]'
    nav_email_xpath = '//a[@href="#email"]'
    nav_events_xpath = '//a[@href="#events"]'
    Sb_DarkTheme_Xpath = "(//span[@class='text-dark glyphicon glyphicon-star'])[1]"
    txt_email_Xpath = "(//div[@class='d-block'])[2]"
    link_viewPage_LinkText = 'View page'
    Sb_ShowNotifications_Xpath = "(//span[@class='text-dark glyphicon glyphicon-star-empty'])[1]"

    def __init__(self,driver):
        self.driver = driver
    def profile(self):
        self.driver.find_element(By.XPATH,self.img_profile_Xpath)
    def name(self):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_name_cssSelectors)
    def location(self):
        self.driver.find_element(By.XPATH,self.txt_location_Xpath)
    def dob(self):
        self.driver.find_element(By.XPATH,self.txt_dob_Xpath)
    def bio(self):
        self.driver.find_element(By.CSS_SELECTOR,self.txt_bio_CssSelectors)
    def ShowNotification(self):
        self.driver.find_element(By.XPATH,self.nav_settings_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Sb_ShowNotifications_Xpath)
    def DarkTheme(self):
        self.driver.find_element(By.XPATH,self.nav_settings_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Sb_DarkTheme_Xpath)
    def Email(self):
        self.driver.find_element(By.XPATH,self.nav_email_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.txt_email_Xpath)
    def viewPage(self):
        self.driver.find_element(By.XPATH,self.nav_email_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT,self.link_viewPage_LinkText).click()
        time.sleep(5)
        self.driver.execute_script("window.history.go(-1)")