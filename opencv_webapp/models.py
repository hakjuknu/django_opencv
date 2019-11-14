from django.db import models

class ImageUploadModel(models.Model):
    # blank=True : Form에서 빈 채로 저장되는 것을 허용(form.is_valid) 즉 ''저장됨
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
