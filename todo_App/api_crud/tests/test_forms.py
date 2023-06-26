from django.test import SimpleTestCase
from api_crud.forms import test_Forms

class Testforms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form=test_Forms(data={
            'title':'expense1',
            'amount': 1000,
            'category': 'development'

        })

        self.assertTrue(form.is_valid())   #checking the form is valid

    def test_expense_form_no_data(self):
        form=test_Forms(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
