from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Config.config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
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
    ASSETS_INFO_ADD_NEW_TAG_BUTTON = (By.CSS_SELECTOR,".selectTags")
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
    ASSETS_PLAY_VIDEO_HOVER = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/video")
    ASSETS_PAUSE_VIDEO_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")
    ASSETS_TRIMMING_CONTROLS_START_TIME = (By.CSS_SELECTOR,".mejs-currenttime")

    SUBTITLES_AND_CAPTIONS_ICON_GEAR = (By.CSS_SELECTOR,".popup_action.btn.rounded")
    SUBTITLES_AND_CAPTIONS_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[7]")
    SUBTITLES_AND_CAPTIONS_ENTER_LANGUAGE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[5]/div[2]/div[2]/div[1]/div/div/a/div/input")
    SUBTITLES_AND_CAPTIONS_ENGLISH_LANGUAGE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[5]/div[2]/div[2]/div[1]/div/ul/li[2]/a")
    SUBTITLES_AND_CAPTIONS_CREATE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[5]/div[2]/div[2]/div[2]/a[1]")
    CREATE_LINE = (By.ID,"lineCreate")
    DELETE_LINE = (By.ID,"lineDelete")
    INSERT_BEFORE = (By.ID,"lineInsertBefore")
    INSERT_AFTER = (By.ID,"lineInsertAfter")
    MERGE_WITH_NEXT = (By.ID,"lineMergeWithNext")
    EDIT_TEXT_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[1]/textarea")

    CHAPTERS_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[8]")
    ADD_CHAPTER_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/a[1]")
    ADD_CHAPTER_TIME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tbody/tr/td[1]/input")
    ADD_CHAPTER_TITLE_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tbody/tr/td[2]/input")
    SAVE_ADDED_CHAPTER = (By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/button')
    ADD_CHAPTER_TIME_INPUT1 = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tbody/tr[1]/td[1]/input")
    ADD_CHAPTER_TITLE_INPUT1 = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tbody/tr[2]/td[2]/input")
    HOVER_TO_DELETE1 = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tr[2]")
    DELETE_CHAPTER1 = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tr[2]/td[3]/a")
    HOVER_TO_DELETE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tr")
    DELETE_CHAPTER = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[11]/div[2]/table/tr[1]/td[3]/a")

    ANNOTATION_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[9]")
    ADD_ANNOTATION_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/a")
    EXPLORE_ME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[3]/div[1]/textarea")
    ANNOTATION_START_TIME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[3]/div[2]/div[1]/div/div[1]/input")
    ANNOTATION_END_TIME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[3]/div[2]/div[2]/div/div[1]/input")
    ANNOTATION_CREATE_ANNOTATION_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[3]/div[9]/div[1]")
    VIDEO_PLAY_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[4]/div")
    EDIT_EXISTING_ANNOTATION = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[1]/div/a")
    DELETE_ANNOTAION_ITEM = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[1]/ul/li[2]/a")
    DELETE_ANNOTAION_ITEM_DELETE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[2]/div[1]/div[1]/div[1]/span")

    CALL_TO_ACTION_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/ul/li[10]")
    CALL_TO_ACTION_TIME_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[13]/div[2]/div/div/div[2]/div[1]/div/div/div[1]/input")
    CALL_TO_ACTION_TYPE_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[13]/div[2]/div/div/div[2]/div[2]/div/select")
    CALL_TO_ACTION_UPLOAD_IMAGE = (By.CSS_SELECTOR,".cta-upload.video-thumbnail-text")
    CALL_TO_ACTION_UPLOAD_IMAGE_BUTTON = (By.XPATH,"/html/body/div[11]/div/div/div/div[2]/div/div/div/div/div[1]/button")
    UPLOAD_IMAGE_FILE_PATH = "C:\\Users\\User\\Pictures\\Untitled-474-450x300.jpg"
    CALL_TO_ACTION_LINK_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[13]/div[2]/div/div/div[2]/div[6]/div/input")
    CALL_TO_ACTION_SAVE_BUTTON = (By.CSS_SELECTOR,".btn.blue.primary.cta-annotation-save")
    CALL_TO_ACTION_CLICK_THUMBNAIL_OPEN_NEW_PAGE = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[6]/div/div/div/div/img")
    NEW_PAGE_ADDRESS = "www.behance.net"











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
        # self.do_click(self.ASSETS_INFO_TITLE_INPUT)
        self.do_clear(self.ASSETS_INFO_TITLE_INPUT)
        self.do_send_keys(self.ASSETS_INFO_TITLE_INPUT, "Record 1111")
        # self.do_click(self.ASSETS_INFO_DESCRIPTION_INPUT)
        self.do_clear(self.ASSETS_INFO_DESCRIPTION_INPUT)
        self.do_send_keys(self.ASSETS_INFO_DESCRIPTION_INPUT,"Record 1111 description")
        # self.do_click(self.ASSETS_INFO_NOTES_INPUT)
        time.sleep(2)
        self.do_clear(self.ASSETS_INFO_NOTES_INPUT)
        self.do_send_keys(self.ASSETS_INFO_NOTES_INPUT,"Record 1111 Notes")
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_BUTTON)  # ?????????????????BUG??????????????????????
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_BUTTON)  # ?????????????????BUG??????????????????????
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_INFO_ADD_NEW_TAG_INPUT,"Record 1111 tag")
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_CREATE)
        time.sleep(2)
        self.do_click(self.ASSETS_INFO_ADD_NEW_TAG_APPLY)
        time.sleep(2)
        self.do_clear(self.ASSETS_INFO_RELATED_LINK_TEXT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_INFO_RELATED_LINK_TEXT,"Record 1111 related link text")
        self.do_clear(self.ASSETS_INFO_RELATED_LINK_URL)
        self.do_send_keys(self.ASSETS_INFO_RELATED_LINK_URL,"Record 1111 related link URL")
        #page must be refreshed in order the description and other texts to be seen in classes, also time.sleep is required.
        self.driver.refresh()
        time.sleep(3)
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
        self.do_send_keys(self.START_TIME_INPUT,"00:01:05")
        time.sleep(2)
        self.do_click(self.END_TIME_INPUT)
        self.do_clear(self.END_TIME_INPUT)
        self.do_send_keys(self.END_TIME_INPUT, "00:05:50")
        time.sleep(2)
        self.do_click(self.ASSETS_REFRESH_MAIN_BUTTON)
        time.sleep(2)
        self.do_click(self.ASSETS_PLAY_ASSET_3)
        time.sleep(2)
        self.do_hover(self.ASSETS_PLAY_VIDEO_HOVER)
        time.sleep(2)
        self.do_click(self.ASSETS_PAUSE_VIDEO_BUTTON)
        time.sleep(1)

    def subtitles_and_captions(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ASSETS_SEARCH_INPUT, "Record 1111")
        time.sleep(2)
        self.do_click(self.ASSETS_SEARCH_INPUT_SEARCH)
        time.sleep(2)
        self.do_click(self.SUBTITLES_AND_CAPTIONS_ICON_GEAR)
        time.sleep(2)
        self.do_click(self.SUBTITLES_AND_CAPTIONS_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.SUBTITLES_AND_CAPTIONS_ENTER_LANGUAGE)
        # languages_menu = self.driver.find_element(By.CSS_SELECTOR,".dd-options.dd-click-off-close")*********************************
        # sel = Select(languages_menu)***********************************SELECT ONLY WORKS ON SELECT ELEMENTS, NOT ON UL************
        # sel.select_by_visible_text("English")*****************************************************************************
        # print("Selected English language for subtitles")**********************************************************************
        # SUBTITLE_OPTION_LANGUAGES = self.driver.find_elements(By.CLASS_NAME, "dd-option-text")
        # SUBTITLE_OPTION_LANGUAGES_CLASS = self.driver.find_element(By.CSS_SELECTOR,".dd-option")
        # for language in SUBTITLE_OPTION_LANGUAGES:
        #     # print (language.text)
        #     if language.text == "English":
        #         print(language)
        self.do_click(self.SUBTITLES_AND_CAPTIONS_ENGLISH_LANGUAGE)
        time.sleep(2)
        self.do_click(self.SUBTITLES_AND_CAPTIONS_CREATE_BUTTON)
        time.sleep(2)
        self.do_click(self.CREATE_LINE)
        time.sleep(2)
        self.do_click(self.EDIT_TEXT_INPUT)
        self.do_send_keys(self.EDIT_TEXT_INPUT,"This is a sample row 1")
        time.sleep(2)
        self.do_click(self.CREATE_LINE)
        time.sleep(2)
        self.do_send_keys(self.EDIT_TEXT_INPUT,"This is a sample row 2")
        time.sleep(2)
        self.do_click(self.CREATE_LINE)
        time.sleep(2)
        self.do_send_keys(self.EDIT_TEXT_INPUT,"This is a sample row 3")
        time.sleep(2)
        self.do_click(self.CREATE_LINE)
        time.sleep(2)
        self.do_send_keys(self.EDIT_TEXT_INPUT,"This is a sample row 4")
        time.sleep(2)
        self.do_click(self.CREATE_LINE)
        time.sleep(2)
        self.do_send_keys(self.EDIT_TEXT_INPUT,"This is a sample row 5")
        time.sleep(2)
        self.do_click(self.INSERT_BEFORE)
        time.sleep(2)
    def add_chapter(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.CHAPTERS_MAIN_LINK)
        self.do_click(self.ADD_CHAPTER_BUTTON)
        time.sleep(2)
        self.do_send_keys(self.ADD_CHAPTER_TIME_INPUT,"20")
        time.sleep(2)
        pyautogui.press('left')
        time.sleep(2)
        self.do_send_keys(self.ADD_CHAPTER_TIME_INPUT,'03')
        time.sleep(3)
        pyautogui.press('left')
        time.sleep(3)
        self.do_send_keys(self.ADD_CHAPTER_TIME_INPUT,"00")
        time.sleep(2)
        self.do_click(self.ADD_CHAPTER_TITLE_INPUT)
        self.do_send_keys(self.ADD_CHAPTER_TITLE_INPUT,"Sample chapter 1")
        time.sleep(2)
        self.do_click(self.SAVE_ADDED_CHAPTER)
        time.sleep(2)
        self.do_click(self.ADD_CHAPTER_BUTTON)
        time.sleep(2)
        pyautogui.press('right')
        time.sleep(2)
        pyautogui.press('right')
        time.sleep(2)
        self.do_send_keys(self.ADD_CHAPTER_TIME_INPUT1,"45")
        time.sleep(2)
        pyautogui.press('left')
        time.sleep(2)
        self.do_send_keys(self.ADD_CHAPTER_TIME_INPUT1,'06')
        time.sleep(2)
        self.do_click(self.ADD_CHAPTER_TITLE_INPUT)
        time.sleep(2)
        self.do_send_keys(self.ADD_CHAPTER_TITLE_INPUT1,"Sample chapter 2")
        time.sleep(2)
        self.do_click(self.SAVE_ADDED_CHAPTER)
        time.sleep(5)
    def del_chapter(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.CHAPTERS_MAIN_LINK)
        self.do_hover(self.HOVER_TO_DELETE1)
        time.sleep(2)
        self.do_click(self.DELETE_CHAPTER1)
        time.sleep(2)
        self.do_hover(self.HOVER_TO_DELETE)
        time.sleep(2)
        self.do_click(self.DELETE_CHAPTER)
        self.do_click(self.SAVE_ADDED_CHAPTER)
    def add_annotation(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ANNOTATION_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.ADD_ANNOTATION_BUTTON)
        time.sleep(2)
        self.do_send_keys(self.EXPLORE_ME_INPUT, "Sample explore me annotation")
        time.sleep(2)
        start_time_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[3]/div[2]/div[1]/div/div[1]/input")
        start_time_input.clear()
        self.do_send_keys(self.ANNOTATION_START_TIME_INPUT,"00:04:45")
        time.sleep(2)
        end_time_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[12]/div[2]/div[3]/div[2]/div[2]/div/div[1]/input")
        end_time_input.clear()
        self.do_send_keys(self.ANNOTATION_END_TIME_INPUT,"00:04:50")
        time.sleep(2)
        self.do_click(self.ANNOTATION_CREATE_ANNOTATION_BUTTON)
        time.sleep(2)
        self.do_click(self.VIDEO_PLAY_BUTTON)
        time.sleep(2)
    def del_annotation(self):
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.ANNOTATION_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.EDIT_EXISTING_ANNOTATION)
        time.sleep(2)
        self.do_click(self.DELETE_ANNOTAION_ITEM)
        time.sleep(2)
        self.do_click(self.DELETE_ANNOTAION_ITEM_DELETE)
    def call_to_action(self):        #####################dropdown option select##########################
        self.do_click(self.ASSETS_PAGE_MAIN_LINK)
        self.do_click(self.ASSETS_SETTINGS_ICON_GEAR)
        self.do_click(self.CALL_TO_ACTION_MAIN_LINK)
        time.sleep(2)
        call_to_action_time_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[13]/div[2]/div/div/div[2]/div[1]/div/div/div[1]/input")
        call_to_action_time_input.clear()
        time.sleep(2)
        self.do_send_keys(self.CALL_TO_ACTION_TIME_INPUT,"06:30")
        time.sleep(2)
        select = Select(self.driver.find_element(By.ID,"cta-annotation-type"))
        print(select.options)
        print (o.text for o in select.options)
        select.select_by_visible_text("Image")
        time.sleep(2)
        self.do_click(self.CALL_TO_ACTION_UPLOAD_IMAGE)
        time.sleep(2)
        self.do_click(self.CALL_TO_ACTION_UPLOAD_IMAGE_BUTTON)
        time.sleep(2)
        pyautogui.typewrite(self.UPLOAD_IMAGE_FILE_PATH, interval=0.15)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)
        link = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[13]/div[2]/div/div/div[2]/div[6]/div/input")
        link.clear()
        self.do_send_keys(self.CALL_TO_ACTION_LINK_INPUT,self.NEW_PAGE_ADDRESS)
        time.sleep(2)
        self.do_click(self.CALL_TO_ACTION_SAVE_BUTTON)
        time.sleep(2)
        self.do_click(self.CALL_TO_ACTION_CLICK_THUMBNAIL_OPEN_NEW_PAGE)
        time.sleep(5)


























































