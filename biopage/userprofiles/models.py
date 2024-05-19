from django.db import models

from biopage.users.models import User


class SocialLink(models.Model):
    user_profile = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()

    def __str__(self):
        return self.platform_name


class UserProfile(models.Model):
    # Basic Info
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, default=user)
    bio = models.TextField(blank=True, default="")
    city = models.CharField(max_length=255, blank=True, default="")
    country = models.CharField(max_length=255, blank=True, default="")

    # occupation Info
    occupation = models.CharField(max_length=255, blank=True, default="")
    organization = models.CharField(max_length=255, blank=True, default="")

    # Social Links
    social_links = models.ManyToManyField(SocialLink, blank=True)

    # Skills and Tags
    skills = models.CharField(max_length=255, blank=True, default="")

    # Other necessary attributes
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.display_name
