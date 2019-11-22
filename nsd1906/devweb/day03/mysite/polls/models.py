from django.db import models

# Create your models here.
class Question(models.Model):
    '实体类必须是models.Model的子类'
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '问题:%s' % self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __str__(self):
        return '%s=>选项:%s' % (self.question, self.choice_text)
