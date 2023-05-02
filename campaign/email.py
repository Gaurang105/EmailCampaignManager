from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_email(subject, to_email, html_content):
    text_content = strip_tags(html_content)  # This will extract plain text from your HTML content
    email = EmailMultiAlternatives(
        subject,
        text_content,
        'gauranggujrati11@gmail.com',
        [to_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
