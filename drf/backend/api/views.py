from django.http import JsonResponse, HttpResponse
import json

def api_home(request):
    
    from products.models import Product
    
    model_data = Product.objects.all().order_by("?").first()
    
    data = {}
    
    if model_data:
        data["title"] = model_data.title
        data["content"] = model_data.content
        data['price'] = model_data.price
    
    
    return JsonResponse(data)