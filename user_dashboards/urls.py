from BI.decorators import login_required
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^find_mechanic/$', login_required(views.ListMechanic.as_view())),
    url(r'^hire_mechanic/(?P<mech_id>\d+)/$', login_required(views.HireMechanic.as_view())),
    url(r'^close_ticket/$', login_required(views.CloseTicket.as_view())),
    url(r'^approve_cancel_appointment/$', login_required(views.ApproveCancelAppointment.as_view())),
    # url(r'^receipts/$', login_required(views.Receipts.as_view())),
    # url(r'^receipts/delete_receipt/$', login_required(views.DeleteReceipt.as_view())),
    # url(r'^receipts/create_receipt/$', login_required(views.CreateReceipt.as_view())),
    # url(r'^receipt_details/(?P<receipt_id>\d+)/$', login_required(views.ReceiptDetails.as_view())),
    # url(r'^export_receipt/$', login_required(views.ExportReceipt.as_view())),
    # url(r'^receipts/remove_product/$', login_required(views.RemoveProduct.as_view())),
    # url(r'^receipts/add_receipt_product/$', login_required(views.AddProduct.as_view())),
    #
    # url(r'^list_products/$', login_required(views.ListProducts.as_view())),
    # url(r'^create_product/$', login_required(views.CreateProducts.as_view())),
    #
    # url(r'^list_customers/$', login_required(views.ListCustomer.as_view())),
    # url(r'^customer/create_customer/$', login_required(views.CreateCustomer.as_view())),
    # url(r'^customer/delete_customer/$', login_required(views.DeleteCustomer.as_view())),
]