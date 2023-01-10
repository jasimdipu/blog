from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        "api/user_accounts/", include(("users.urls", "users"))
    ),
    re_path(
        "api/blog", include(("blog.urls", "blog"))
    ),
    path("api/v1/schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path(
        "api/v1/schema/swagger-ui/", SpectacularSwaggerView.as_view(), name="swagger-ui"
    ),
    path("api/v1/schema/redoc/", SpectacularRedocView.as_view(), name="redoc"),
    path("api/blog/", SpectacularRedocView.as_view(), name="redoc"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)