import time

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from selenium.webdriver.common.by import By
import pyautogui

class GalleriesPage(BasePage):
    MAIN_GALLERY_LINK=(By.XPATH,"/html/body/div[1]/div[1]/ul/li[1]/a")
    CREATE_GALLERY_BUTTON=(By.XPATH,"//*[@id=\"container\"]/div[1]/div[2]/ul[3]/li/div")
    GALLERIES_SEARCH_INPUT=(By.XPATH,"//*[@id=\"libraryHead\"]/div[2]/div/input")
    GALLERIES_SEARCH_BUTTON=(By.XPATH,"//*[@id=\"libraryHead\"]/div[2]/div/a[1]/i")
    GALLERY_PREVIEW=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]/a[1]")
    GALLERY_MANAGE_UPLOAD_FILES_LINK=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]/a[2]")
    GALLERY_EMBED_GALLERY_LINK=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]/a[3]")

    EDIT_GALLERY_TITLE_PEN=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/span/span[2]")
    EDIT_GALLERY_INPUT=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[1]/form/input")
    EDIT_GALLERY_CONFIRM=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[1]/form/div/a[1]")
    EDIT_GALLERY_CANCEL=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[1]/form/div/a[2]")

    GALLERY_TITLE_SECTION=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]")
    GALLERY_ADD_NEW_TAG_LINK=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[7]/a")
    GALLERY_TAG_INPUT_LINK=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[7]/div[2]/div[1]/div/input")
    GALLERY_TAG_INPUT_CREATE_TAG=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[7]/div[2]/div[1]/div/p/span[2]")
    GALLERY_TAG_INPUT_APPLY=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[7]/div[2]/div[2]/a")

    GALLERY_ITEMS_FOLDER=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div[2]/i")
    GALLERY_ITEMS_FOLDER_ADD_FILES=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[1]/a[1]")
    GALLERY_ITEMS_FOLDER_ADD_FILES_FROM_ASSETS=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[2]/a")
    GALLERY_ITEMS_FOLDER_AFFA_SEARCH_INPUT=(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[13]/div/input")
    GALLERY_ITEMS_FOLDER_AFFA_SEARCH_ICON=(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[13]/div/a[1]/i")
    GALLERY_ITEMS_FOLDER_AFFA_CHECKBOX1=(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[15]/div/div[1]/label/i")
    GALLERY_ITEMS_FOLDER_AFFA_CHECKBOX2 = (By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[15]/div[6]/div[1]/label/i")
    GALLERY_ITEMS_FOLDER_AFFA_SEARCH_INPUT_CLOSE=(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[13]/div/a[2]/i")

    GALLERY_CHOOSE_FILES_BUTTON=(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[3]/div/div[1]/div/div/button")
    GALLERY_CHOOSE_FILES_BUTTON_MAIN=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[1]/div/div/button")
    FILE_UPLOAD_FOLDER_PATH=('CC:\\Users\\User\\Downloads\\180607_A_102.mp4')

    UPLOAD_FILES_GALLERY_MAIN_LINK=(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/a[1]")
    CREATE_YOUR_FIRST_GALLERY_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/div/p[2]/a")

    VIDEO_ACADEMY_TEMPLATE_HOVER = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/ul/li[8]/div")
    VAT_USE_THIS_GALLERY = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/ul/li[8]/div/div[2]/a")
    CREATE_GALLERY_SAVE_AND_NEXT = (By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/button[2]")





    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def gallery_search(self, title):
        self.driver.find_element(By.LINK_TEXT, LoginPage.GO_TO_LOGIN).click()
        self.do_send_keys(LoginPage.EMAIL, TestData.USER_NAME)
        self.do_send_keys(LoginPage.PASSWORD, TestData.PASSWORD)
        self.do_click(LoginPage.LOGIN_BUTTON)
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(self.GALLERIES_SEARCH_INPUT)
        self.do_send_keys(self.GALLERIES_SEARCH_INPUT, title)
        self.do_click(self.GALLERIES_SEARCH_BUTTON)


    def gallery_settings(self,gallery_locator):
        # self.do_send_keys(LoginPage.EMAIL,TestData.USER_NAME)
        # self.do_send_keys(LoginPage.PASSWORD,TestData.PASSWORD)
        # self.do_click(LoginPage.LOGIN_BUTTON)
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(gallery_locator)
    def gallery_manage_upload_files(self,gallery_locator):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(gallery_locator)
    def gallery_embed_gallery(self,gallery_locator):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(gallery_locator)

    def edit_gallery_title(self,title):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(self.EDIT_GALLERY_TITLE_PEN)
        self.do_clear(self.EDIT_GALLERY_INPUT)
        self.do_send_keys(self.EDIT_GALLERY_INPUT,title)
        self.do_click(self.EDIT_GALLERY_CONFIRM)

    def add_new_tag_gallery(self, title):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_hover(self.GALLERY_TITLE_SECTION)
        # time.sleep(3)
        self.do_click(self.GALLERY_ADD_NEW_TAG_LINK)
        # time.sleep(3)
        self.do_send_keys(self.GALLERY_TAG_INPUT_LINK,title)
        # time.sleep(3)
        self.do_click(self.GALLERY_TAG_INPUT_CREATE_TAG)
        self.do_click(self.GALLERY_TAG_INPUT_APPLY)

    def add_files_assets_gallery(self,title):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(self.GALLERY_ITEMS_FOLDER)
        self.do_click(self.GALLERY_ITEMS_FOLDER_ADD_FILES)
        self.do_click(self.GALLERY_ITEMS_FOLDER_ADD_FILES_FROM_ASSETS)
        self.do_send_keys(self.GALLERY_ITEMS_FOLDER_AFFA_SEARCH_INPUT, title)
        self.do_click(self.GALLERY_ITEMS_FOLDER_AFFA_SEARCH_ICON)
        time.sleep(2)
        self.do_click(self.GALLERY_ITEMS_FOLDER_AFFA_CHECKBOX1)
        time.sleep(2)
        self.do_click(self.GALLERY_ITEMS_FOLDER_AFFA_SEARCH_INPUT_CLOSE)

    def upload_file_gallery(self, folder_path):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(self.GALLERY_ITEMS_FOLDER)
        self.do_click(self.GALLERY_ITEMS_FOLDER_ADD_FILES)
        self.do_click(self.GALLERY_CHOOSE_FILES_BUTTON)
        pyautogui.typewrite(folder_path, interval=0.15)
        pyautogui.press('enter')

    def upload_files_main_link(self,folder_path):
        self.do_click(self.MAIN_GALLERY_LINK)
        self.do_click(self.UPLOAD_FILES_GALLERY_MAIN_LINK)
        self.do_click(self.GALLERY_CHOOSE_FILES_BUTTON_MAIN)
        time.sleep(2)
        pyautogui.typewrite(folder_path, interval=0.15)
        pyautogui.press('enter')




