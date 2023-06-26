#### Creating this forms only for learning tesing forms

from django import forms

class test_Forms(forms.Form):
    title=forms.CharField(label='Title', max_length=100)
    amount=forms.IntegerField(label='Total_amount', initial=0)    # instead of default
    category=forms.CharField(label='Category', max_length=100)