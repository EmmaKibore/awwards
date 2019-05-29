from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^accounts/profile/$', views.profile, name = 'profile'),
    url(r"^search/",views.search,name="search"),
]     
