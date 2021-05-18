import time

import pytest
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Pages.GalleriesPage import GalleriesPage
from Pages.AssetsPage import AssetsPage
from selenium.webdriver.common.by import By
import pyautogui

class LoginPages(BasePage):
    UPLOAD_FILE_PATH = "C:\\Users\\User\\Downloads\\sample4.wma"
    ADD_FILES_FROM_ASSETS_TITLE = "sample4.wma"
    ADD_FILES_FROM_ASSETS_CHECKBOX1 = (By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[15]/div[1]/div[1]/label/i")
    ADD_FILES_FROM_ASSETS_CHECKBOX2 = (By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[15]/div[2]/div[1]/label/i")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def login(self):
        self.driver.find_element(By.LINK_TEXT, LoginPage.GO_TO_LOGIN).click()
        self.do_send_keys(LoginPage.EMAIL, TestData.USER_NAME)
        self.do_send_keys(LoginPage.PASSWORD, TestData.PASSWORD)
        time.sleep(2)
        self.do_click(LoginPage.LOGIN_BUTTON)
    def upload_files_to_assets(self,file_path):
        self.main_page=GalleriesPage(self.driver)
        self.main_page.upload_files_main_link(file_path)
    def create_first_gallery_video_academy(self,title):
        self.mainPage = GalleriesPage(self.driver)
        self.mainPage.do_click(GalleriesPage.MAIN_GALLERY_LINK)
        self.mainPage.do_click(GalleriesPage.CREATE_YOUR_FIRST_GALLERY_LINK)
        self.mainPage.do_hover(GalleriesPage.VIDEO_ACADEMY_TEMPLATE_HOVER)
        self.mainPage.do_click(GalleriesPage.VAT_USE_THIS_GALLERY)
        self.mainPage.do_click(GalleriesPage.CREATE_GALLERY_SAVE_AND_NEXT)
        self.mainPage.do_click(GalleriesPage.GALLERY_ITEMS_FOLDER_ADD_FILES_FROM_ASSETS)
        self.do_send_keys(GalleriesPage.GALLERY_ITEMS_FOLDER_AFFA_SEARCH_INPUT, title)
        self.do_click(GalleriesPage.GALLERY_ITEMS_FOLDER_AFFA_SEARCH_ICON)
        time.sleep(2)
        self.do_click(self.ADD_FILES_FROM_ASSETS_CHECKBOX1)
        self.do_click(self.ADD_FILES_FROM_ASSETS_CHECKBOX2)







    


