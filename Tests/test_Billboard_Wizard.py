import pytest
from Pages.BillboardWizard import BillboardWizard
from Pages.LoginPage import LoginPage
from Pages.PhotonWizard import PhotonWizard
from Pages.MainPage import LoginPages
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.GalleriesPage import GalleriesPage
from Pages.AssetsPage import AssetsPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pyautogui
import time

class Test_Billboard_Wizard(BaseTest):
    MAIN_PLAY_BUTTON = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[1]/div/div/div[2]/div[6]/div")
    MAIN_PLAY_BUTTON2 = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[1]/div/div/div[2]/div[4]/div")
    FORWARD_BUTTON = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[2]/li[2]/a")
    def test_login(self):
        self.billboard_wizard = LoginPages(self.driver)
        self.billboard_wizard.login()
    def test_set_basic_settings(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.set_basic_settings()
        bb_wizard_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/span/span[2]")
        bwname_text = bb_wizard_name.text
        if bwname_text == "LA COLERE DE SANCETRES":
            print("********The title is changed *********")
        bb_wizard_desc = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[3]")
        bb_wizard_desc_text = bb_wizard_desc.text
        if bb_wizard_desc_text == "LA COLERE DE SANCETRES and other files":
            print("******The description is changed ***********")
    def test_autocontinue(self): ### move forward to third video, wait 10 sec to switch to next video and check autocontinue
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.autocontinue()
        autocontinue_on = self.driver.find_element(By.CSS_SELECTOR,".itoggle.toggleOnOff.iTon")
        autocontinue_off = self.driver.find_element(By.CSS_SELECTOR,".itoggle.toggleOnOff.iToff")
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        self.billboard_wizard.do_click(self.MAIN_PLAY_BUTTON)
        time.sleep(2)
        self.billboard_wizard.do_click(self.FORWARD_BUTTON)
        time.sleep(2)
        self.billboard_wizard.do_click(self.FORWARD_BUTTON)
        time.sleep(12)
        if autocontinue_off and self.MAIN_PLAY_BUTTON:
            print("*****autocontinue is off working***********")
        if autocontinue_on:
            self.billboard_wizard.do_click(self.MAIN_PLAY_BUTTON2)
            time.sleep(12)
            print("******autocontinue is on working**********")
    def test_add_title_align_left(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.add_title_align_left()
        left = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]")
        print(left.get_attribute("style"))
        if left.get_attribute("style") == "text-align: left; padding: 20px; overflow: hidden; box-sizing: border-box;":
            print("*******title is left aligned******")
        else:
            print("--------title left aligned failed-------")
    def test_add_title_align_right(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.add_title_align_right()
        right = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]")
        print(right.get_attribute("style"))
        if right.get_attribute("style") == "text-align: right; padding: 20px; overflow: hidden; box-sizing: border-box;":
            print("*******title is right aligned******")
        else:
            print("-------title right aligned failed-------")
    def test_title_desc_left(self): #### verify that video title and description are left and right aligned, after sliding back and forward also
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.title_desc_left()
        textbox_title = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]/h2/span[1]")
        textbox_desc = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]/h2/span[2]")
        left = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[3]")
        if textbox_title and textbox_desc and left.get_attribute("style") == "text-align: left; padding: 20px; overflow: hidden; box-sizing: border-box;":
            print("*****title and description on first item are  left aligned*******")
        else:
            print("-------title and description left align failed----------")
        time.sleep(2)
        forward_arrow = (By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[2]/li[2]/a")
        self.billboard_wizard.do_click(forward_arrow)
        time.sleep(2)
        self.billboard_wizard.do_click(forward_arrow)
        time.sleep(2)
        textbox_title3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[3]/h2/span[1]")
        textbox_desc3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[3]/h2/span[2]")
        left3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[3]/div[3]")
        if textbox_title3 and textbox_desc3 and left3.get_attribute("style") == "text-align: left; padding: 20px; overflow: hidden; box-sizing: border-box; height: 100px; opacity: 1;":
            print("*****title and description on third item are  left aligned*******")
        else:
            print("-------title and description  align failed on third item----------")
    def test_slideshow_on_off(self): #### verify that when slideshow is on/off video is being slided every 5 seconds
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.slideshow_on_off()
        toggle_on = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[8]/div[1]/ul/li[2]/div[2]/div[1]/div[4]/div/div/label")
        print(toggle_on.get_attribute("class")) #itoggle  toggleOnOff iTon
        if toggle_on.get_attribute("class") == "itoggle  toggleOnOff iTon":
            print("******* The slideshow is activated *******")
        iframe = self.driver.find_element(By.ID, "simulator_content")
        self.driver.switch_to.frame(iframe)
        second_item_thumb = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[2]")
        print(second_item_thumb.get_attribute("class"))
        if second_item_thumb.get_attribute("class") == "mediaObject video activatedPlugin flex-active-slide":
            print("****** The second items classname is printed *******")
        else:
            print("----- Slideshow activation failed --------")
    def test_autoplay_on_off(self): ### if autoplay toggle is on, play button style must be display: none
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.autoplay_on_off()
        main_play_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[1]/div/div/div[2]/div[6]")
        print(main_play_button.get_attribute("style"))
        if main_play_button.get_attribute("style") == "width: 901.5px; height: 507px; display: none;":
            print("****** The autoplay is activated *******")
        else:
            print("------ Autoplay activation failed -------")
    def test_control_navigation_numbers_top(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.control_navigation_numbers_top()
        numbers_top_id = self.driver.find_element(By.ID,"controls_navgallery_wrap_container")
        numbers_top_class_atribute = numbers_top_id.get_attribute("class")
        print(numbers_top_class_atribute)
        if numbers_top_class_atribute == "controls_top numbers_nav controls_slide ":
            print("******* The numbers top pagination is active ********")
        else:
            print("------- The numbers top pagination failed. ----------")
    def test_control_navigation_numbers_bottom(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.control_navigation_numbers_bottom()
        numbers_bottom_id = self.driver.find_element(By.ID,"controls_navgallery_wrap_container")
        numbers_bottom_class_atribute = numbers_bottom_id.get_attribute("class")
        print(numbers_bottom_class_atribute)
        if numbers_bottom_class_atribute == "controls_bottom numbers_nav controls_slide ":
            print("******* The numbers bottom pagination is active ********")
        else:
            print("------- The numbers bottom pagination failed. ----------")
    def test_control_navigation_bullets_top(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.control_navigation_bullets_top()
        bullets_top_id = self.driver.find_element(By.ID,"controls_navgallery_wrap_container")
        bullets_top_class_atribute = bullets_top_id.get_attribute("class")
        print(bullets_top_class_atribute)
        if bullets_top_class_atribute == "controls_top navigation_rounds controls_slide ":
            print("******* The bullets top pagination is active ********")
        else:
            print("------- The bullets top pagination failed. ----------")
    def test_control_navigation_bullets_bottom(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.control_navigation_bullets_bottom()
        bullets_bottom_id = self.driver.find_element(By.ID,"controls_navgallery_wrap_container")
        bullets_bottom_class_atribute = bullets_bottom_id.get_attribute("class")
        print(bullets_bottom_class_atribute)
        if bullets_bottom_class_atribute == "controls_bottom navigation_rounds controls_slide ":
            print("******* The bullets bottom pagination is active ********")
        else:
            print("------- The bullets bottom pagination failed. ----------")
    def test_control_navigation_thumbnail_title_top(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.control_navigation_thumbnail_title_top()
        thumbnail_title_top_id = self.driver.find_element(By.ID,"controls_navgallery_wrap_container")
        title_top_class_atribute = thumbnail_title_top_id.get_attribute("class")
        print(title_top_class_atribute)
        if title_top_class_atribute == "controls_top navigation_with_title thumbnails_nav controls_slide ":
            print("******* The thumbnail-title-top pagination is active ********")
        else:
            print("------- The thumbnail-title-top pagination failed. ----------")
    def test_control_navigation_thumbnail_title_bottom_thumbsize(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.control_navigation_thumbnail_title_bottom_thumbsize()
        thumbnail_title_bottom_id = self.driver.find_element(By.ID,"controls_navgallery_wrap_container")
        title_bottom_class_attribute = thumbnail_title_bottom_id.get_attribute("class")
        print(title_bottom_class_attribute)
        if title_bottom_class_attribute == "controls_bottom navigation_with_title thumbnails_nav controls_slide ":
            print("*******The thumbnail-title-bottom pagination is activated******")
        else:
            print("--------The thumbnail-title-bottom pagination failed.--------")
    def test_nav_arrow_off(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.nav_arrow_off()
        try:
            slide_arrows_class = self.driver.find_element(By.CSS_SELECTOR,".flex-direction-nav")
            if (slide_arrows_class):
                print("-------Navigation arrows disabling failed.------")
        except:
            print("*******The navigation arrows are disabled******")
    def test_mute_video(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.mute_video()
        try:
            mute_video_control = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-volume-button.mejs-unmute")
            if mute_video_control:
                print("******** The video mute control is toggled on*********")
        except:
            print("--------Mute control is not working--------")
    def test_popup_video(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.popup_video()
        next_video_content = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[5]/div[2]/div/div/div[1]/p")
        print(next_video_content.text)
        if next_video_content.is_displayed():
            print("********The next video content is visible*********")
        else:
            print("-----------The next video content is not displayed.-----------")                                      ######### BUG #########
    def test_randomize_slide_order(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.randomize_slide_order()
        next_videos_class = self.driver.find_elements(By.CSS_SELECTOR,".flex-next-video")
        second_video_class = self.driver.find_elements(By.CSS_SELECTOR,".ze_video.mediaElementObject")
        # for video in next_videos_class:
        #     print(video.get_attribute("style")[23:110])
        print(next_videos_class[0].get_attribute("style")[23:120])
        print(second_video_class[2].get_attribute("poster"))
        if next_videos_class[0].get_attribute("style")[23:120] == second_video_class[2].get_attribute("poster"):
            print("******* In Randomized Slide Order the next video is the same as the actual displayed one ******")
        else:
            print("----- The Randomized Slide Order is Wrong --------")                                             ##### BUG #######


    ##############################/////////////////////////////////////////////##################################################

    def test_show_play_pause_button(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.show_play_pause_button()
        try:
            controls_play = self.driver.find_element(By.CSS_SELECTOR, ".mejs-button.mejs-playpause-button.mejs-play")
            controls_pause = self.driver.find_element(By.CSS_SELECTOR, ".mejs-button.mejs-playpause-button.mejs-pause")
            if controls_pause or controls_play:
                print("-------  Play/Pause button can not be hidden, toggle is not working --------")
        except:
            print("******** Play/Pause button is hidden *******")

    def test_share_button(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.share_button()
        try:
            controls_share = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-share-button")
            if controls_share:
                print("******* Share button is added ***********")
        except:
            print("-------- Share button can not be added ---------")             ######## BUG ############
    def test_subtitle(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.subtitle()
        try:
            controls_subs = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-captions-button")
            if controls_subs:
                print("------ Subtitles are not being hidden ---------")
        except:
            print("******* Subtitles can be hidden with toggle button **********")
    def test_fullscreen(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.fullscreen()
        try:
            controls_fs = self.driver.find_element(By.CSS_SELECTOR,".mejs-button.mejs-fullscreen-button")
            if controls_fs:
                print("------ Fullscreen button can not be hidden. ---------")
        except:
            print("******* Fullscreen button is hidden with toggle. **********")

    def test_volume_button(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.volume_button()
        try:
            controls_volume = self.driver.find_element(By.CSS_SELECTOR, ".mejs-button.mejs-volume-button.mejs-mute")
            if controls_volume:
                print("------ Volume button can not be hidden. ---------")
        except:
            print("******* Volume button is hidden with toggle. **********")
    def test_time_control(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.time_control()
        try:
            controls_time = self.driver.find_element(By.CSS_SELECTOR, ".mejs-time")
            if controls_time:
                print("------ Time control can not be hidden. ---------")
        except:
            print("******* Time control is hidden with toggle. **********")
    def test_time_indication_bar(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.time_indication_bar()
        try:
            controls_indication = self.driver.find_element(By.CSS_SELECTOR, ".mejs-time-rail")
            if controls_indication:
                print("------ Time indication control can not be hidden. ---------")
        except:
            print("******* Time indication control is hidden with toggle. **********")
    def test_download_button(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.download_button()
        try:
            controls_download = self.driver.find_element(By.CSS_SELECTOR, ".mejs-button.mejs-download-button")
            if controls_download:
                print("******* Video download control is added. ********")
        except:
            print("-------- Video download control can not be added. ---------")
    def test_chapters_list(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.chapters_list()
        try:
            controls_chapters = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[1]/div/div/div[2]/div[8]/div/ol")
            if controls_chapters:
                print("******* Video chapters control is added. ********")
        except:
            print("-------- Video chapters control can not be added. ---------")
    def test_video_trim(self):
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.video_trim()
        time.sleep(2)
        all_buttons_class = self.driver.find_elements(By.CSS_SELECTOR,".mejs-overlay-button")
        for button in all_buttons_class:
            if button.get_attribute("aria-label") == "Play":
                button.click()
        time.sleep(1)
        print(pyautogui.position())
        time.sleep(2)
        pyautogui.click(1255,823)
        time.sleep(5)
        play_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/div[1]/div/div/div[2]/div[6]/div")
        if play_button.is_displayed():
            print("***** The video is not playing after the trim time is over ***********")
        else:
            print("------ Video trimming failed. The video is playing after the trim. ------")
    def test_overlay_watermarks(self):                                                  ############# BUG ###############
        self.billboard_wizard = BillboardWizard(self.driver)
        self.billboard_wizard.overlay_watermarks()
        overlay_watermark = self.driver.find_element(By.CSS_SELECTOR,".ze_overlay_watermark.ze_overlay")
        # print(overlay_watermark.get_attribute("style"))
        if overlay_watermark.get_attribute("style") == "left: 0px; bottom: 0px;":
            print("------ The watermark is out of the player. ----------")























