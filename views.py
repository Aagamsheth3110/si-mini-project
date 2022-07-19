from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def email(request):
	return render(request,'customer/email.html')

def email_info(request):
	myto = request.POST['to']
	mysubject = request.POST['subject']
	mymassage = request.POST['massage']


	#email 
	send_mail(mysubject,mymassage,settings.EMAIL_HOST_USER,[myto], fail_silently=False)
	return redirect('/customer/email/')

