from django.test import TestCase
from api_crud.models import Task



class TestModels(TestCase):
    def setUp(self):
        #self.client=client()
        self.data=Task.objects.create(
            title='Testing_models',
            completed=False
        )

        self.data2=Task.objects.create(
            title='Testing_models_2',
            completed=True
        )

    def test_app_models(self):
        self.assertEquals(self.data.title, 'Testing_models')
        self.assertFalse(self.data.completed)    # Assert false is for testing completed is false


    def test_app_models_2(self):
        self.assertEquals(self.data2.title,'Testing_models_2')
        self.assertTrue(self.data2.completed)