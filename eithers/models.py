from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=20)
    issue_a = models.CharField(max_length=20)
    issue_b = models.CharField(max_length=20)
    image_a = ProcessedImageField(
        processors=[Thumbnail(200, 300)],   # 처리할 작업 목록
        format='JPEG',   # 저장 포맷
        options={'quality': 90},    # 추가 옵션들
        upload_to='eithers/images',    # 저장 위치(MEDIA_ROOT/article/images)
    )
    image_b = ProcessedImageField(
        processors=[Thumbnail(200, 300)],   # 처리할 작업 목록
        format='JPEG',   # 저장 포맷
        options={'quality': 90},    # 추가 옵션들
        upload_to='eithers/images',    # 저장 위치(MEDIA_ROOT/article/images)
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) # articles/10/
        return reverse('question:detail', kwargs={'question_pk': self.pk}) # articles/10/
       

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'Question({self.question_id}): Answer({self.pk})-{self.comment}'
    