from .views import CategoryViewSet, PostViewSet
from rest_framework import routers

app_name = 'blog'

router = routers.SimpleRouter()

router.register("blog-category", CategoryViewSet)
router.register("blog-post", PostViewSet)

urlpatterns = router.urls


