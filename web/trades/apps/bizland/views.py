from django.shortcuts import render
from .models import Companies
from .models import Contact
from django.core.mail import EmailMessage
from .models import ReceivedMessages, Portfolios, PortfolioLi
from django.http import JsonResponse
from django.core.mail import send_mail


def index(request):
    company_ = Companies.objects.get(id=1)
    biz = company_
    contact_obj = biz
    portfolios = Portfolios.objects.all()
    portfolio_links = PortfolioLi.objects.all()
    return render(request, 'bizland/index.html', {'company': company_, 'contact_obj': contact_obj,
                                                  'portfolios': portfolios, 'portfolio_links': portfolio_links})


def post_contact_us(request):
    company_ = Companies.objects.get(id=1)
    if request.method == 'POST':
        contact_us_name = request.POST.get('name')
        contact_us_email = request.POST.get('email')
        contact_us_subject = request.POST.get('subject')
        contact_us_message = request.POST.get('message')
        if contact_us_subject == '' or contact_us_message == '':
            rr = {'status': 'Must enter subject and a message!'}
        else:
            try:
                ReceivedMessages.objects.create(company=company_,
                                                name=contact_us_name,
                                                email=contact_us_email,
                                                subject=contact_us_subject,
                                                message=contact_us_message)
                contact_us_message = 'message received from ' + contact_us_name + ' \nEmail:' + contact_us_email + ' \nMessage:\n' + contact_us_message
                #print(contact_us_message)
                email = EmailMessage(contact_us_subject,
                                     contact_us_message,
                                     contact_us_email,
                                     [company_.email]
                                     )
                email.send()
                print(contact_us_email)
                print(company_.email)
                rr = {'status': 'Your message was received.\n\nThank you.'}
            except Exception as ee:
                print(ee)
                rr = {'status': 'ko'}

    return JsonResponse(rr)

# def post_contact_us(request):
#
#     contact_id = request.POST.get('contact_id')
#     contact_us_name = request.POST.get('name')
#     contact_us_email = request.POST.get('email')
#     print(contact_us_email)
#     print(1111111111111111111111)
#     contact_us_subject = request.POST.get('subject')
#     contact_us_message = request.POST.get('contact_us_message')
#     if contact_us_subject == '' or contact_us_message == '':
#         rr = {'status': 'Must enter subject and a message!'}
#     else:
#         rr = {'status': 'got it'}
#         contact_us_message = 'Received email from: ' + contact_us_email + '\n\n' + request.POST.get('contact_us_message')
#         print(contact_us_message)
#         try:
#             #contact_ = Contact.objects.get(id=contact_id)
#             ReceivedMessages.objects.create(contact=contact_id, name=contact_us_name, email=contact_us_email,
#                                             subject=contact_us_subject, message=contact_us_message)
#             print(ReceivedMessages)
#             email = EmailMessage(contact_us_subject, contact_us_message, contact_us_email, [contact_id.contact_us_email])
#             email.send()
#             rr = {'status': 'Your message was received.\n\nThank you.'}
#         except Exception as ee:
#             rr = {'status': 'ko'}
#     return JsonResponse(rr)


