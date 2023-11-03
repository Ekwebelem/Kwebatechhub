from django import forms

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)


	# forms.py

from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'pdf_file']  # Include other fields




######################
# forms.py

from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'phone_number', 'cover_letter', 'cv', 'email']

	#cv = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf'}))  # Add this line



# forms.py

from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'subject', 'message']
