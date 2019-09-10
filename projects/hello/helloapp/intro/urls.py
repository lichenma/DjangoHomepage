# howdy/urls.py 
from django.conf.urls import url 
from intro import views 

urlpatterns = [
    path('$', views.HomePageView.as_view()), 
]