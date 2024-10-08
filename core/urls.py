from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def custom_404(request, exception):
    return redirect("http://tech-echo.dev/vue/404")


handler404 = custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("teachers/", include("teachers.urls")),
    path("questions/", include("questions.urls")),
    path("users/", include("users.urls")),
    path("questions/<int:id>/answers/", include("answers.urls")),
    path("payments/", include("payments.urls")),
    path("accounts/", include("allauth.urls")),
    path("chat/", include("chat.urls")),
    path("reservations/", include("reservations.urls")),
    path("blogs/", include("blogs.urls")),
    path("editors/", include("editors.urls")),
]
