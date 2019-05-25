from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True, null=False)
    pub_date = models.DateTimeField()

    def __str__(self):
        return '问题: %s' % self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200, null=False)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return '%s => %s' % (self.question, self.choice_text)
