from django.urls import path
from .views import PostList, PostDetail, CategoryList, CategoryDetail

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('category', CategoryList.as_view(), name='categorylistcreate'),
    path('category-details', CategoryDetail.as_view(), name='categorydetails'),
]