import pytest
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

class Test_Photon_Wizard(BaseTest):
    def test_login(self):
        self.photon_wizard = LoginPages(self.driver)
        self.photon_wizard.login()
    # def test_create_photon_wizard(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.create_photon_wizard()
    #     PRODUCT_NAME_CSS_SELECTOR = self.driver.find_element(By.CSS_SELECTOR,".cp-template-name.name")
    #     if PRODUCT_NAME_CSS_SELECTOR.text == "Product: Photon Video Player":
    #         print("******************The Photon gallery is successfully created!********************")
    #     else:
    #         print("------------------The gallery creation failed.-----------------------------------")
    # def test_change_player_color(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.create_photon_wizard()
    #     self.photon_wizard.change_player_color()
    # def test_enable_video_chapters(self):                 ##here chapters must be turned on
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.enable_video_chapters()
    #     chapters_list = self.driver.find_element(By.CSS_SELECTOR, ".mejs-chapters-list")
    #     if chapters_list:
    #         print("Chapters are enabled,and chapters text is", chapters_list.text)
    #     else:
    #         print("Chapters are disabled, no text is available.")
    # def test_disable_video_chapters(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.disable_video_chapters()
    #     print("************All chapters are disabled.****************")
    # def test_video_popup(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.video_popup()
    #     if self.photon_wizard.VIDEO_THUMBNAIL_OPEN_VIDEO:
    #         print("*******Video popup was added***********")
    #     else:
    #         print("------------The popup was not added------------")
    # def test_text_popup(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.text_popup()
    #     if self.photon_wizard.VIDEO_THUMBNAIL_OPEN_TEXT:
    #         print("***********The text was added***********")
    #     else:
    #         print("---------The popup was not added-----------")
    # def test_video_autoplay(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.video_autoplay()
    #     print("********The mute autoplay was added*********")
    # def test_video_autoplay_with_sound(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.video_autoplay_with_sound()
    #     print("**********Video Autoplay With Sound Was Added***********")
    # def test_video_autoplay_scroll_view(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.video_autoplay_scroll_view()
    #     print("**********Video Autoplay With Scroll to View Was Added***********")

    # def test_lead_gen_after_first_video(self):
    #     self.photon_wizard = PhotonWizard(self.driver)
    #     self.photon_wizard.lead_gen_after_first_video()
    #     time.sleep(2)
    #     new_page = self.driver.window_handles[1]
    #     self.driver.switch_to.window(new_page)
    #     time.sleep(5)
    #     print(pyautogui.position())
    #     pyautogui.click(1581,970)
    #     time.sleep(3)
    #     pyautogui.click(1581,970)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[4]/div").click()
    #     time.sleep(10)
    #     first_name_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[6]/div/div/div/div[1]/input")
    #     if first_name_input:
    #         print("********The lead gen form after the video was added**********")
    #     else:
    #         print("----------The lead gen form after the video was added-----------")
    def test_lead_gen_before_first_video(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.lead_gen_before_first_video()
        time.sleep(2)
        new_page = self.driver.window_handles[2]
        time.sleep(5)
        self.driver.switch_to.window(new_page)
        time.sleep(5)
        first_name_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[6]/div/div/div/div[1]/input")
        if first_name_input:
            print("********The lead gen form before the video was added**********")
        else:
            print("----------The lead gen form after the video was added-----------")


