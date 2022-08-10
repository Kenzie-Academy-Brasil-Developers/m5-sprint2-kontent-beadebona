from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=50, null=False)
    module = models.TextField(null=False, blank=False)
    students = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(blank=True, default=False)

    def __repr__(self) -> str:
        representation = f"<[{self.id}] {self.title} - {self.module}>"
        return representation
