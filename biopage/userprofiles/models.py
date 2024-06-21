from django.db import models
from django.urls import reverse

from biopage.users.models import User


class SocialLink(models.Model):
    user_profile = models.ForeignKey(
        "UserProfile",
        on_delete=models.CASCADE,
    )
    # Foreign Key used because social_link can only have one UserProfile, but UserProfiles can have multiple social_links.
    # UserProfile as a string rather than object because it hasn't been declared yet in file.
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()

    def __str__(self):
        return f"{self.user_profile} - {self.platform_name}"

    def get_absolute_url(self):
        return reverse("userprofiles:detail", kwargs={"pk": self.user.pk})


class UserProfile(models.Model):
    # Basic Info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, default="")
    bio = models.TextField(blank=True, default="")
    city = models.CharField(max_length=255, blank=True, default="")
    country = models.CharField(max_length=255, blank=True, default="")

    # occupation Info
    occupation = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Wroks as",
    )
    organization = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Workplace",
    )

    # Social Links
    # social_links = models.ManyToManyField(SocialLink, blank=True)
    # social_links = models.ForeignKey(SocialLink, on_delete=models.CASCADE)

    # Tags
    tags = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Interests",
        help_text="Enter interests as a comma-separated list (e.g., Camping, Technology, History).",
    )

    # Other necessary attributes
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("userprofiles:detail", kwargs={"pk": self.pk})
