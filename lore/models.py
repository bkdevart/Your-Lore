from django.db import models

class Lore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    story = models.TextField()
    group = models.ManyToManyField('auth.group', related_name='lore')
    owner = models.ForeignKey('auth.user', related_name='lore', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']