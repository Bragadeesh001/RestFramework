from selenium import webdriver
from api_crud import Task
from django.contrib.statisfiles.testing import staticServerTestCase
from django.urls import reverse


class Testprojectlistpage(staticServerTestCase):


    def setUp(self):
        self.browser = webdriver.IE(r"C:\IEDriverServer.exe")

    def teardown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed():
        self.browser.get(self.live_server_url)
        time.sleep(20)



