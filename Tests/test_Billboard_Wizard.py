import pytest
from Pages.BillboardWizard import BillboardWizard
from Pages.LoginPage import LoginPage
from Pages.PhotonWizard import PhotonWizard
from Pages.MainPage import LoginPages
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Pages.AssetsPage import AssetsPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pyautogui
import time

class Test_Billboard_Wizard(BaseTest):
    MAIN_PLAY_BUTTON = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[1]/div/div/div[2]/div[6]/div")
    MAIN_PLAY_BUTTON2 = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[1]/div/div/div[2]/div[4]/div")
    FORWARD_BUTTON = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[2]/li[2]/a")
    def test_login(self):
        self.billboard_wizard = LoginPages(self.driver)
        self.billboard_wizard.login()
    # def test_set_basic_settings(self):
    #     self.billboard_wizard = BillboardWizard(self.driver)
    #     self.billboard_wizard.set_basic_settings()
    #     bb_wizard_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/span/span[2]")
    #     bwname_text = bb_wizard_name.text
    #     if bwname_text == "LA COLERE DE SANCETRES":
    #         print("********The title is changed *********")
    #     bb_wizard_desc = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[3]")
    #     bb_wizard_desc_text = bb_wizard_desc.text
    #     if bb_wizard_desc_text == "LA COLERE DE SANCETRES and other files":
    #         print("******The description is changed ***********")
    # def test_autocontinue(self):
    #     self.billboard_wizard = BillboardWizard(self.driver)
    #     self.billboard_wizard.autocontinue()
    #     autocontinue_on = self.driver.find_element(By.CSS_SELECTOR,".itoggle.toggleOnOff.iTon")
    #     autocontinue_off = self.driver.find_element(By.CSS_SELECTOR,".itoggle.toggleOnOff.iToff")
    #     iframe = self.driver.find_element(By.ID, "simulator_content")
    #     self.driver.switch_to.frame(iframe)
    #     time.sleep(3)
    #     self.billboard_wizard.do_click(self.MAIN_PLAY_BUTTON)
    #     time.sleep(2)
    #     self.billboard_wizard.do_click(self.FORWARD_BUTTON)
    #     time.sleep(2)
    #     self.billboard_wizard.do_click(self.FORWARD_BUTTON)
    #     time.sleep(12)
    #     if autocontinue_off and self.MAIN_PLAY_BUTTON:
    #         print("*****autocontinue is off working***********")
    #     if autocontinue_on:
    #         self.billboard_wizard.do_click(self.MAIN_PLAY_BUTTON2)
    #         time.sleep(12)
    #         print("******autocontinue is on working**********")
    # def test_add_title_align_left(self):
    #     self.billboard_wizard = BillboardWizard(self.driver)
    #     self.billboard_wizard.add_title_align_left()
    #     left = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]")
    #     print(left.get_attribute("style"))
    #     if left.get_attribute("style") == "text-align: left; padding: 20px; overflow: hidden; box-sizing: border-box;":
    #         print("*******title is left aligned******")
    #     else:
    #         print("--------title left aligned failed-------")
    # def test_add_title_align_right(self):
    #     self.billboard_wizard = BillboardWizard(self.driver)
    #     self.billboard_wizard.add_title_align_right()
    #     right = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]")
    #     print(right.get_attribute("style"))
    #     if right.get_attribute("style") == "text-align: right; padding: 20px; overflow: hidden; box-sizing: border-box;":
    #         print("*******title is right aligned******")
    #     else:
    #         print("-------title right aligned failed-------")
    # def test_title_desc_left(self): #### verify that video title and description are left and right aligned, after sliding back and forward also
    #     self.billboard_wizard = BillboardWizard(self.driver)
    #     self.billboard_wizard.title_desc_left()
    #     textbox_title = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]/h2/span[1]")
    #     textbox_desc = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]/h2/span[2]")
    #     left = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]")
    #     if textbox_title and textbox_desc and left.get_attribute("style") == "text-align: left; padding: 20px; overflow: hidden; box-sizing: border-box;":
    #         print("*****title and description on first item are  left aligned*******")
    #     else:
    #         print("-------title and description left align failed----------")
    #     time.sleep(2)
    #     forward_arrow = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[2]/li[2]/a")
    #     self.billboard_wizard.do_click(forward_arrow)
    #     time.sleep(2)
    #     self.billboard_wizard.do_click(forward_arrow)
    #     time.sleep(2)
    #     textbox_title3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[3]/h2/span[1]")
    #     textbox_desc3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[3]/h2/span[2]")
    #     left3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[3]")
    #     if textbox_title3 and textbox_desc3 and left3.get_attribute("style") == "text-align: left; padding: 20px; overflow: hidden; box-sizing: border-box; height: 100px; opacity: 1;":
    #         print("*****title and description on third item are  left aligned*******")
    #     else:
    #         print("-------title and description  align failed on third item----------")
    def test_slideshow_on_off(self): #### verify that when slideshow is on/off video is being slided every 5 seconds
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.slideshow_on_off()
        toggle_on = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[4]/div/div/label")
        print(toggle_on.get_attribute("class")) #itoggle  toggleOnOff iTon
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        second_item_thumb = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[2]")
        print(second_item_thumb.get_attribute("class"))
        if toggle_on.get_attribute("class") == "itoggle  toggleOnOff iTon" and second_item_thumb.get_attribute("class") == "mediaObject video activatedPlugin flex-active-slide":
            print("******The slideshow is activated and second items classname is printed")
        else:
            print("-----slideshow activation failed--------")













