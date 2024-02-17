from django import forms

from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        exclude = ('user',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }

    
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         # fields = '__all__'
#         exclude = ('blog',)
        
