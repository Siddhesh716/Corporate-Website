from django.contrib import admin
from .models import ContactSubmission,Job,Client,TimelineItem,Project

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'submitted_at')
    search_fields = ('name', 'email', 'mobile')
    list_filter = ('submitted_at',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date_posted', 'is_active')
    search_fields = ('title', 'description', 'location')
    list_filter = ('is_active',)
    ordering = ('-date_posted',)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_type', 'image', 'description')
    list_filter = ('client_type',)
    search_fields = ('name',)
admin.site.register(Client, ClientAdmin)

@admin.register(TimelineItem)
class TimelineItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'left_placeholder', 'right_placeholder')
    list_filter = ('position',)
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'additional_description', 'image', 'position', 'left_placeholder', 'right_placeholder')

admin.site.register(Project)