from django.contrib import admin
from django.urls import path
from public import views

urlpatterns = [
    path("home/",views.HomePage.as_view(),name="home_2"), 
    path("request_bin/",views.RequestBin.as_view(),name="request_bin"),
    # path("complaint/",views.CustmoerComplaint.as_view(),name="c_omplaint"),
    path('pending-requests/', views.PendingRequestsView.as_view(), name='requests'),
    path('accept-request/<int:pk>/', views.AcceptRequestView.as_view(), name='accept_request'),
    path('reject-request/<int:pk>/', views.RejectRequestView.as_view(), name='reject_request'),
    path('pending-re/', views.pending_requests_view, name='pending_requests'),
    path("add_location/",views.AddLocationView.as_view(),name="location_add"),
    path('send/', views.send_complaint, name='send_complaint'),
    path('complaint/<int:complaint_id>/', views.view_complaint, name='view_complaint'),
    path('complaint/<int:complaint_id>/accept/', views.accept_complaint, name='accept_complaint'),
    path('complaint/<int:complaint_id>/reject/', views.reject_complaint, name='reject_complaint'),
    path('complaint_list/', views.list_complaints, name='list_complaints')
]
   

