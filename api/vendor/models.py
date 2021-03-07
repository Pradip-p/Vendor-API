from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Provinces(models.Model):
    provinces_number = models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
	provinces = models.ForeignKey(Provinces, on_delete=models.CASCADE)
	vendor_id = models.CharField(max_length=20)
	vendor_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	telephone = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, null=True, blank=True)
	fax_no = models.CharField(max_length=100, null=True, blank=True)
	create_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	owner_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	type_of_business = models.CharField(max_length=100)
	year_of_establishment = models.CharField(max_length=100)
	vat_number = models.CharField(max_length=100)
	pan_number = models.CharField(max_length=100)
	service_tax_reg_number = models.CharField(max_length=100)
	

	def __str__(self):
		return self.vendor_name


class VenderContactPerson(models.Model):
	vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, null=True)
	name_of_contact_person = models.CharField(max_length=100)
	designation =models.CharField(max_length=100)
	mobile_number = models.CharField(max_length= 100)
	email_id = models.EmailField(max_length=200, null=True, blank=True)
	
	def __str__(self):
		return self.name_of_contact_person



class VendorBankDetails(models.Model):
	vendor = models.OneToOneField(Vendor,on_delete=models.CASCADE, null=False)
	name_of_branch = models.CharField(max_length=200)
	branch_address = models.CharField(max_length=200)
	type_of_account = models.CharField(max_length=200)
	bank_branch_ifsc_code = models.CharField(max_length=200)
	bank_name = models.CharField(max_length=100)
	account_holder_name = models.CharField(max_length=100)

	def __str__(self):
		return self.name_of_branch
		






