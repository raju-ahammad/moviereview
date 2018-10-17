from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('home', views.HomepageView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailPageView.as_view(), name='detail'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('genera/<int:pk>', views.MovieGeneraView.as_view(), name='genera'),
    path('actor/<int:pk>', views.ActorView.as_view(), name='actor'),
    path('cat', views.CatView.as_view(), name='cat'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('director/<int:pk>', views.DirectorView.as_view(), name='director'),




]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
