from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [ 
    path('article/', views.article_create),
    path('article/<int:user_id>/<int:page_idx>/', views.article_list),
    path('article/<int:article_id>/delete/', views.article_delete),
    path('user/', views.user_signup),
    path('user/<int:user_id>/', views.user_signout_and_update),
]
