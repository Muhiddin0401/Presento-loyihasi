from django.contrib import admin
from django.urls import path, include
from configapp.views import *
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = 'home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name = 'signup'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('messages/', admin_messages, name = 'admin_messages'),
    path('messages/answer/<int:message_id>/', answer_message, name = 'answer_message')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)