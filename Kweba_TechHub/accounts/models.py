from django.db import models

# Create your models here.

class Contact(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	phone_number  = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 150)
	subject = models.CharField(max_length = 50)
	yourmessage = models.TextField( max_length = 2000)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"




class UploadedPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pdf_file.name


# models.py

from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed
    pdf_file = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




##################





# models.py

from django.db import models

class JobApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    cover_letter = models.TextField()
    cv = models.FileField(upload_to='cv_files/')
    email = models.EmailField(default="support@kwebatechhub.com")  # Use spaces for indentation

    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# models.py

from django.db import models

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
