from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(req, *args, **kwargs):
    """
    Vanilla Django Examples
    """
    # request -> HttpRequest -> django
    # request.body
    # body = req.body  # byte string of json data
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(req.GET)
    # data['headers'] = dict(req.headers)  # request.META
    # data['content_type'] = req.content_type
    # model_data = Product.objects.all().order_by('?').first()
    # data = {}
    # if model_data:
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price
    #     data = model_to_dict(model_data)
    #     # serialization
    #     # model instance (model_data)
    #     # turn a python dict
    #     # return JSON to my client
    # return JsonResponse(data)
    """
    DRF API View
    """
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance).data
    return Response(data)
