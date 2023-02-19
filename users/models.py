from django.db import models
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture" Timestamp 1:33
from django.contrib.auth.models import User
# Code derived from "Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile" Timestamp 19:04
from PIL import Image

# Code derived from "Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture" Timestamp 1:51
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Code derived from "Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile" Timestamp 17:56, 19:28
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



