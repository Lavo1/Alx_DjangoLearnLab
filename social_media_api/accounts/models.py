from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,   # A follows B ≠ B follows A
        related_name="followers",
        blank=True
    )

    def __str__(self):
        return self.username
    
    
    def follow(self, user):
        """Follow another user."""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user."""
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        """Check if following a user."""
        return self.following.filter(id=user.id).exists()