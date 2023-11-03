from django.contrib import admin

from .models import    Contact

# Register your models here.

admin.site.register(Contact)


# admin.py

from .models import UploadedPDF

@admin.register(UploadedPDF)
class UploadedPDFAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'upload_date')



# admin.py

from django.contrib import admin
from .models import Application

admin.site.register(Application)


# admin.py

from django.contrib import admin
from .models import JobApplication

admin.site.register(JobApplication)


# admin.py

from django.contrib import admin
from .models import ContactSubmission

admin.site.register(ContactSubmission)
