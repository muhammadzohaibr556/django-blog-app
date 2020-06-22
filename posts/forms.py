from django import forms
from .models import Post# new
class PostForm(forms.ModelForm): # ModelForm is new Form is old
   class Meta:# new
        model = Post # new
        fields = ['title','description','photo']#new
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Title','name':'title','required':'True'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description', 'rows':'7','name':'description'}),
            'photo': forms.FileInput(attrs={'class':'form-control-file','name':'photo', 'id':'inputfile', 'class':'filestyle', 'data-btnClass':'btn-warning','data-input':'false', 'data-text':'Change', 'onchange':'readURL(this);'})
        }