import time

import pytest

from pageObjects.UserForm_Updation import profileUpdation
from pageObjects.User_Info import user_information
from utilities.CustomLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_001_UserForm:
    def test_fillData(self):
        self.profile = profileUpdation(self.driver)
        logger = LogGen.loggen()
        #self.profile.Figure2()
        logger.info("**********Test Started***********")
        self.input_Image = self.profile.Figure7()
        self.input_Email =self.profile.email("sujith@yopmail.com")
        self.input_Name = self.profile.name("sujith")
        time.sleep(3)
        self.input_DOB = self.profile.Dob()
        self.input_Website = self.profile.pagelink("www.github.com")
        self.checkbox_showNotifications = self.profile.ShowNotification()
        time.sleep(3)
        self.checkbox_DarkTheme = self.profile.darktheme()
        self.input_Bio = self.profile.Bio("Biodata is an abbreviation for the term biographical data. ... ")
        time.sleep(5)
    #def test_showData(self):
        self.Updated_Profile = user_information(self.driver)
        self.info_data_profileImage = self.Updated_Profile.profile()
        self.info_data_bio = self.Updated_Profile.bio()
        self.info_data_name = self.Updated_Profile.name()
        self.info_data_darkTheme = self.Updated_Profile.DarkTheme()
        self.info_data_email = self.Updated_Profile.Email()
        self.info_data_website=self.Updated_Profile.viewPage()
        self.info_data_showNotifications=self.Updated_Profile.ShowNotification()
        self.info_data_Dob = self.Updated_Profile.dob()
        print("Current Page Title after Back:"+ self.driver.title)

        #time.sleep(3)
    #def test_execution(self):
        #print("test002")
        if self.input_Name==self.info_data_name:
            logger.info("********Name were Displayed Successfully*******")
            assert True
        else:
             print("False")
             assert False
        if self.input_Image==self.info_data_profileImage:
            logger.info("********Image were Displayed Successfully*******")
            assert True
        else:
             print("False")
             assert False
        if self.checkbox_showNotifications == self.info_data_showNotifications:
            logger.info("********Show Notifications were Deselected Successfully*******")
            assert True
        else:
            print("False")
            assert False
        if self.checkbox_DarkTheme==self.info_data_darkTheme:
            logger.info("********DarkTheme were Selected Successfully*******")
            assert True
        else:
            print("False")
            assert False
        if self.input_Email==self.info_data_email:
            logger.info("********Email were Displayed Successfully*******")
            assert True
        else:
            print("False")
            assert False
        if self.input_Bio==self.info_data_bio:
            logger.info("******** Bio were Displayed Successfully *******")
            assert True
        else:
            print("False")
            assert False
        if self.input_DOB==self.info_data_Dob:
            logger.info("******* DOB were Displayed Successfully *******")
            assert True
        else:
            print("False")
            assert False
        logger.info("**********TestCases Passed**********")
        logger.info("**********Test Ended**********")








