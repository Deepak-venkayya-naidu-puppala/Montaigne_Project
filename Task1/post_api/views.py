from django.shortcuts import render
from rest_framework.views import APIView
import json 
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import PostJSONDataSerializer, GetJsonDataSerializer
from .models import JSONFileUpload, JsonDataModel, OwnerModel, CampaignModel, URLModel
from rest_framework.response import Response
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import generics
from django.http import JsonResponse

def store_json_data():

    
        json_file = JSONFileUpload.objects.all().values()[0]
        name = json_file["datafile"]
        obj = settings.MEDIA_ROOT + '\\' + name
        with open(obj) as data_file:
            json_obj = json.load(data_file)
        obj = JsonDataModel(data=json_obj)
        obj.save()
        JSONFileUpload.objects.all().delete()
        

    
class JsonAPICreateView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = PostJSONDataSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            store_json_data()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OwnerAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        obj = JsonDataModel.objects.first().data
        obj = obj["data"]["owner_id"]
        model = OwnerModel(owner_id = obj)
        model.save()

        return Response(obj, status=status.HTTP_201_CREATED)

        
class CampaigneAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        obj = JsonDataModel.objects.first().data
        key = list(obj["data"]["campaign"].keys())[0]
        name = obj["data"]["campaign"][list(obj["data"]["campaign"].keys())[0]]["campaigne_name"]
        model = CampaignModel(campaign_id=key, campaign_name=name)
        model.save()

        return Response(obj, status=status.HTTP_201_CREATED)

        
class URLAPIView(APIView):

    def post(self, request, *args, **kwargs):
        obj = JsonDataModel.objects.first().data
        owner_id = obj["data"]["owner_id"]
        key = list(obj["data"]["campaign"].keys())[0]
        campaigne = obj["data"]["campaign"][list(obj["data"]["campaign"].keys())[0]]["campaigne_name"]
        url_keys = list(obj["data"]["campaign"][key]["url"].keys())
        
        for i in url_keys:
            print(i)
            try :
                keys_second = obj["data"]["campaign"]["146"]["url"][i]["backlink_data"]["follow"].keys()
            except:
                continue
            for j in keys_second:
                local_obj = obj["data"]["campaign"]["146"]["url"][i]["backlink_data"]["follow"][j]
                url = j
                pa = local_obj["pa"]
                da = local_obj["da"]
                model = URLModel(url=url, pa=pa, da=da, owner=OwnerModel.objects.get(owner_id=owner_id), campaign=CampaignModel.objects.get(campaign_name=campaigne))
                model.save()

        return Response("Url Table sucessfully created", status=status.HTTP_201_CREATED)



class GetURLDetailsView(APIView):

    def get(self, request):
        owner_id = request.POST["owner_id"]
        campaigne_id = request.POST["campaigne_id"]
        owner_value = OwnerModel.objects.filter(owner_id=owner_id).values()[0]["owner_id"]
        campaigne_value = CampaignModel.objects.filter(campaign_id=campaigne_id).values()[0]["campaign_name"]
        json_dict = {
            "owner_id": owner_value,
            "campaigne": campaigne_value,
            "campaign_id": { campaigne_value:[]
            }

        }
        UrlObject = list(URLModel.objects.filter(owner=OwnerModel.objects.get(id=1), campaign=CampaignModel.objects.get(campaign_name="URLs")).values())

        for i  in UrlObject:
            json_tmp = {
                "url_name":i["url"],
                "pa": i["pa"],
                "da": i["da"]
            }
            json_dict["campaign_id"][campaigne_value].append(json_tmp)
        return JsonResponse(json_dict)

        


