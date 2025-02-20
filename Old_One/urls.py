from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="Home"),
    path("About",views.About, name="About"),
    path("Contact",views.Contact, name="Contact"),
    path("projects/",views.project_list, name="project_list"),
    path("project_detail/<slug:slug>/",views.project_detail, name="project_detail"),
    path("Management",views.Management,name="Management"),
    path("Services",views.Services,name="Services"),
    path("Clients",views.Clients,name="Clients"),
    path("Achievements",views.Affiliations,name="Achievements"),
    path("Jobs",views.Jobs,name="Jobs")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)