from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Config.config import TestData
from selenium.webdriver.common.by import By
import time

class AssetsPage(BasePage):
    ASSETS_PAGE_MAIN_LINK=(By.XPATH,"/html/body/div[1]/div[1]/ul/li[2]/a")
    ASSETS_PAGE_MAIN_CHECKBOX=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/a")
    ASSETS_CHECKBOX_COPY_ITEMSNUMBER="Copy To(10)"
    ASSETS_SEARCH_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/input")
    ASSETS_SEARCH_INPUT_ITEM_DELETE = 'testdelete'
    ASSETS_SEARCH_INPUT_SEARCH = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/a[1]/i")
    ASSETS_MAIN_DELETE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/a/i")
    ASSETS_DELETE_FILES_FOREVER = (By.XPATH,"/html/body/div[11]/div/div/div/div[2]/div[2]/a")
    ASSETS_COPY_TO_BUG = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/a")
    ASSETS_COPY_TO_GALLERY_BUG = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div/ul/li[1]/a")
    YES_COPY_THE_FILES_BUG = (By.XPATH,"/html/body/div[11]/div/div/div/div[3]/div[2]/a")
    ASSETS_GO_GALLERY_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[1]/ul/li[1]/a")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def check_items_in_assets(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.ASSETS_PAGE_MAIN_CHECKBOX)
    def delete_item_from_assets(self, name):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_SEARCH_INPUT,name)
        time.sleep(2)
        self.do_click(self.ASSETS_SEARCH_INPUT_SEARCH)
        time.sleep(5)
        self.do_click(self.ASSETS_PAGE_MAIN_CHECKBOX)
        time.sleep(2)
        self.do_click(self.ASSETS_MAIN_DELETE_BUTTON)
        time.sleep(2)
        self.do_click(self.ASSETS_DELETE_FILES_FOREVER)
        time.sleep(3)
        self.do_click(self.ASSETS_COPY_TO_BUG)
        self.do_click(self.ASSETS_COPY_TO_GALLERY_BUG)
        self.do_click(self.YES_COPY_THE_FILES_BUG)
        time.sleep(5)
        self.do_click(self.ASSETS_GO_GALLERY_MAIN_LINK)










