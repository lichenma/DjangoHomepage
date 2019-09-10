# howdy/urls.py 
from django.conf.urls import url 
from intro import views 

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()), 
]