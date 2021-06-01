from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.GalleriesPage import GalleriesPage
from selenium.webdriver.common.by import By
import time
import pyautogui

class PhotonWizard(BasePage):
    CREATE_GALLERY_MAIN_LINK = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul[3]/li/div")
    CREATE_GALLERY_MAIN_LINK_ARROW = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul[3]/li/div/div/i")
    GALLERY_FROM_TEMPLATE = (By.XPATH,"/html/body/div[1]/div[1]/div[2]/ul[3]/li/div/div/ul/li[2]/a")
    PHOTON_PLAYER_HOVER = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/ul/li[3]/div/div[1]")
    PHOTON_PLAYER_CREATE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/ul/li[3]/div/div[2]/a")

    PLAYER_COLOR_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[1]/div[1]/div[4]/p")
    PLAYER_COLOR_INPUT = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[1]/div[1]/div[4]/div[2]/div/div/div/div[1]/input")
    PLAYER_COLOR_INPUT_DONE = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[1]/div[1]/div[4]/div[1]")

    GALLERY_PAGE_MAIN_LINK = (By.XPATH,"/html/body/div[1]/div[1]/ul/li[1]")
    CUSTOMIZE_GALLERY_GEAR_ICON = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]/a[1]/i")
    ENABLE_VIDEO_CHAPTERS_TOGGLE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[1]/div[1]/div[5]/p")
    MAIN_SAVE_AND_NEXT_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/button[2]")
    TEST_GALLERY = (By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[1]/div")

    VIDEO_POPUP_TOGGLE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[1]/div[3]")
    VIDEO_POPUP_OPTION_THUMBNAIL = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/ul/li[2]/label/b")
    VIDEO_POPUP_OPTION_TEXT = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/ul/li[3]/label")
    VIDEO_POPUP_ARROW_DOWN = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[1]/p/div/span")
    VIDEO_POPUP_DONE = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[1]/div[1]")
    VIDEO_THUMBNAIL = (By.XPATH,"/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div[1]")
    VIDEO_THUMBNAIL_OPEN_VIDEO = (By.XPATH,"/html/body/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/video")
    VIDEO_THUMBNAIL_OPEN_TEXT = (By.XPATH,"/html/body/div[1]/div/div/div/div/div[1]/p")

    AUTOPLAY_POPUP_ARROW_DOWN = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[2]/p/div/span")
    START_ON_MUTE_RADIO = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[2]/div[2]/div/div/div/div/ul/li[2]/label/b")
    AUTOPLAY_WITH_SOUND = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[2]/div[2]/div/div/div/div/ul/li[3]/label/b")
    AUTOPLAY_WHEN_SCROLL = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[2]/div[2]/div/div/div/div/ul/li[4]/label/b")
    VIDEO_AUTOPLAY_DONE = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[3]/div[1]/div[2]/div[1]")

    LEAD_GEN_TOGGLE_BUTTON = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[4]/div[1]/div[1]/div[3]/label")
    LEAD_GEN_BTN_ARROW = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[4]/div[1]/div[1]/p/div/span")
    SHOW_AFTER_FIRST_VIDEO_RADIO = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[4]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/label/b")
    LEAD_GEN_DONE = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[4]/div[1]/div[1]/div[1]")
    SHOW_BEFORE_FIRST_VIDEO_RADIO = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[4]/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/ul/li[3]/label/b")




    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def create_photon_wizard(self):
        self.do_hover(self.CREATE_GALLERY_MAIN_LINK_ARROW)
        time.sleep(2)
        self.do_click(self.GALLERY_FROM_TEMPLATE)
        time.sleep(2)
        self.do_hover(self.PHOTON_PLAYER_HOVER)
        time.sleep(2)
        self.do_click(self.PHOTON_PLAYER_CREATE_BUTTON)
    def customize_save_galleries(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.TEST_GALLERY)
        time.sleep(2)
    def change_player_color(self):
        time.sleep(2)
        self.do_click(self.PLAYER_COLOR_BUTTON)
        time.sleep(2)
        self.do_click(self.PLAYER_COLOR_INPUT)
        time.sleep(2)
        self.do_clear(self.PLAYER_COLOR_INPUT)
        time.sleep(2)
        self.do_send_keys(self.PLAYER_COLOR_INPUT,"#0892dd")
        time.sleep(2)
        self.do_click(self.PLAYER_COLOR_INPUT_DONE)
    def enable_video_chapters(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(3)
        elem = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[1]/div[1]/div[5]/p')
        elem.click()
        time.sleep(5)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(5)
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(5)
        self.do_click(self.TEST_GALLERY)
        time.sleep(2)
        new_page = self.driver.window_handles[1]
        self.driver.switch_to.window(new_page)
        time.sleep(2)
    def disable_video_chapters(self):
        new_page = self.driver.window_handles[0]
        self.driver.switch_to.window(new_page)
        # self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        elem = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[8]/div[1]/div/ul/li[1]/div[1]/div[5]/div[3]')
        if elem.is_enabled():
            elem.click()
            time.sleep(2)
        else:
            pass
        time.sleep(5)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(5)
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(5)
        self.do_click(self.TEST_GALLERY)
        time.sleep(2)
        # new_page = self.driver.window_handles[1]
        # self.driver.switch_to.window(new_page)
        # time.sleep(2)
    def video_popup(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        # new_page = self.driver.window_handles[0]
        # self.driver.switch_to.window(new_page)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.VIDEO_POPUP_ARROW_DOWN)
        time.sleep(2)
        self.do_click(self.VIDEO_POPUP_OPTION_THUMBNAIL)
        time.sleep(2)
        self.do_click(self.VIDEO_POPUP_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
    def text_popup(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.VIDEO_POPUP_ARROW_DOWN)
        time.sleep(2)
        self.do_click(self.VIDEO_POPUP_OPTION_TEXT)
        time.sleep(2)
        self.do_click(self.VIDEO_POPUP_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
    def video_autoplay(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.AUTOPLAY_POPUP_ARROW_DOWN)
        time.sleep(2)
        self.do_click(self.START_ON_MUTE_RADIO)
        time.sleep(2)
        self.do_click(self.VIDEO_AUTOPLAY_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
    def video_autoplay_with_sound(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.AUTOPLAY_POPUP_ARROW_DOWN)
        time.sleep(2)
        self.do_click(self.AUTOPLAY_WITH_SOUND)
        time.sleep(2)
        self.do_click(self.VIDEO_AUTOPLAY_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
    def video_autoplay_scroll_view(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.AUTOPLAY_POPUP_ARROW_DOWN)
        time.sleep(2)
        self.do_click(self.AUTOPLAY_WITH_SOUND)
        time.sleep(2)
        self.do_click(self.VIDEO_AUTOPLAY_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
    def lead_gen_after_first_video(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.LEAD_GEN_TOGGLE_BUTTON)
        time.sleep(2)
        self.do_click(self.SHOW_AFTER_FIRST_VIDEO_RADIO)
        time.sleep(3)
        print(pyautogui.position())
        time.sleep(2)
        pyautogui.click(486,851)
        self.do_click(self.LEAD_GEN_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
    def lead_gen_before_first_video(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        self.do_click(self.CUSTOMIZE_GALLERY_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.LEAD_GEN_BTN_ARROW)
        time.sleep(2)
        self.do_click(self.SHOW_BEFORE_FIRST_VIDEO_RADIO)
        time.sleep(3)
        print(pyautogui.position())
        time.sleep(2)
        pyautogui.click(486,851)
        self.do_click(self.LEAD_GEN_DONE)
        time.sleep(2)
        self.do_click(self.MAIN_SAVE_AND_NEXT_BUTTON)
        time.sleep(2)
        self.customize_save_galleries()
        self.do_click(self.TEST_GALLERY)











































