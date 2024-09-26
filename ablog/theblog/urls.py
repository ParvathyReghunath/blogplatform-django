from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView
# #for displaying hello world
# urlpatterns = [  
#     path('',views.home, name='home'),
# ]

#adding blog posts to webpage
urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('abstract/<int:pk>',ArticleDetailView.as_view(),name="article_detail" ),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('update_post/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('delete_post/<int:pk>',DeletePostView.as_view(),name="delete_post"),
]