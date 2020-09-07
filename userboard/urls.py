from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:post_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<int:post_id>/', views.update, name="update"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]