from django.shortcuts import render
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
#from .models import ContactForm

def home(request):
    # context={
    # 'posts':Post.objects.all()
    # }
    return render(request, 'blog/home.html')

def about(request):
    
    # if request.method == "POST":
    # 	message_name = request.POST['message-name'],
	# 	message_email = request.POST['message-email'],
	# 	message = request.POST['message']

	# 	# send an email
	# 	send_mail(
	# 		message_name, # subject
	# 		message, # message
	# 		message_email, # from email
	# 		['ratanridhi18@gmail.com'], # To Email
	# 		)

	# 	return render(request, 'blog/about.html', {'message_name': message_name})

	# else:
	# 	#return render(request, 'contact.html', {})
    return render(request, 'blog/about.html',{'title':'about'})


def new(request):
    return render(request, 'blog/new.html')

def p1(request):
    return render(request, 'blog/p1.html')

def p2(request):
    return render(request, 'blog/p2.html')
def p3(request):
    return render(request, 'blog/p3.html')
def p4(request):
    return render(request, 'blog/p4.html')
def p5(request):
    return render(request, 'blog/p5.html')

# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['ratanridhi18@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "email.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')

# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']