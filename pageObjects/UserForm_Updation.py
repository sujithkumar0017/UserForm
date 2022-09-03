import time

from selenium.webdriver.common.by import By


class profileUpdation:
    img_figure1_Xpath = "//figure[1]//img[1]"
    img_figure2_Xpath = "//figure[2]//img[1]"
    img_figure3_Xpath = "//figure[3]//img[1]"
    img_figure4_Xpath = "//figure[4]//img[1]"
    img_figure5_Xpath = "//figure[5]//img[1]"
    img_figure6_Xpath = "//figure[6]//img[1]"
    img_figure7_Xpath = "//figure[7]//img[1]"
    input_name_Xpath = "//input[@placeholder='Your name']"
    input_email_Xpath ="//input[@placeholder='Email address']"
    input_password_Xpath = "//input[@placeholder='password']"
    input_confirm_password_Xpath = "//input[@placeholder='password confirmation']"
    input_location_Xpath = "//input[@placeholder='Location']"
    input_DOB_Xpath = "//input[@placeholder='Date of birth']"
    input_phone_Xpath = '//input[@placeholder="Phone number"]'
    input_pagelink_Xpath = '//input[@placeholder="Link to your page / profile"]'
    checkbox_ShowNotifications_Id = "settings-index-0"
    checkbox_Darktheme_Xpath = '(//input[@class="form-check-input"])[2]'
    checkbox_AdBlocks_linktext = "Ad-Blocks"
    checkbox_EmailUpdates_linktext = "Email updates"
    textbox_Bio_Xpath = "//textarea[@class='form-control form-control-lg']"


    def __init__(self,driver):
        self.driver = driver
    def Figure1(self):
        self.driver.find_element(By.XPATH,self.img_figure1_Xpath).click()
    def Figure2(self):
        self.driver.find_element(By.XPATH,self.img_figure2_Xpath).click()
    def Figure3(self):
        self.driver.find_element(By.XPATH,self.img_figure3_Xpath).click()
    def Figure4(self):
        self.driver.find_element(By.XPATH,self.img_figure4_Xpath).click()
    def Figure5(self):
        self.driver.find_element(By.XPATH,self.img_figure5_Xpath).click()
    def Figure6(self):
        self.driver.find_element(By.XPATH,self.img_figure6_Xpath).click()
    def Figure7(self):
        self.driver.find_element(By.XPATH,self.img_figure7_Xpath).click()
    def name(self,name):
        self.driver.find_element(By.XPATH, self.input_name_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_name_Xpath).send_keys(name)
    def email(self,email):
        self.driver.find_element(By.XPATH, self.input_email_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_email_Xpath).send_keys(email)
    def password(self,password):
        self.driver.find_element(By.XPATH, self.input_password_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_password_Xpath).send_keys(password)
    def confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH, self.input_confirm_password_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_confirm_password_Xpath).send_keys(confirm_password)
    def location(self,location):
        self.driver.find_element(By.XPATH, self.input_location_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_location_Xpath).send_keys(location)
    def Dob(self):
        self.driver.find_element(By.XPATH, self.input_DOB_Xpath).clear()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Date of birth']").click()
        calendar = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/form/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]').text
        time.sleep(3)
        print(calendar)
        month = "March 2000"
        while calendar != month:
                #print(calendar)
                self.driver.find_element(By.XPATH, "//button[normalize-space()='Next Month']").click()
                calendar = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/form/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]').text
        time.sleep(2)
        date = self.driver.find_element(By.XPATH, "//div[@aria-label='day-9']").click()
        time.sleep(5)
    def phone(self,phone):
        self.driver.find_element(By.XPATH, self.input_phone_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_phone_Xpath).send_keys(phone)
    def pagelink(self,pagelink):
        self.driver.find_element(By.XPATH, self.input_pagelink_Xpath).clear()
        self.driver.find_element(By.XPATH,self.input_pagelink_Xpath).send_keys(pagelink)
    def ShowNotification(self):
        self.driver.find_element(By.ID,self.checkbox_ShowNotifications_Id).click()
    def darktheme(self):
        self.driver.find_element(By.XPATH, self.checkbox_Darktheme_Xpath).click()
    def ad_blocks(self):
        self.driver.find_element(By.LINK_TEXT, self.checkbox_AdBlocks_linktext).click()
    def EmailUpdates(self):
        self.driver.find_element(By.LINK_TEXT,self.checkbox_EmailUpdates_linktext).click()
    def Bio(self,Bio):
        self.driver.find_element(By.XPATH, self.textbox_Bio_Xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Bio_Xpath).send_keys(Bio)

