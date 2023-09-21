from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default="avatar.jpg",
        upload_to="profile_avatars",
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)

        if img.width > 300 or img.height > 300:
            if img.width > img.height:
                new_width = max(300, img.width * 300 // img.height)
                new_height = max(300, 300)
            else:
                new_width = max(300, 300)
                new_height = max(300, img.height * 300 // img.width)

            img = img.resize((new_width, new_height))

        if not img.height == img.width:

            left = 0
            top = 0
            right = int((img.width + 300) / 2)
            bottom = int((img.height + 300) / 2)
            img = img.crop((left, top, right, bottom))


        img.save(self.avatar.path)
