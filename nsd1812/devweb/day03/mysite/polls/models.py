from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True, null=False)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '问题: %s' % self.question_text
