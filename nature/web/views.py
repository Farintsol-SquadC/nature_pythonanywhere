from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
# Create your views here.
from nature import settings
from django.contrib import messages

def home(request):
    if request.method == 'POST' or request.method == 'FILES':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_number = request.POST.get('contact_number')
        contact_msg = request.POST.get('contact_address')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')

        msg = '''
        Below are form details:
        
        Name : '''+contact_name+'''\n
        Email : '''+contact_email+'''\n
        Mobile : '''+contact_number+'''\n
        City : '''+city+'''\n
        Pin Code : '''+pin_code+'''\n
        Address : '''+contact_msg+'''\n
        
        '''

        try:

            send_mail("New Form - Nature's Blessing", msg, settings.EMAIL_HOST_USER, ['thenaturesblessing@gmail.com',])
            print('email sent')
            messages.success(request, "Submitted Successfully!!!")
        except:
            print('exception occured email not sent')
            messages.error(request, "Error in submitting form, Try Again after some time.")
        return redirect('/')
    return render(request,'index.html')