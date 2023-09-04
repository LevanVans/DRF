from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer

#alt view imports

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



#Get one item
class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    #lookup_field = 'pk'



# Post one item 
class ProductDetailCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
       
    
    def perform_create(self, serializer):
        
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get('content')

        
        
        if  content is None:
            content = "Content field was empty ! "
        
        serializer.save(content=content)


#Get List of all items
    
class ProductListApiView(generics.ListAPIView):
    
    
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer

    
    
    
# Alt View 
@api_view(["GET","POST"])
def product_alt_view(request, pk=None):
    
    if request.method == "GET":
        
        if pk is not None:
            
            
            obj = get_object_or_404(Product, pk = pk)
            
            data = ProductSerializer(obj, many=False).data
            
            return Response(data)
        
        queryset = Product.objects.all()
    
        data = ProductSerializer(queryset, many=True).data
        
        return Response(data)
    
    if request.method == "POST":
        
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            
            
            content = serializer.validated_data.get("content") or None
            
            if content is None:
                content = "This field is empty from ALT"
                
            serializer.save(content=content)
            
            return Response(serializer.data)
        
        
#Update View

class ProductUpdateApiView(generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = 'pk'
    
    def perfome_update(self, serializer):
        
        instance = serializer.save()
        
        
        
#Destroy 



class ProductDestroyApiView(generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = 'pk'
    
    def perfome_destroy(self, instance):
        
        super().perform_destroy(instance)