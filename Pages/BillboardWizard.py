from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.GalleriesPage import GalleriesPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    AUTOPLAY_TOGGLE_ON = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[5]/div/div/label")
    CONTROL_NAVIGATION = (By.ID,"skin_param_list_control_nav")
    CONTROL_NAVIGATION_UL_OPTIONS = (By.CSS_SELECTOR,".dd-option")
    NAVIGATION_CONTROLS_THUMB_SIZE_W = (By.ID,"skin_param_size_nav_thumb_size_w")
    NAVIGATION_CONTROLS_THUMB_SIZE_H = (By.ID,"skin_param_size_nav_thumb_size_h")
    OVERLAY_TYPE = (By.ID,"skin_param_list_overlay_type")
    OVERLAY_TYPE_WATERMARK = By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[6]/div[2]/div[2]/div[1]/div/div/ul/li[3]/a"
    WATERMARK_POSITION_TOP_LEFT = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[6]/div[2]/div[2]/div[7]/div/div/ul/li[1]/a")
    WATERMARK_IMAGE_URL = (By.ID,"skin_param_text_overlay_watermark_url")
    WATERMARK_POSITION = (By.ID,"skin_param_list_overlay_watermark_position")
    WATERMARK_CLICK_URL = (By.ID,"skin_param_text_overlay_link")
    OVERLAY_TIME = (By.ID,"skin_param_list_overlay_time")
    OVERLAY_TIME_ON_LOAD = (By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[6]/div[2]/div[3]/div[6]/div/div/ul/li[1]/a")







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
        ##############################################################
    ########################## ADVANCED SETTINGS #######################
    ####################################################################
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
    def autoplay_on_off(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.AUTOPLAY_TOGGLE_ON)
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def control_navigation_numbers_top(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.CONTROL_NAVIGATION)
        time.sleep(2)
        control_navigation_ul_options = self.driver.find_elements(By.CSS_SELECTOR,".dd-option-text")
        for option in control_navigation_ul_options:
            print(option.text)
            if option.text == "Numbers on the top":
                option.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def control_navigation_numbers_bottom(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.CONTROL_NAVIGATION)
        time.sleep(2)
        control_navigation_ul_options = self.driver.find_elements(By.CSS_SELECTOR,".dd-option-text")
        for option in control_navigation_ul_options:
            print(option.text)
            if option.text == "Numbers on the bottom":
                option.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def control_navigation_bullets_top(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.CONTROL_NAVIGATION)
        time.sleep(2)
        control_navigation_ul_options = self.driver.find_elements(By.CSS_SELECTOR,".dd-option-text")
        for option in control_navigation_ul_options:
            print(option.text)
            if option.text == "Bullets on the top":
                option.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def control_navigation_bullets_bottom(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.CONTROL_NAVIGATION)
        time.sleep(2)
        control_navigation_ul_options = self.driver.find_elements(By.CSS_SELECTOR,".dd-option-text")
        for option in control_navigation_ul_options:
            print(option.text)
            if option.text == "Bullets on the bottom":
                option.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def control_navigation_thumbnail_title_top(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.CONTROL_NAVIGATION)
        time.sleep(2)
        control_navigation_ul_options = self.driver.find_elements(By.CSS_SELECTOR, ".dd-option-text")
        for option in control_navigation_ul_options:
            print(option.text)
            if option.text == "Thumbnails with title on the top":
                option.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def control_navigation_thumbnail_title_bottom_thumbsize(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        self.do_click(self.CONTROL_NAVIGATION)
        time.sleep(2)
        control_navigation_ul_options = self.driver.find_elements(By.CSS_SELECTOR,".dd-option-text")
        for option in control_navigation_ul_options:
            if option.text == "Thumbnails with title on the bottom":
                option.click()
        time.sleep(2)
        self.do_clear(self.NAVIGATION_CONTROLS_THUMB_SIZE_W)
        self.do_send_keys(self.NAVIGATION_CONTROLS_THUMB_SIZE_W,"200")
        time.sleep(2)
        self.do_clear(self.NAVIGATION_CONTROLS_THUMB_SIZE_H)
        self.do_send_keys(self.NAVIGATION_CONTROLS_THUMB_SIZE_H,"150")
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def nav_arrow_off(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        toggle_buttons_classnames = self.driver.find_elements(By.CSS_SELECTOR,".itoggle.toggleOnOff.iTon")
        for toggle in toggle_buttons_classnames:
            print(toggle.get_attribute("for"))
            if toggle.get_attribute("for") == "dummyskin_param_bool_show_nav":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def mute_video(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        toggle_buttons_classnames = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iToff")
        for toggle in toggle_buttons_classnames:
            print(toggle.get_attribute("for"))
            if toggle.get_attribute("for") == "dummyskin_param_bool_mute_video":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def popup_video(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        toggle_buttons_classnames = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iToff")
        for toggle in toggle_buttons_classnames:
            # print(toggle.get_attribute("for"))
            if toggle.get_attribute("for") == "dummyskin_param_bool_popup_video_mode":
                toggle.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def randomize_slide_order(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        self.do_click(self.ADVANCED_SETTINGS)
        time.sleep(2)
        toggle_buttons_classnames = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iToff")
        for toggle in toggle_buttons_classnames:
            # print(toggle.get_attribute("for"))
            if toggle.get_attribute("for") == "dummyskin_param_bool_randomize":
                toggle.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)

    ##################################################################
    ############## PLAYER CONTROL ##################################
    ################################################################
    def show_play_pause_button(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR,".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        time.sleep(2)
        # player_control_all_toggles_class = self.driver.find_elements(By.CSS_SELECTOR, ".argumentGroup.fieldItem.toggle.block")
        # for toggle in player_control_all_toggles_class:
        #     print(toggle.text)
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR,".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_play_button":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def share_button(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_share":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def subtitle(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_subtitle":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def fullscreen(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_fullscreen_videobutton":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def volume_button(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_volume_slider":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def time_control(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_timeControl":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def progress_indication_bar(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iTon")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_seekingBar":
                toggle.click()
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def download_button(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iToff")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_download_button":
                toggle.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def chapters_list(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        time.sleep(2)
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iToff")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_chapter":
                toggle.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
    def video_trim(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Player Control":
                control.click()
        time.sleep(2)
        all_toggles_on_off = self.driver.find_elements(By.CSS_SELECTOR, ".itoggle.toggleOnOff.iToff")
        for toggle in all_toggles_on_off:
            if toggle.get_attribute("for") == "dummyskin_param_bool_videoTrim":
                toggle.click()
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
        ##################################################################
        ############## OVERLAY ##################################
        ################################################################
    def overlay_watermarks(self):
        self.do_click(self.GALLERY_PAGE_MAIN_LINK)
        time.sleep(2)
        self.do_click(self.BILLBOARD_GALLERY_CUSTOMIZE_GEAR_ICON)
        time.sleep(2)
        all_controlls_classname = self.driver.find_elements(By.CSS_SELECTOR, ".followWrap")
        for control in all_controlls_classname:
            # print(control.text)
            if control.text == "Overlay":
                control.click()
        time.sleep(2)
        self.do_click(self.OVERLAY_TYPE)
        time.sleep(2)
        self.do_click(self.OVERLAY_TYPE_WATERMARK)
        time.sleep(2)
        self.do_send_keys(self.WATERMARK_IMAGE_URL, "https://cdn3.vectorstock.com/i/thumb-large/24/12/astronauts-and-aliens-chill-together-on-moon-vector-36202412.jpg")
        time.sleep(2)
        self.do_click(self.WATERMARK_POSITION)
        time.sleep(2)
        self.do_click(self.WATERMARK_POSITION_TOP_LEFT)
        time.sleep(2)
        self.do_send_keys(self.WATERMARK_CLICK_URL,"https://www.vectorstock.com/royalty-free-vectors/alien-eating-vectors")
        self.do_click(self.OVERLAY_TIME)
        time.sleep(2)
        self.do_click(self.OVERLAY_TIME_ON_LOAD)
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(2)



















