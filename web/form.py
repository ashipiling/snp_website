from django import forms

class FileForm(forms.Form):
    file_name = forms.FileField(label=u"用例文件")

