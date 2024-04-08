from django.urls import path
from posts import views

url patterns = [ 
    path('posts/' views.PostList.as_view()), 
    path('posts/<int:pk>/', views.PostDetail.as_view() )
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]