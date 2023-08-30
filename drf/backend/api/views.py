from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

def api_home(request):
    
    from products.models import Product
    
    model_data = Product.objects.all().order_by("?").first()
    
    data = {}
    
    if model_data:
        data = model_to_dict(model_data, fields=["id","title"])


    return  JsonResponse(data)
    
