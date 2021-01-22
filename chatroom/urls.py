from django.contrib import admin
from django.urls import path
from chatweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sign_in, name="home"),
    path('main_page.html', views.start_chat, name='chat_start'),
    path('chat_page.html', views.send_msg, name='sending'),
]
