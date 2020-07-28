from django import forms

from .models import Student

'''class StudentForm(forms.Form):
    name = forms.CharField(label='姓名',max_length=128)
    sex = forms.ChoiceField(label='性别',choices=Student.SEX_ITEMS)
    professions = forms.CharField(label='职业',max_length=128)
    email = forms.EmailField(label='邮箱',max_length=128)
    qq = forms.CharField(lable='QQ',max_length=128)
    phone = forms.CharField(lable='手机',max_length=128)'''

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)
    class Meta:
        model = Student
        fields = {
            'name','sex','profession',
            'email','qq','phone','status'
        }