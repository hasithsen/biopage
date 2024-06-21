from django.urls import path

from .views import userprofile_create_view
from .views import userprofile_detail_view
from .views import userprofile_list_view
from .views import userprofile_update_view

app_name = "userprofiles"
urlpatterns = [
    path(
        "userprofiles/~create/",
        view=userprofile_create_view,
        name="create",
    ),
    path(
        "userprofiles/~update/<int:pk>",
        view=userprofile_update_view,
        name="update",
    ),
    path(
        "<int:pk>/",
        view=userprofile_detail_view,
        name="detail",
    ),
    path(
        "userprofiles/",
        view=userprofile_list_view,
        name="list",
    ),
]
