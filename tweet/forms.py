from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'What\'s happening?'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        forbidden_words = ['shit', 'fuck', 'bobo']
        for word in forbidden_words:
            if word.lower() in content.lower():
                raise forms.ValidationError("Your tweet contains prohibited words.")
        return content
