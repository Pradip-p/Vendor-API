from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vendor.serializers import *
from vendor. models import *
from rest_framework import status



####details of provinces

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def provinces_list(request):
    if request.method=='GET':
        obj=Provinces.objects.all()
        serializer_class=ProvincesSerializers(obj,many=True)
        return Response(serializer_class.data)
    elif request.method=='POST':
        serializer_class=ProvincesSerializers(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def  provinces_details(request,provinces_number):
    try:
        obj=Provinces.objects.filter(provinces_number=provinces_number)
        
    except Provinces.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    serializer_class=ProvincesSerializers(obj, many=True)
    return Response(serializer_class.data)


#### details of vendor


# @permission_classes([IsAuthenticated])
class VendorViewset(viewsets.ModelViewSet):
    
    def list(self, request):
        print("********List********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        queryset = Vendor.objects.all()
        serializer_class = VendorSerializers(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        print("********Retrieve********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk

        if id is not None:
            vendor = Vendor.objects.get(pk=id)
            serializer_class = VendorSerializers(vendor)
            return Response(serializer_class.data)

    def  create(self, request):
        print("********Create********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        serializer_class = VendorSerializers(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Data Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,pk, request):
        print("********Update********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        id=pk
        vendor = Vendor.objects.get(pk=id)
        serializer_class = VendorSerializers(vendor, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Data Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,pk, request):
        print("********Partial Update********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        id=pk
        vendor = Vendor.objects.get(pk=id)
        serializer_class = VendorSerializers(vendor, data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Partial Data Created"})

        return Response(serializer_class.errors)

    def destory(self,request,pk):
        print("********Delete********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        vendor = Vendor.objects.get(pk=id)
        vendor.delete()
        return  Response({"msg":"Data deleted"})

### VendorBankDetails

# @permission_classes([IsAuthenticated])
class VendorBankDetailsViewset(viewsets.ModelViewSet):
    
    def list(self, request):
        print("********List********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        queryset = VendorBankDetails.objects.all()
        serializer_class = VendorBankDetailsSerizers(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        print("********Retrieve********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        id = pk
        if id is not None:
            vendor = VendorBankDetails.objects.get(pk=id)
            # vendor=Vendor.objects.all().prefetch_related().filter(pk=id)
            serializer_class = VendorBankDetailsSerizers(vendor)
            return Response(serializer_class.data)
        
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def  create(self, request):
        print("********Create********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        serializer_class = VendorBankDetailsSerizers(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Data Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,pk, request):
        print("********Update********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        id=pk
        vendor = VendorBankDetails.objects.get(pk=id)
        serializer_class = VendorBankDetailsSerizers(vendor, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Data Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,pk, request):
        print("********Partial Update********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        id=pk
        vendor = VendorBankDetails.objects.get(pk=id)
        serializer_class = VendorBankDetailsSerizers(vendor, data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Partial Data Created"})

        return Response(serializer_class.errors)

    def destory(self,request,pk):
        print("********Delete********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        
        id = pk
        vendor = VendorBankDetails.objects.get(pk=id)
        vendor.delete()
        return  Response({"msg":"Data deleted"})


#### detailsof contact person

# @permission_classes([IsAuthenticated])
class VenderContactPersonViewset(viewsets.ModelViewSet):
    
    def list(self, request):
        print("********List********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        queryset = VenderContactPerson.objects.all()
        serializer_class = VenderContactPersonSerizers(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        print("********Retrieve********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        id = pk
        if id is not None:
            vendor = VenderContactPerson.objects.get(pk=id)
            serializer_class = VenderContactPersonSerizers(vendor)
            return Response(serializer_class.data)

    def  create(self, request):
        print("********Create********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        serializer_class = VenderContactPersonSerizers(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Data Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,pk, request):
        print("********Update********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)

        id=pk
        vendor = VenderContactPerson.objects.get(pk=id)
        serializer_class = VenderContactPersonSerizers(vendor, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Data Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,pk, request):
        print("********Partial Update********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        id=pk
        vendor = VenderContactPerson.objects.get(pk=id)
        serializer_class = VenderContactPersonSerizers(vendor, data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({"msg":"Partial Data Created"})

        return Response(serializer_class.errors)

    def destory(self,request,pk):
        print("********Delete********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Name:", self.name)
        print("Description:", self.description)
        
        id = pk
        vendor = VenderContactPerson.objects.get(pk=id)
        vendor.delete()
        return  Response({"msg":"Data deleted"})
