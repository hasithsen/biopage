from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .models import UserProfile


class UserProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserProfile
    fields = (
        "profilename",
        "profile_picture",
        "display_name",
        "bio",
        "occupation",
        "location",
        "tags",
    )
    # success_url = "/success-url/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def dispatch(self, *args, **kwargs):
    #     if UserProfile.objects.filter(user=self.request.user).exists():
    #         # Redirect to profile detail page or any other page
    #         return redirect(
    #             "userprofiles:list",
    #         )
    #     return super().dispatch(*args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        # Pre-populate profilename with username for initail userprofile
        if not UserProfile.objects.filter(user=self.request.user).exists():
            initial["profilename"] = self.request.user.username
        return initial


userprofile_create_view = UserProfileCreateView.as_view()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = (
        "profilename",
        "profile_picture",
        "display_name",
        "bio",
        "occupation",
        "location",
        "tags",
    )
    # success_url = "/success-url/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        # Get the UserProfile instance to be updated, ensuring it belongs to the current user
        return get_object_or_404(
            UserProfile,
            profilename=self.kwargs["profilename"],
            user=self.request.user,
        )


userprofile_update_view = UserProfileUpdateView.as_view()


class UserProfileDetailView(DetailView):
    model = UserProfile

    def get_object(self, queryset=None):
        # Get the UserProfile instance to be viewed
        return get_object_or_404(
            UserProfile,
            profilename=self.kwargs["profilename"],
        )


userprofile_detail_view = UserProfileDetailView.as_view()


class UserProfileListView(LoginRequiredMixin, ListView):
    model = UserProfile
    # slug_field = "username"
    # slug_url_kwarg = "username"

    def get_queryset(self):
        # Return the UserProfile objects associated with the current user
        return UserProfile.objects.filter(user=self.request.user)


userprofile_list_view = UserProfileListView.as_view()
