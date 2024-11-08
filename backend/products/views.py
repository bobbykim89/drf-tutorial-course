from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send Django signal


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        # return super().perform_update(serializer)


product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        return super().perform_destroy(instance)


product_delete_view = ProductDeleteAPIView.as_view()

# class ProductListApiView(generics.ListAPIView):
#     """
#     Not gonna use this method
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# product_list_view = ProductListApiView.as_view()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, req, *args, **kwargs):  # HTTP -> GET
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(req, *args, **kwargs)
        return self.list(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):  # HTTP -> POST
        return self.create(req, *args, **kwargs)

    def perform_create(self, serializer):
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'This is a single view of doing cool stuff'
        serializer.save()


product_mixin_view = ProductMixinView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(req, pk=None, *args, **kwargs):
    method = req.method

    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':
        serializer = ProductSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)
