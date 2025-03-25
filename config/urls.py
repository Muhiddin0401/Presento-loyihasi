from django.contrib import admin
from django.urls import path, include
from configapp.views import *
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', custom_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('admin/messages/', admin_messages, name='admin_messages'),  # admin.site.urls dan oldin
    path('admin/messages/answer/<int:message_id>/', answer_message, name='answer_message'),  # admin.site.urls dan oldin
    path('admin/', admin.site.urls),  # Oxirida joylashishi kerak
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)