from django import forms
from .models import Question, Profile


class AskForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField()

    # author = Profile.objects.get(id=0)

    title.widget.attrs.update({'class': 'form-control', 'placeholder': 'title'})
    body.widget.attrs.update({'class': 'form-control', 'placeholder': 'enter your question'})

    def save(self):
        new_question = Question.objects.create(
            title=sefl.cleaned_data['title'],
            slug=self.cleaned_data['slug'],
            author=author
        )
        return new_question