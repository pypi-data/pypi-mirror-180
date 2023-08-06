from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from medux.common.views import LoginView

# namespaced URLs
app_name = "common"

# URLs namespaced  under common/
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
]


# global URLs
root_urlpatterns = [
    path(
        "accounts/login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "accounts/logout/",
        LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
]

if settings.DEBUG:
    root_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
