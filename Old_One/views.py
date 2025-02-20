from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import ContactSubmission,Job,Client,TimelineItem,Project

def home(request):
    return render(request, "base.html")

def About(request):
    return render(request,"About_Us.html")

def project_detail(request,slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request,"project_detail.html",{'project':project})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html',{'projects':projects})

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        ContactSubmission.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            message=message
        )
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Thank you for your submission!'})
        return HttpResponse('Thank you for your submission!')
    return render(request, "Contact_Us.html")

def Management(request):
    timeline_items = TimelineItem.objects.all()
    return render(request,"Management.html",{'timeline_items':timeline_items})

def Services(request):
    return render(request,"Services.html")

def Clients(request):
    public_clients = Client.objects.filter(client_type='public')
    private_clients = Client.objects.filter(client_type='private')
    context = {'public_clients':public_clients,'private_clients':private_clients}
    return render(request,"Clients.html",context)

def Affiliations(request):
    return render(request,"Achievements.html")

def Jobs(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request,"Carrers.html",{'jobs':jobs})