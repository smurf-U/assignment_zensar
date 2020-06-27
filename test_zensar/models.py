from django.db import models


class SoftDeleteModel(models.Model):
    class meta:
        abstract = True

    is_deleted = models.BooleanField(null=False, default=False)

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

class RouterManager(models.Model):

    sapid = models.CharField(max_length=18)
    hostname = models.CharField(max_length=14, unique=True)
    loopback = models.GenericIPAddressField(protocol='IPv4', unique=True)
    mac_address = models.CharField(max_length=17)

    def __str__(self):
        return self.hostname