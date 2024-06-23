from django.contrib.auth.mixins import LoginRequiredMixin
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

    def dispatch(self, *args, **kwargs):
        if UserProfile.objects.filter(user=self.request.user).exists():
            # Redirect to profile detail page or any other page
            return redirect(
                "userprofiles:update",
                pk=self.request.user.userprofile.pk,
            )
        return super().dispatch(*args, **kwargs)


userprofile_create_view = UserProfileCreateView.as_view()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = (
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


userprofile_update_view = UserProfileUpdateView.as_view()


class UserProfileDetailView(DetailView):
    model = UserProfile


userprofile_detail_view = UserProfileDetailView.as_view()


class UserProfileListView(LoginRequiredMixin, ListView):
    model = UserProfile
    slug_field = "username"
    slug_url_kwarg = "username"


userprofile_list_view = UserProfileListView.as_view()
