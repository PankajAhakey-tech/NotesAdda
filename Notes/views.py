from dataclasses import field
from pyexpat import model
from unicodedata import category
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView  , CreateView ,DeleteView

from Notes.models import Branch , Notes
from .forms import NotesForm 
from Notes.models import Notes , Branch


class  HomeView(ListView):
    model =Notes
    template_name = "home.html"
    cats = Branch.objects.all()
    ordering = ['-id']
   
    # for catgory in navbar
    def get_context_data(self,*args, **kwargs):
        cat_menu =Branch.objects.all
        context = super(HomeView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class MyNotesView(ListView):
    # model = Notes
    model =Notes
    template_name = "my_notes.html"
    cats = Branch.objects.all()
    ordering = ['-id']
   
    

class AddNotesView(CreateView):
    model = Notes
    form_class = NotesForm
    
    template_name = 'add_notes.html'

class DeletePostView(DeleteView):
    model = Notes
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def BranchView(request,cats):
    category_post = Notes.objects.filter(branch=cats.replace('-',' '))
    return render(request,'branch.html',{'cats':cats.title().replace('-',' '),'category_post':category_post})

    