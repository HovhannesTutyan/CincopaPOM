from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Config.config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pyautogui

class AssetsPage(BasePage):
    ASSETS_PAGE_MAIN_LINK=(By.XPATH,"/html/body/div[1]/div[1]/ul/li[2]/a")
    ASSETS_PAGE_MAIN_CHECKBOX=(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/a")
    ASSETS_CHECKBOX_COPY_ITEMSNUMBER="Copy To(10)"
    ASSETS_SEARCH_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/input")
    ASSETS_SEARCH_INPUT_ITEM_DELETE = 'New Added Asset'
    ASSETS_SEARCH_INPUT_SEARCH = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/a[1]/i")
    ASSETS_MAIN_DELETE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/a/i")
    ASSETS_DELETE_FILES_FOREVER = (By.XPATH,"/html/body/div[11]/div/div/div/div[2]/div[2]/a")
    ASSETS_COPY_TO_BUG = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/a")
    ASSETS_COPY_TO_GALLERY_BUG = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div/ul/li[1]/a")
    YES_COPY_THE_FILES_BUG = (By.XPATH,"/html/body/div[11]/div/div/div/div[3]/div[2]/a")
    ASSETS_GO_GALLERY_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[1]/ul/li[1]/a")

    ASSETS_UPLOAD_FILES_MAIN_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/a[1]")
    ASSETS_UPLOAD_FILE_CHOOSE_FILE_MAIN_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[1]/div/div/button/i")
    ASSETS_UPLOAD_FILE_PATH = "C:\\Users\\User\\Downloads\\SampleVideo_720x480_2mb.mp4"
    ASSETS_ADD_TITLE_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[14]/div/form/div[1]/span[1]/input")
    ASSETS_ADD_DESCRIPTION_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[14]/div/form/div[1]/span[2]/textarea")
    ASSETS_ADD_TAG_NEW_ASSET = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[14]/div/form/div[2]/div[3]/a[1]")
    ASSETS_ADD_TAG_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[14]/div/form/div[2]/div[3]/div/div[1]/div/input")
    ASSETS_ADD_TAG_CREATE_TAG = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[14]/div/form/div[2]/div[3]/div/div[1]/div/p/span[2]")
    ASSETS_ADD_TAG_CREATE_TAG_APPLY = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/div/div[14]/div/form/div[2]/div[3]/div/div[2]/a")
    RETURN_TO_ASSETS_MAIN_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/button[2]")
    NEW_ASSET_TITLE_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[5]/div[6]/div[3]/div[2]/i")

    ASSETS_SETTINGS_ICON_GEAR = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[5]/div[1]/div[4]/a[2]/i")
    ASSETS_INFO_TITLE_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[1]/td/input")
    ASSETS_INFO_DESCRIPTION_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[2]/td/textarea")
    ASSETS_INFO_NOTES_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[3]/td/textarea")
    ASSETS_INFO_ADD_NEW_TAG_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[4]/td/a")
    ASSETS_INFO_ADD_NEW_TAG_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[4]/td/div[2]/div[1]/div/input")
    ASSETS_INFO_ADD_NEW_TAG_CREATE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[4]/td/div[2]/div[1]/div/p/span[2]")
    ASSETS_INFO_ADD_NEW_TAG_APPLY = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[4]/td/div[2]/div[2]/a")
    ASSETS_INFO_RELATED_LINK_TEXT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[5]/td/input")
    ASSETS_INFO_RELATED_LINK_URL = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[6]/table/tbody/tr[6]/td/input")

    ASSETS_SHARE_ASSET_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[2]")
    ASSETS_SHARE_ASSET_COPY_URL = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[7]/div[2]/div[2]/div[2]/p/span[1]/a")
    ASSETS_SET_THUMBNAIL_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[5]")
    ASSETS_SET_THUMBNAIL_IMAGE_RADIO = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[10]/div[2]/div/div[1]/label[1]/i")
    ASSETS_SET_THUMBNAIL_IMAGE_UPLOAD_IMAGE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[10]/div[2]/div/div[2]/div[3]/a")
    ASSETS_SET_THUMBNAIL_IMAGE_FILE_PATH = "C:\\Users\\User\\Pictures\\Screenshot_5_mam4um.png"
    ASSETS_REFRESH_MAIN_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/a[1]")
    ASSETS_BACK_TO_ASSETS = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/a")
    ASSETS_RESET_THUMBNAIL = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[10]/div[2]/div/div[2]/div[2]/a")
    ASSETS_PLAY_ASSET = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[5]/div[1]/div[2]/div")
    ASSETS_PLAY_ASSET_SEC = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[4]")

    ASSETS_SET_THUMBNAIL_VIDEO_RADIO = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[10]/div[2]/div/div[1]/label[2]/i")
    VIDEO_THUMBNAIL_SLIDER_HANDLE = (By.XPATH,"/html/body/form/div[3]/div[2]/div[3]/div[4]/div[1]/div[10]/div[2]/div/div[3]/div[1]/div[1]")

    ASSETS_TRIMMING_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[6]")
    START_TIME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[14]/div[2]/div/div[1]/div[1]/div/div[1]/input")
    END_TIME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[14]/div[2]/div/div[2]/div[1]/div/div[1]/input")
    ASSETS_PLAY_ASSET_3 = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[4]")









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
    def upload_file_to_assets_folder(self,name):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_UPLOAD_FILES_MAIN_BUTTON)
        self.do_click(self.ASSETS_UPLOAD_FILE_CHOOSE_FILE_MAIN_BUTTON)
        time.sleep(2)
        pyautogui.typewrite(name, interval=0.15)
        pyautogui.press('enter')
        time.sleep(15)
        self.do_click(self.ASSETS_ADD_TITLE_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_ADD_TITLE_INPUT,"New Added Asset")
        time.sleep(2)
        self.do_click(self.ASSETS_ADD_DESCRIPTION_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_ADD_DESCRIPTION_INPUT,"New Added Asset Description")
        time.sleep(2)
        self.do_click(self.ASSETS_ADD_TAG_NEW_ASSET)
        time.sleep(2)
        self.do_click(self.ASSETS_ADD_TAG_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_ADD_TAG_INPUT,"New Asset Tag")
        time.sleep(2)
        self.do_click(self.ASSETS_ADD_TAG_CREATE_TAG)
        time.sleep(2)
        self.do_click(self.ASSETS_ADD_TAG_CREATE_TAG_APPLY)
        time.sleep(2)
        self.do_click(self.RETURN_TO_ASSETS_MAIN_BUTTON)
        time.sleep(5)

    def view_assets_info(self): ###### There is a bug on the "Add new tag" button, with popup window.########
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ASSETS_INFO_TITLE_INPUT)
        self.do_clear(self.ASSETS_INFO_TITLE_INPUT)
        self.do_send_keys(self.ASSETS_INFO_TITLE_INPUT, "Record 1111")
        self.do_click(self.ASSETS_INFO_DESCRIPTION_INPUT)
        self.do_send_keys(self.ASSETS_INFO_DESCRIPTION_INPUT,"Record 1111 description")
        self.do_click(self.ASSETS_INFO_NOTES_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_INFO_NOTES_INPUT,"Record 1111 Notes")
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_BUTTON)#?????????????????BUG??????????????????????
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_INFO_ADD_NEW_TAG_INPUT,"Record 1111 tag")
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_RELATED_LINK_TEXT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_INFO_RELATED_LINK_TEXT,"Record 1111 related link text")
        self.do_click(self.ASSETS_INFO_RELATED_LINK_URL)
        self.do_send_keys(self.ASSETS_INFO_RELATED_LINK_URL,"Record 1111 related link URL")
    def share_asset(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ASSETS_SHARE_ASSET_MAIN_LINK)
        # copy_url_link = self.do_click(self.ASSETS_SHARE_ASSET_COPY_URL)
        # self.driver.execute_script("window.open('self.do_click(self.ASSETS_SHARE_ASSET_COPY_URL)','new window')")
        self.do_hover(self.ASSETS_SHARE_ASSET_COPY_URL)
        self.do_click(self.ASSETS_SHARE_ASSET_COPY_URL)
    def set_thumbnail_image_reset(self,file_path):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ASSETS_SET_THUMBNAIL_MAIN_LINK)
        self.do_click(self.ASSETS_SET_THUMBNAIL_IMAGE_RADIO)
        self.do_click(self.ASSETS_SET_THUMBNAIL_IMAGE_UPLOAD_IMAGE)
        time.sleep(2)
        pyautogui.typewrite(file_path, interval=0.15)
        pyautogui.press('enter')
        time.sleep(5)
        self.do_click(self.ASSETS_REFRESH_MAIN_BUTTON)
        time.sleep(5)
        self.do_click(self.ASSETS_BACK_TO_ASSETS)
        time.sleep(2)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ASSETS_SET_THUMBNAIL_MAIN_LINK)
        self.do_click(self.ASSETS_RESET_THUMBNAIL)
        time.sleep(2)
        self.do_click(self.ASSETS_REFRESH_MAIN_BUTTON)
        time.sleep(3)
        self.do_click(self.ASSETS_BACK_TO_ASSETS)
        time.sleep(2)
        self.do_click(self.ASSETS_PLAY_ASSET)
        time.sleep(2)
        self.do_click(self.ASSETS_REFRESH_MAIN_BUTTON)
        time.sleep(2)
        self.do_hover(self.ASSETS_PLAY_ASSET_SEC)
        time.sleep(2)
    def set_thumbnail_video(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ASSETS_SET_THUMBNAIL_MAIN_LINK)
        self.do_click(self.ASSETS_SET_THUMBNAIL_VIDEO_RADIO)
        ActionChains(self.driver).drag_and_drop_by_offset(self.VIDEO_THUMBNAIL_SLIDER_HANDLE, 60, 0).perform()

    def asset_trimming(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ASSETS_TRIMMING_LINK)
        self.do_click(self.START_TIME_INPUT)
        self.do_clear(self.START_TIME_INPUT)
        self.do_send_keys(self.START_TIME_INPUT,5)
        time.sleep(2)
        self.do_click(self.END_TIME_INPUT)
        self.do_clear(self.END_TIME_INPUT)
        self.do_send_keys(self.END_TIME_INPUT, 15)
        time.sleep(2)
        self.do_click(self.ASSETS_REFRESH_MAIN_BUTTON)
        time.sleep(2)
        self.do_click(self.ASSETS_PLAY_ASSET_3)























