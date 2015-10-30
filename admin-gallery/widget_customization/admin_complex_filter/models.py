from django.db import models

# Create your models here.


class Item(models.Model):
    item_id = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
    price = models.IntegerField(null=True)
    special = models.CharField(max_length=30, blank=True)
    notes = models.CharField(max_length=400, blank=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return u"({id}) {title}".format(id=self.item_id, title=self.title)
