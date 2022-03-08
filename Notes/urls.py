from django.urls import path
from . import views
from .views import HomeView , AddNotesView , MyNotesView , DeletePostView
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('add_notes/',AddNotesView.as_view(),name="add_notes"),
    path('branch/<str:cats>',views.BranchView,name="branch"),
    path('my_notes/',MyNotesView.as_view(),name="my_notes"),
    path('notes/delete/<int:pk>',DeletePostView.as_view(),name="delete_post"),

    
]