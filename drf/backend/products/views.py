from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer

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

    