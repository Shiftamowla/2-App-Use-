from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('BlogPost/', BlogPost, name='BlogPost'),
    path('NewsPost/', NewsPost, name='NewsPost'),
    path('AddNews/', AddNews, name='AddNews'),
    path('AddBlog/', AddBlog, name='AddBlog'),
    path('blogtable/', blogtable, name='blogtable'),
    path('Newstable/', Newstable, name='Newstable'),
    path('viewnews/<int:id>', viewnews, name='viewnews'),
    path('viewblog/<int:id>', viewblog, name='viewblog'),
    path('deletenews/<int:id>', deletenews, name='deletenews'),
    path('deleteblog/<int:id>', deleteblog, name='deleteblog'),
    path('search/', search, name='search'),
    path('searchblog/', searchblog, name='searchblog'),
    path('updateprofile/<int:id>', updateprofile, name='updateprofile'),
    path('Profile/', Profile, name='Profile'),
    path('base/', base, name='base'),
    path('', loginpage, name='loginpage'),
    path('password_change', password_change, name='password_change'),
    path('registerpage/', registerpage, name='registerpage'),
    path('logoutpage/', logoutpage, name='logoutpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
