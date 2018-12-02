import env
from polls.models import Choice, Question

print(Question.objects.all())

print(Choice.objects.all())

q = Question.objects.get(pk=1)