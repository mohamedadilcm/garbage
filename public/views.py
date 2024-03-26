from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,View,CreateView
from public.forms import UserGarbageBinForm,ComplaintForm,AddLocation
from my_work.models import Area, UserGarbageBin,Complaint, UserArea
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.



class HomePage(TemplateView):
    template_name="public/home.html"




class RequestBin(CreateView):
    template_name='public/bin_request.html'
    form_class=UserGarbageBinForm
    model=UserGarbageBin
    success_url=reverse_lazy('home_2')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    

# class CustmoerComplaint(CreateView):
#     template_name='public/complaint.html'
#     form_class=ComplaintForm
#     model=Complaint
#     success_url=reverse_lazy('home_2')
    
    
    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)
              

class PendingRequestsView(View):
    def get(self, request):
        pending_requests = UserGarbageBin.objects.filter(status='pending')
        return render(request, "public/request_details.html", {"pending_requests": pending_requests})

class AcceptRequestView(View):
    def post(self, request, pk):
        user_garbage_bin = get_object_or_404(UserGarbageBin, pk=pk)
        user_garbage_bin.status = 'accepted'
        user_garbage_bin.save()   
        return redirect('pending_requests')

class RejectRequestView(View):
    def post(self, request, pk):
        user_garbage_bin = get_object_or_404(UserGarbageBin, pk=pk)
        user_garbage_bin.status = 'rejected'
        user_garbage_bin.save()
        return redirect('pending_requests')
    
def pending_requests_view(request):
    pending_requests = UserGarbageBin.objects.filter(status='pending')
    return render(request, 'public/pending_requests.html', {'pending_requests': pending_requests})



class AddLocationView(CreateView):
    template_name='public/location.html'
    form_class=AddLocation
    model=UserArea
    success_url=reverse_lazy('home_2')
    areas = Area.objects.all()

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    





# @login_required
def send_complaint(request):
    if request.method == 'POST':
        issue = request.POST.get('issue', '')
        if issue:
            complaint = Complaint.objects.create(user=request.user, issue=issue)
            messages.success(request, 'Complaint sent successfully!')
            return redirect('home_2')  # You can redirect to a success page
        else:
            messages.error(request, 'Please provide an issue for the complaint.')
    return render(request, 'public/send_complaint.html')  # Render a template with a form for sending complaints

# @login_required
def view_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.user == complaint.user:  # Ensure only the user who sent the complaint can view it
        return render(request, 'public/view_complaint.html', {'complaint': complaint})
    else:
        messages.error(request, 'You are not authorized to view this complaint.')
        return redirect('home_2')  # Redirect to home or another appropriate page

# @login_required
def accept_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == 'POST':
        complaint.accepted = True
        complaint.save()
        messages.success(request, 'Complaint accepted successfully!')
        return redirect('home_2')  # Redirect to home or another appropriate page
    return render(request, 'public/accept_complaint.html', {'complaint': complaint})

# @login_required
def reject_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == 'POST':
        complaint.rejected = True
        complaint.save()
        messages.success(request, 'Complaint rejected successfully!')
        return redirect('home_2')  # Redirect to home or another appropriate page
    return render(request, 'public/reject_complaint.html', {'complaint': complaint})



def list_complaints(request):
    user_complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'public/list_complaints.html', {'user_complaints': user_complaints})


    












