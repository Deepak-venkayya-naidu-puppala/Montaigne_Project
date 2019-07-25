from django.contrib import admin
from .models import JsonDataModel, JSONFileUpload,OwnerModel,CampaignModel, URLModel  

# Register your models here.

admin.site.register(JsonDataModel)

admin.site.register(JSONFileUpload)

admin.site.register(OwnerModel)
admin.site.register(CampaignModel)

admin.site.register(URLModel)