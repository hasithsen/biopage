from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from linkpage.users.models import User


class SocialLink(models.Model):
    user_profile = models.ForeignKey(
        "UserProfile",
        on_delete=models.CASCADE,
    )
    # Foreign Key used because social_link can only have one UserProfile, but UserProfiles can have multiple social_links.
    # UserProfile as a string rather than object because it hasn't been declared yet in file.
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile} - {self.platform_name} - { self.id }"

    def get_absolute_url(self):
        return reverse("userprofiles:detail", kwargs={"pk": self.user.pk})


class UserProfile(models.Model):
    # Basic Info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilename = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Profile name can only contain alphanumeric characters and underscores",
                code="invalid_profilename",
            ),
        ],
        verbose_name="Profile handle",
    )
    display_name = models.CharField(max_length=255, default="")
    bio = models.TextField(
        blank=True,
        default="",
        verbose_name="About",
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Lives in",
    )

    # occupation Info
    occupation = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Works as",
    )

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.profilename}"

    def get_absolute_url(self):
        return reverse("userprofiles:detail", kwargs={"profilename": self.profilename})
