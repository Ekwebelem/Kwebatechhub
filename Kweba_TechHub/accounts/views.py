from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

#new
from django.core.files.storage import FileSystemStorage
from .models import UploadedPDF


# Create your views here.
def home(request):

        return render(request, 'index.html')
# @login_required
def about(request):
    return render(request, 'about.html')

def softwaredev(request):
    return render(request, 'softwaredev.html')

def businessdev(request):
    return render(request, 'businessdev.html')

def ui_ux(request):
    return render(request, 'ui_ux.html')

def crypto(request):
    return render(request, 'crypto.html')

def career(request):
    return render(request, 'career.html')

def privacy(request):
    return render(request, 'privacy.html')

def ourservices(request):
    return render(request, 'ourservices.html')

def project(request):
    return render(request, 'project.html')

def marketer(request):
    return render(request, 'marketer.html')


#def contact(request):
    #return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=UserCreationForm
    return render(request, 'registration/register.html', {'form':form})

'''
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
			'first_name': form.cleaned_data['first_name'],
			'last_name': form.cleaned_data['last_name'],
			'email': form.cleaned_data['email_address'],
			'message':form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")

	form = ContactForm()
	return render(request, "contact.html", {'form':form})
'''
'''

def contact(request):
	if request.method == 'POST':
		form = Contact(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
			'firstname': form.cleaned_data['firstname'],
			'lastname': form.cleaned_data['lastname'],
            'phoneno': form.cleaned_data['phoneno'],
			'email': form.cleaned_data['email_address'],
            'subject': form.cleaned_data['subject'],
			'yourmessage':form.cleaned_data['yourmessage'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")

	form = ContactForm()
	return render(request, "contact.html", {'form':form})

    '''
# main contact view
def contact(request):

    if request.method == 'POST':
        contact=Contact()
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        yourmessage=request.POST.get('yourmessage')

        contact.first_name=first_name
        contact.last_name=last_name
        contact.phone_number=phone_number
        contact.email=email
        contact.subject=subject
        contact.yourmessage=yourmessage
        contact.save()

#        return HttpResponse('Thanks for contacting us')
        return render(request, 'contact_success.html')
    return render(request, "contact.html",)






#uploading of document

def marketer(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        fs.save(pdf_file.name, pdf_file)
        return render(request, 'upload_success.html', {'pdf_url': fs.url(pdf_file.name)})
#    return render(request, 'upload_pdf.html')
    return render(request, 'marketer.html')




    # views.py

from django.shortcuts import render
from .forms import ApplicationForm

def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')
    else:
        form = ApplicationForm()
    return render(request, 'marketer.html', {'form': form})













    # views.py

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ApplicationForm

def marketer(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Send email with attachment
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pdf_file = form.cleaned_data['pdf_file']

            subject = 'New Job Application'
            message = f"Name: {name}\nEmail: {email}"
            from_email = 'barryekwebelem@email.com'
            recipient_list = ['ekwebelembarry@email.com']

            send_mail(subject, message, from_email, recipient_list, fail_silently=False, attachment=[pdf_file])

            return render(request, 'upload_success.html')
    else:
        form = ApplicationForm()
    return render(request, 'marketer.html', {'form': form})




#########################


# views.py

from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import JobApplicationForm

def submit_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Send email to recipient and admin
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            cv = form.cleaned_data['cv']

            subject = 'New Job Application Received'
            message = f"Name: {name}\nEmail: {email}"
            from_email = 'support@kwebatechhub.com'
            recipient_list = ['ekwebelembarry@gmail.com', 'support@kwebatechhub.com']

            email = EmailMessage(subject, message, from_email, recipient_list)
            email.attach(cv.name, cv.read(), cv.content_type)
            email.send()

            return render(request, 'application_success.html')
    else:
        form = JobApplicationForm()
    return render(request, 'application_form.html', {'form': form})





from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import JobApplicationForm

def marketer(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Send email to recipient and admin
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            cv = form.cleaned_data['cv']

            subject = 'New Job Application Received'
            message = f"Name: {name}\nEmail: {email}"
            from_email = 'support@kwebatechhub.com'
            recipient_list = ['ekwebelembarry@gmail.com', 'support@kwebatechhub.com']

            email = EmailMessage(subject, message, from_email, recipient_list)
            email.attach(cv.name, cv.read(), cv.content_type)
            email.send()

            return render(request, 'application_success.html')
    else:
        form = JobApplicationForm()
    return render(request, 'marketer.html', {'form': form})
