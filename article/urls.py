from django.urls import path

from . import views
app_name = 'article'
urlpatterns = [
    path('article_list/', views.article_list, name= 'article_list'),
    path('index/', views.article_index, name = "index"),
    path('article_detail/<int:id>/', views.article_detail, name = 'article_detail'),
    path('article_create/', views.article_create, name = 'article_create'),
    path('article_safe_delete/<int:id>/', views.article_safe_delete, name = 'article_safe_delete'),
    path('article_update/<int:id>/', views.article_update, name = 'article_update'),
    path('increase_likes/<int:id>/', views.IncreaseLikesView.as_view(), name = 'increase_likes')
]