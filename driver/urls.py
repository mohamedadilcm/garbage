from django.contrib import admin
from django.urls import path
from driver import views

urlpatterns = [
    path("home/",views.HomePage.as_view(),name="home_3"),
    path('send-request/<int:user_id>/', views.SendCollectionRequestView.as_view(), name='send_collection_request'),
    path('accept-reject-request/<int:request_id>/', views.AcceptRejectRequestView.as_view(), name='accept_reject_request'),
    path('accepted-users/', views.AcceptedUserListView, name='accepted_user_list'),
]
