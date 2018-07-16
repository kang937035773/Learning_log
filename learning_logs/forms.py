from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic   #制作的表单依照的模型
        fields = ['text'] #表单中显示的字段
        labels = {'text':''} #为text的值赋为空，页面不显示标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        #通过forms.Textarea来修改系统的默认值
        widgets = {'text':forms.Textarea(attrs={'cols':80})} 