from vendor.models import Provinces, Vendor, VendorBankDetails, VenderContactPerson
from rest_framework import serializers



class ProvincesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Provinces
        fields='__all__'

class VendorSerializers(serializers.ModelSerializer):
	"""docstring for ClassName"""

	class Meta():
		"""docstring for ClassName"""
		model = Vendor
		fields = '__all__'

class VendorBankDetailsSerizers(serializers.ModelSerializer):
	class Meta:
		model =  VendorBankDetails
		fields = '__all__'

class VenderContactPersonSerizers(serializers.ModelSerializer):
	class Meta:
		model = VenderContactPerson
		fields = '__all__'
	
		