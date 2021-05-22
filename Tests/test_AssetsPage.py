import pytest
from Pages.LoginPage import LoginPage
from Pages.MainPage import LoginPages
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Pages.AssetsPage import AssetsPage
from selenium.webdriver.common.by import By
import time

class Test_Assets(BaseTest):
    def test_check_items_in_assets(self):
        self.assets_page = LoginPages(self.driver)
        self.assets_page.login()
        time.sleep(2)
    # def test_check_items_in_assets_check_items(self):
    #     #Check if number of assets in Copy To/Delete is the same as number of assets with checkboxes
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.check_items_in_assets()
    #     assets_copy_to_parent_div_id = self.driver.find_element(By.ID,"copyTo")
    #     assets_copy_to_text = assets_copy_to_parent_div_id.text
    #     print(assets_copy_to_text)
    #     assets_checkbox_class = self.driver.find_elements(By.CLASS_NAME,"selected")
    #     assets_checkbox_length = len(assets_checkbox_class)
    #     print(assets_checkbox_length)
    #     if assets_copy_to_text == "Copy To("+str(assets_checkbox_length)+")":
    #         print("*************The Copy to number of items is the same as actual number of items*****************")
    #     else:
    #         print("Something went wrong.")
    # def test_upload_file_to_assets_folder(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.upload_file_to_assets_folder(self.assets_page.ASSETS_UPLOAD_FILE_PATH)
    #     i_text_all = self.driver.find_elements(By.CLASS_NAME, "caption")
    #     for text in i_text_all:
    #         print (text.text)
    #         if text.text == "New Added Asset":
    #             print("**************Element is present in screen*****************")
    #
    # def test_delete_item_from_assets(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.delete_item_from_assets(self.assets_page.ASSETS_SEARCH_INPUT_ITEM_DELETE)
    #     i_text_all = self.driver.find_elements(By.CLASS_NAME, "caption")
    #     for text in i_text_all:
    #         print(text.text)
    #         if text.text == "New Added Asset":
    #             print("Element is present in screen")
    #         else:
    #             print("**************Element is deleted*************")
    def test_view_assets_info(self):
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.view_assets_info()
    # def test_share_asset(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.share_asset()
    # def test_set_thumbnail_image(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.set_thumbnail_image_reset(self.assets_page.ASSETS_SET_THUMBNAIL_IMAGE_FILE_PATH)
    # def test_set_thumbnail_video(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.set_thumbnail_video()
    # def test_asset_trimming(self):
    #     self.assets_page = AssetsPage(self.driver)
    #     self.assets_page.asset_trimming()