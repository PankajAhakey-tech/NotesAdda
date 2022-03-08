from dataclasses import fields
from random import choices
from django import  forms
from .models import Notes , Branch

choices = Branch.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
    choice_list.append(item)

class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ('user','subject', 'branch','description','notes')
        notes=forms.FileField()

        

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control' , 'value':'','id':'author_name','type':'hidden'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'branch': forms.Select(choices=choice_list,attrs={'class':'form-control','placeholder':choices}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        } 
 