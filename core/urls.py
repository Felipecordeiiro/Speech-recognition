from django.contrib import admin
from django.urls import path
from allview import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('upload/', views.upload_audio),

]
