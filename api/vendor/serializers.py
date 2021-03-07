from vendor.models import Provinces, Vendor, VendorBankDetails, VenderContactPerson
from rest_framework import serializers



class ProvincesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Provinces
        fields='__all__'

class VendorSerializers(serializers.ModelSerializer):
	"""docstring for ClassName"""
	provinces = serializers.StringRelatedField()

	class Meta():
		"""docstring for ClassName"""
		model = Vendor
		fields = '__all__'

class VendorBankDetailsSerizers(serializers.ModelSerializer):
	vendor = serializers.StringRelatedField()
	class Meta:
		model =  VendorBankDetails
		fields = ['id','name_of_branch','branch_address','type_of_account','vendor']

class VenderContactPersonSerizers(serializers.ModelSerializer):
	vendor = serializers.StringRelatedField()
	class Meta:
		model = VenderContactPerson
		fields = '__all__'
	
		