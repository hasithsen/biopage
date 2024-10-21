from django.urls import path

from .views import userprofile_create_view
from .views import userprofile_detail_view
from .views import userprofile_list_view
from .views import userprofile_update_view

app_name = "userprofiles"
urlpatterns = [
    path(
        "profiles/~create/",
        view=userprofile_create_view,
        name="create",
    ),
    path(
        "profiles/~update/<str:profilename>",
        view=userprofile_update_view,
        name="update",
    ),
    path(
        "profiles/",
        view=userprofile_list_view,
        name="list",
    ),
    path(
        "<str:profilename>/",
        view=userprofile_detail_view,
        name="detail",
    ),
]
