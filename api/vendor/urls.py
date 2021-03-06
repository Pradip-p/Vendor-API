from django.urls import path, include
from . import views
from rest_framework import routers

#creating router objects
router=routers.DefaultRouter()
router.register('vendor', views.VendorViewset, basename='vendorapi')
router.register('vendor-bank-details', views.VendorBankDetailsViewset, basename="bank")
router.register('Vender-contact-person', views.VenderContactPersonViewset, basename="contact-person")

urlpatterns=[
	path('api/', include(router.urls)),
	# path('bank/', include(router.urls)),
    path('provinces/',views.provinces_list),
    path('provinces/<provinces_number>',views.provinces_details),
    # path('vendor/', views.vendor_list),
    # path('vendor/<vendor_id>', views.vendor_details)
]