from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from .models import TextItem

def index(request):
    text = TextItem.objects.all()
    return render(
        request,
        'index.html',
        {'text': text}
    )

def about(request):
    text = TextItem.objects.all()
    return render(
        request,
        'about.html',
        {'text': text}
    )

def gallery(request):
    return render(
        request,
        'gallery.html'
    )

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(name = form.cleaned_data['name'], email = form.cleaned_data['email'], phone = form.cleaned_data['phone'], message = form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contact.html',
        context=context
    )


def send_message(name, email, phone, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'phone': phone, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'flowerclient@example.com'
    text_content = text.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
