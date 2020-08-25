from . import views 
from django.urls import path
urlpatterns = [
    path('',views.upload,name="upload"),
    path('upload/',views.upload_csv,name='upload_csv'),
    path('upload_list/',views.file_list,name="files_list"),
]
