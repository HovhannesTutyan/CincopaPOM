import pytest
from Pages.LoginPage import LoginPage
from Pages.MainPage import LoginPages
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Pages.AssetsPage import AssetsPage
import time

class Test_Assets(BaseTest):
    def test_check_items_in_assets(self):
        self.assets_page = LoginPages(self.driver)
        self.assets_page.login()
        time.sleep(2)
        # self.assets_page = AssetsPage(self.driver)
        # self.assets_page.check_items_in_assets()
    def test_delete_item_from_assets(self): # test with bug
        self.assets_page = AssetsPage(self.driver)
        self.assets_page.delete_item_from_assets(self.assets_page.ASSETS_SEARCH_INPUT_ITEM_DELETE)

