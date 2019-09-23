from django.urls import path
import blog.views as views

urlpatterns = [
    path("hello_world", views.hello_world),
    path("content", views.article_content),
    path("index", views.get_index_page),
    path("detail/<int:article_id>", views.get_detail_page),
]