from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api_crud.views import taskCreate, taskList, taskDetail

class TestUrls(SimpleTestCase): ## Testing urls is working fine or not
    def test_list_url_is_resolved(self):
        url = reverse('task-list') # name of the url created in app url
        print(resolve(url))
        self.assertEquals(resolve(url).func, taskList) # Function name


    def test_create_url_is_resolved(self):
        url = reverse('task-create') # name of the url created in app url
        print(resolve(url))
        self.assertEquals(resolve(url).func, taskCreate) # Function name

    def test_detail_url_is_resolved(self):
        url = reverse('task-detail',args=['0']) # name of the url created in app url 
        print(resolve(url))
        self.assertEquals(resolve(url).func, taskDetail) # Function name