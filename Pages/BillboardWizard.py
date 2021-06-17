from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.GalleriesPage import GalleriesPage
from selenium.webdriver.common.by import By
import time
import pyautogui

class BillboardWizard(BasePage):
    GALLERY_PAGE_MAIN_LINK = (By.XPATH, "/html/body/div[1]/div[1]/ul/li[1]")
    BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]/a[1]/i")
    BASIC_SETTINGS = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[1]/div[1]/a")
    GALLERY_TITLE = (By.ID,"_foldername")
    GALLERY_DESCRIPTION = (By.ID,"_folderdescription")
    AUTOCONTINUE = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[1]/div[2]/div[3]/div/div/div[3]/div/div/label")
    MAIN_SAVE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[1]/div[3]/button[2]")
    ADVANCED_SETTINGS = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[1]/a")
    TEXT_ALIGN = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[3]/div/div/div/a")
    TEXT_ALIGN_LEFT = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[3]/div/div/ul/li[2]/a")
    TEXT_ALIGN_LEFT_STYLE = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]/h2/span")
    TEXT_ALIGN_RIGHT = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[3]/div/div/ul/li[3]/a")
    ADD_TEXT_SELECTION = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[2]/div/div/div/a")
    TITLE_DESC_SELECTION = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[2]/div/div/ul/li[4]/a")
    SLIDESHOW_TOGGLE = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[4]/div/div/label")
    SLIDESHOW_TOGGLE_ON = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[4]/div/div/label")



    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def set_basic_settings(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.BASIC_SETTINGS)
        time.sleep(2)
        self.do_clear(self.GALLERY_TITLE)
        time.sleep(2)
        self.do_send_keys(self.GALLERY_TITLE,'LA COLERE DE SANCETRES')
        time.sleep(2)
        self.do_clear(self.GALLERY_DESCRIPTION)
        self.do_send_keys(self.GALLERY_DESCRIPTION, "LA COLERE DE SANCETRES and other files")
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_BUTTON)
        time.sleep(2)
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(3)
    def autocontinue(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.BASIC_SETTINGS)
        time.sleep(2)
        self.do_click(self.AUTOCONTINUE)
        time.sleep(2)
    def add_title_align_left(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.TEXT_ALIGN)
        time.sleep(2)
        self.do_click(self.TEXT_ALIGN_LEFT)
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)

    def add_title_align_right(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.TEXT_ALIGN)
        time.sleep(2)
        self.do_click(self.TEXT_ALIGN_RIGHT)
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
    def title_desc_left(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.ADD_TEXT_SELECTION)
        time.sleep(2)
        self.do_click(self.TITLE_DESC_SELECTION)
        time.sleep(2)
        self.do_click(self.TEXT_ALIGN)
        time.sleep(2)
        self.do_click(self.TEXT_ALIGN_LEFT)
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
    def slideshow_on_off(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.SLIDESHOW_TOGGLE)
        time.sleep(10)





















