from django.shortcuts import render, get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filters import ProductsFilter
from .serializers import ProductSrializer
from rest_framework.pagination import PageNumberPagination

from product.models import Product

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    total = filterset.qs.count()
    resPage =2
    paginator = PageNumberPagination()
    paginator.page_size = resPage
    products = Product.objects.all()
    #serializer = ProductSrializer(products,many=True)
    queryset = paginator.paginate_queryset(filterset.qs,request)
    serializer = ProductSrializer(products,many=True)
    #print(serializer)
    return Response({"Products": serializer.data ,"par page" :resPage, 'total': total})



@api_view(['GET'])
def get_by_id_products(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSrializer(product, many=False)
    print(product)
    return Response({'Product': serializer.data})
