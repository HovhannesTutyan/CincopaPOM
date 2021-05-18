import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Pages.AssetsPage import AssetsPage

import time
class Test_Galleries(BaseTest):
    def test_gallery_search(self):
        self.gallery_page=GalleriesPage(self.driver)
        self.gallery_page.gallery_search(TestData.GALLERIES_SEARCH_TEXT_TEST)
        assert TestData.GALLERIES_SEARCH_TEXT_TEST == TestData.GALLERIES_SEARCH_TEXT_BASE
    # def test_gallery_settings(self):
    #     self.gallery_page=GalleriesPage(self.driver)
    #     self.gallery_page.gallery_settings(GalleriesPage.GALLERY_PREVIEW)
    #     title = self.gallery_page.get_title(TestData.CUSTOMIZE_GALLERY_TITLE)
    #     assert title == TestData.CUSTOMIZE_GALLERY_TITLE
    # def test_gallery_manage_upload_files(self):
    #     self.gallery_page=GalleriesPage(self.driver)
    #     self.gallery_page.gallery_manage_upload_files(GalleriesPage.GALLERY_MANAGE_UPLOAD_FILES_LINK)
    #     title = self.gallery_page.get_title(TestData.MANAGE_UPLOAD_FILES_TITLE)
    #     assert title == TestData.MANAGE_UPLOAD_FILES_TITLE
    # def test_gallery_embed_gallery(self):
    #     self.gallery_page=GalleriesPage(self.driver)
    #     self.gallery_page.gallery_embed_gallery(GalleriesPage.GALLERY_EMBED_GALLERY_LINK)
    #     title = self.gallery_page.get_title(TestData.EMBED_GALLERY_TITLE)
    #     assert title == TestData.EMBED_GALLERY_TITLE
    #
    # def test_edit_gallery_title1(self):
    #     self.gallery_page=GalleriesPage(self.driver)
    #     self.gallery_page.edit_gallery_title(TestData.EDIT_GALLERY_TITLE_TEXT1)
    #     time.sleep(3)
    #     inputText=self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/span/span[2]")
    #     inputText_text=inputText.text
    #     assert inputText_text == TestData.EDIT_GALLERY_TITLE_TEXT1
    #
    # def test_add_new_tag_gallery(self):
    #     self.gallery_page=GalleriesPage(self.driver)
    #     self.gallery_page.add_new_tag_gallery(TestData.GALLERY_TAG_NAME)
    #     inputText=self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[7]/div[1]/div/span[2]/span")
    #     inputText_text=inputText.text
    #     assert inputText_text == TestData.GALLERY_TAG_NAME_TEST

    # def test_add_files_gallery(self):
    #     self.gallery_page = GalleriesPage(self.driver)
    #     self.gallery_page.add_files_assets_gallery(TestData.ADD_GALLERY_FROM_ASSETS_NAME1)

    def test_upload_file_gallery(self):
        self.gallery_page=GalleriesPage(self.driver)
        self.gallery_page.upload_file_gallery(GalleriesPage.FILE_UPLOAD_FOLDER_PATH)
