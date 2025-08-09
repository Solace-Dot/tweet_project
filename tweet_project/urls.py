from django.contrib import admin
from django.urls import path
from tweet import views  # ✅ match the app name 'tweets'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_tweet, name='create_tweet'),  # Create tweet page
    path('tweets/', views.view_tweets, name='view_tweets'),  # View tweets page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
