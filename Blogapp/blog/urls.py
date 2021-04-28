from django.urls import path
#from . import views
from .views import HomeView, HomeDetailView

urlpatterns = [
    #path('', views.home, name="home"),
    path('post/<int:pk>/', HomeDetailView, name='post_detail'),
    path('', HomeView.as_view(), name="home"),
]
