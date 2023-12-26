from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('add/folder/', views.CreateFolderView.as_view(), name='add_folder'),
    path('folder/detail/<slug:slug>/', views.UserFolderDetailView.as_view(), name='user_folder_detail'),
    path('upload/file-in-folder/<slug:folder_slug>/', views.FileUploadView.as_view(), name='upload_file_in_folder'),
    path('file/<slug:slug>/', views.UserFileDetailView.as_view(), name='user_file_detail'),
    path('file/decrypted/<slug:file_slug>/', views.DecryptFileView.as_view(), name='decrypt_file_view'),
]
