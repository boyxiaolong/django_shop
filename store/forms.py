from django import forms

class AllenSearchForm(forms.Form):
    content = forms.CharField(label='', max_length=20
                              , widget=forms.TextInput(attrs={'id':'select'
                                                              ,'placeholder': '请输入搜索文字...'}))