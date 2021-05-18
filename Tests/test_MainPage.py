import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Pages.MainPage import LoginPages
from Pages.AssetsPage import AssetsPage
from selenium.webdriver.common.by import By
import time

class Test_LoginPages(BaseTest):
    def test_login(self):
        self.main_page=LoginPages(self.driver)
        self.main_page.login()
    # def test_upload_files_to_assets(self):
    #     self.main_page=LoginPages(self.driver)
    #     self.main_page.upload_files_to_assets(self.main_page.UPLOAD_FILE_PATH)
    #     time.sleep(35)
    #     self.main_page.upload_files_to_assets(self.main_page.UPLOAD_FILE_PATH)
    #     time.sleep(35)
    #     # self.main_page.upload_files_to_assets(self.main_page.UPLOAD_FILE_PATH)
    #     # time.sleep(35)
    #     # self.main_page.upload_files_to_assets(self.main_page.UPLOAD_FILE_PATH)
    #     # time.sleep(35)
    #     time.sleep(2)
    #     self.sec_page=AssetsPage(self.driver)
    #     time.sleep(2)
    #     self.sec_page.check_items_in_assets()
    #     assets_count=self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/a/label")
    #     assets_count_text=assets_count.text()
    #     assert assets_count_text == self.sec_page.ASSETS_CHECKBOX_COPY_ITEMSNUMBER
    # def test_create_first_gallery_video_academy(self):
    #     self.mainPage = LoginPages(self.driver)
    #     self.mainPage.create_first_gallery_video_academy(self.mainPage.ADD_FILES_FROM_ASSETS_TITLE)
    def test_create_gallery_main_link(self):
        self.mainPage = LoginPages(self.driver)
        self.mainPage.create_gallery_main_link(self.mainPage.ADD_FILES_FROM_ASSETS_TITLE)









