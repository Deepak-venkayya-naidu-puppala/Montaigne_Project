from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class JsonDataModel(models.Model):
    data = JSONField()

    class Meta:
        verbose_name= "JSON Datum"
        verbose_name_plural= "JSON Data"


class JSONFileUpload(models.Model):
    name = models.CharField(max_length=36)
    datafile = models.FileField(null=True,blank=True)
    def __str__(self):
        return str(self.name)

class OwnerModel(models.Model):
    owner_id = models.CharField(max_length=16)

    def __str__(self):
        return str(self.owner_id)


class CampaignModel(models.Model):
    campaign_id = models.CharField(max_length=16)
    campaign_name = models.CharField(max_length=16)

    def __str__(self):
        return str(self.campaign_name)


class URLModel(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    pa = models.IntegerField(default=0)
    da = models.IntegerField(default=0)
    owner = models.ForeignKey(OwnerModel, blank=True, null=True,on_delete=models.CASCADE)
    campaign = models.ForeignKey(CampaignModel, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
