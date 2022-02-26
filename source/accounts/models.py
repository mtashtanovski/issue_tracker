from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name="profile",
        verbose_name="Профиль",
        on_delete=models.CASCADE,
    )

    birth_date = models.DateField(
        null=True,
        blank=False,
        verbose_name="Дата рождения",
    )

    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to="avatars/",
        null=True,
        blank=False
    )

    git_profile = models.URLField(
        null=True,
        blank=False,
        max_length=128,
        verbose_name="Профиль GitHub"
    )

    about_me = models.TextField(
        max_length=2000,
        null=True,
        blank=False,
        verbose_name="О себе")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.username + "'s Profile"
