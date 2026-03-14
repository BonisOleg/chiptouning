import re

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models1 import SiteSettings, HeroSection, AboutSection, ServiceItem
from .models2 import (
    WorkStep, StatItem, AdvantageItem, AdvantagesSection,
    ServicesSection, ContactSection, FAQSection, FAQItem, LeadSubmission,
)

_PHONE_RE = re.compile(r'^\+?[\d\s\-\(\)]{7,20}$')
_LEAD_RATE_LIMIT = 5
_LEAD_RATE_WINDOW = 3600  # seconds (1 hour)


def _get_context() -> dict:
    return {
        'site': SiteSettings.load(),
        'hero': HeroSection.load(),
        'about': AboutSection.load(),
        'services_section': ServicesSection.load(),
        'service_cat1': ServiceItem.objects.filter(category='removal'),
        'service_cat2': ServiceItem.objects.filter(category='tuning'),
        'steps': WorkStep.objects.all(),
        'stats': StatItem.objects.all(),
        'advantages_section': AdvantagesSection.load(),
        'advantages': AdvantageItem.objects.all(),
        'contact': ContactSection.load(),
        'faq_section': FAQSection.load(),
        'faq_items': FAQItem.objects.all(),
    }


def _get_client_ip(request) -> str:
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '')


def _is_rate_limited(ip: str) -> bool:
    key = f'lead_rl:{ip}'
    count: int = cache.get(key, 0)
    if count >= _LEAD_RATE_LIMIT:
        return True
    cache.set(key, count + 1, timeout=_LEAD_RATE_WINDOW)
    return False


def _send_lead_notification(name: str, phone: str, message: str) -> None:
    recipient = getattr(settings, 'LEAD_NOTIFICATION_EMAIL', '') or getattr(settings, 'EMAIL_HOST_USER', '')
    if not recipient:
        return
    body = f'Ім\'я: {name}\nТелефон: {phone}'
    if message:
        body += f'\nПовідомлення: {message}'
    try:
        send_mail(
            subject=f'[DISTAGE] Нова заявка від {name}',
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=True,
        )
    except Exception:
        pass


class IndexView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(_get_context())
        return ctx


class LeadFormView(View):
    def post(self, request):
        contact = ContactSection.load()

        # Honeypot check — bots fill hidden fields, humans don't
        if request.POST.get('website', ''):
            return render(request, 'landing/htmx/lead_success.html', {'contact': contact})

        # Rate limiting by IP
        ip = _get_client_ip(request)
        if _is_rate_limited(ip):
            return render(request, 'landing/htmx/lead_success.html', {'contact': contact})

        name = request.POST.get('name', '').strip()[:120]
        phone = request.POST.get('phone', '').strip()[:20]
        message = request.POST.get('message', '').strip()[:500]

        if name and phone and _PHONE_RE.match(phone):
            LeadSubmission.objects.create(name=name, phone=phone, message=message)
            _send_lead_notification(name, phone, message)

        return render(request, 'landing/htmx/lead_success.html', {'contact': contact})
