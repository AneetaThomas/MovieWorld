from django import forms
from app1.models import MovieWorldModel
class MovieForm(forms.ModelForm):
    class Meta:
        model=MovieWorldModel

        fields=['title','description','year','image','language']