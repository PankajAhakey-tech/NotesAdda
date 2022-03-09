from django.contrib import admin
from django.urls import path , include , re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.static import serve

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('favicon\.ico', favicon_view),
    path('',include('Notes.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)