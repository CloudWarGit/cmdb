from django import forms

class HostAddForm(forms.Form):
    host_name = forms.CharField(label='主机名', max_length=100)