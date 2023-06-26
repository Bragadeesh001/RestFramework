from django.test import TestCase, Client     # client is not the only way to test views there are other ways
from django.urls import reverse
from api_crud.models import Task


class TestViews(TestCase):


    def setUp(self):
        self.client=Client()

        self.list_url = reverse('task-list')

        self.detail_url = reverse('task-detail', args=['1'])
        
        Task.objects.create(
            id=1,
            title='Test cases',
            completed='False'
        )

        self.create_url = reverse('task-create')

        ## delete
        self.delete=Task.objects.create(
            title='Test cases',
            completed='False'
        )
        self.delete_url=reverse('task-delete', args=[str(self.delete.id)])

        ## Update
        self.task=Task.objects.create(
            title='Original',
            completed=True
        )
        self.update_url=reverse('task-update', args=[self.task.id])


    ## if setUp is not there
    # def test_task_detail_Get(self):
    #     client=Client()
    #     response=client.get(reverse('task-list'))    # url name

    #     self.assertEquals(response.status_code, 200)
        #self.assertTemplateUsed(response, 'api_crud/task_detail.htm')   # for html

    def test_task_detail_Get(self):
        response=self.client.get(self.list_url)    # url name
        self.assertEquals(response.status_code, 200)

    def test_task_detail_Get(self):
        response=self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_task_create_post(self):
        response= self.client.post(self.create_url,{
            "id":"1",
            "title":"Test_views",
            "completed":"True"
        })

        self.assertEquals(response.status_code, 200)

        #### Checking weather the data got posted in database
        from api_crud.models import Task  # Import your Todo model
        self.assertTrue(Task.objects.filter(title='Test_views').exists())

    
    def test_task_delete(self):
        response=self.client.delete(self.delete_url)
        self.assertEquals(response.status_code, 200)

#### Doubt in update (PUT)
    # def test_task_update(self):
    #     response=self.client.put(self.update_url, {
    #         "title":"Original title",
    #         "completed":True
    #     })

    #     self.assertEquals(response.status_code,200)

