from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.MenuItemsView.as_view()),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
    # path('ratings', views.RatingsView.as_view()),
]