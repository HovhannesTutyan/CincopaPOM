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
    def test_create_photon_wizard(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.create_photon_wizard()
        PRODUCT_NAME_CSS_SELECTOR = self.driver.find_element(By.CSS_SELECTOR,".cp-template-name.name")
        if PRODUCT_NAME_CSS_SELECTOR.text == "Product: Photon Video Player":
            print("******************The Photon gallery is successfully created!********************")
        else:
            print("------------------The gallery creation failed.-----------------------------------")
    def test_change_player_color(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.create_photon_wizard()
        self.photon_wizard.change_player_color()
        print("***********Player color was changed******************")
    def test_enable_video_chapters(self):                 ##here chapters must be turned on
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.enable_video_chapters()
        chapters_list = self.driver.find_element(By.CSS_SELECTOR, ".mejs-chapters-list")
        if chapters_list:
            print("************Chapters are enabled,and chapters text is************", chapters_list.text)
        else:
            print("-------Chapters are disabled, no text is available.----------")
    def test_disable_video_chapters(self):
        from selenium.common.exceptions import NoSuchElementException
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.disable_video_chapters()
        try:
            chapters_list = self.driver.find_element(By.CSS_SELECTOR, ".mejs-chapters-list")
            if chapters_list:
                print("---------Chapter Elements are still present----------")
        except NoSuchElementException:
            print("**********Chapter elements are successfully deleted***********")

    def test_video_popup(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.video_popup()
        if self.photon_wizard.VIDEO_THUMBNAIL_OPEN_VIDEO:
            print("*******Video popup was added***********")
        else:
            print("------------The popup was not added------------")
    def test_text_popup(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.text_popup()
        if self.photon_wizard.VIDEO_THUMBNAIL_OPEN_TEXT:
            print("*******Text popup was added***********")
        else:
            print("------------Text popup was not added------------")
    def test_video_autoplay(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.video_autoplay()
        play = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-playpause-button.mejs-pause")
        mute = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-volume-button.mejs-unmute")
        if play and mute:
            print("********The mute autoplay was added*********")
        else:
            print("--------The video mute autoplay is not added--------")
    def test_video_autoplay_with_sound(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.video_autoplay_with_sound()
        play = self.driver.find_element(By.CSS_SELECTOR, ".mejs-button.mejs-playpause-button.mejs-pause")
        unmute = self.driver.find_element(By.CSS_SELECTOR, ".mejs-button.mejs-volume-button.mejs-mute")
        if play and unmute:
            print("********The unmute autoplay was added*********")
        else:
            print("--------The video unmute autoplay is not added--------")

    def test_play_video_loop_mode(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.play_video_loop_mode()
        repeat = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-loop-button.mejs-loop-on")
        if repeat:
            print("************The loop mode was added**********")
        else:
            print("----------The loop mode was not added----------")

    def test_lead_gen_after_first_video(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.lead_gen_after_first_video()
        time.sleep(2)
        play_center = self.driver.find_element(By.CSS_SELECTOR,".mejs-overlay-button")
        play_center.click()
        time.sleep(2)
        print(pyautogui.position())
        pyautogui.click(1741,846)
        time.sleep(3)
        pyautogui.click(1741,846)
        time.sleep(8)
        personal_details = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[6]/div/div/div")
        if personal_details:
            print("********The lead gen form after the video was added**********")
        else:
            print("----------The lead gen form after the video was added-----------")

    def test_lead_gen_before_first_video(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.lead_gen_before_first_video()
        time.sleep(5)
        personal_details = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[6]/div/div/div")
        if personal_details:
            print("********The lead gen form before the video was added**********")
        else:
            print("----------The lead gen form before the video was added-----------")
    def test_password_protection(self):
        self.photon_wizard = PhotonWizard(self.driver)
        self.photon_wizard.password_protection()
        try:
            password_container = self.driver.find_element(By.CSS_SELECTOR,".ze_password_promt_container_inner")
            if password_container:
                print("********Password Protection is Added************")
        except:
            print("-------Password Protection was  not added-----------")
        password_text = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[1]/h1").text
        if password_text == "higklmnop":
            print("**********The password text matches with the input**********")
        else:
            print("--------The password text does not match with the input--------")
        time.sleep(2)
        self.photon_wizard.do_send_keys(self.photon_wizard.IFRAME_PASSWORD_INPUT,"abcdefg")
        time.sleep(2)
        self.photon_wizard.do_click(self.photon_wizard.IFRAME_PASSWORD_INPUT_CONTINUE)
        time.sleep(2)
        try:
            play_middle_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[4]/div")
            if play_middle_button:
                print("*******The video is playing after input the right password*******")
        except:
                print("---------The video is not opened when correct password is inputed-------------")


