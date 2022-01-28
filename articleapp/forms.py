from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-start',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    # 테스트 확인중인 부분
    image = forms.FileInput(attrs={'accept' : 'image/*'})

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']