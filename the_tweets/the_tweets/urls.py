from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('login/', auth_views.LoginView.as_view(template_name='Registration/login.html', next_page='tweet_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='tweet_list'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
