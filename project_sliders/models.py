from django.db import models


def upload_image_path(instance, filename):
    final_name = f"{instance.id}-{instance.title}.jpg"
    return f"sliders/{final_name}"


class Slider(models.Model):
    img = models.ImageField(upload_to=upload_image_path,null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    button_url = models.URLField()

    def __str__(self):
        return self.title
