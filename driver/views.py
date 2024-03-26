from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import TemplateView,View

from django.contrib import messages
from my_work.models import GarbageBin,CollectionRequest,Area
from my_work.models import *
# Create your views here.


class HomePage(TemplateView):
    template_name="driver/home.html"






class SendCollectionRequestView(View):
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        area_id = request.POST.get('area_id')
        bin_id = request.POST.get('bin_id')
        
        # Assuming the request has been sent successfully
        CollectionRequest.objects.create(user=user, area_id=area_id, bin_id=bin_id)
        
        return render(request, 'registration/request.html')




class AcceptRejectRequestView(View):
    def post(self, request, request_id):
        collection_request = get_object_or_404(CollectionRequest, id=request_id)
        action = request.POST.get('action')  # 'accept' or 'reject'
        
        if action == 'accept':
            collection_request.accepted = True
            collection_request.rejected = False
        elif action == 'reject':
            collection_request.accepted = False
            collection_request.rejected = True
        
        collection_request.save()
        return redirect('home_3')  # Redirect to a list of requests for the user




def AcceptedUserListView(request):
    accepted_requests = CollectionRequest.objects.filter(status='accepted')
    return render(request, 'registration/accepted.html', {'accepted': accepted_requests})