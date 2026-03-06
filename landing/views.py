import logging
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

from .models1 import SiteSettings, HeroSection, AboutSection, ServiceItem
from .models2 import (
    WorkStep, StatItem, AdvantageItem, AdvantagesSection,
    ServicesSection, ContactSection, FAQSection, FAQItem, LeadSubmission,
)


def _get_context():
    return {
        'site': SiteSettings.load(),
        'hero': HeroSection.load(),
        'about': AboutSection.load(),
        'services_section': ServicesSection.load(),
        'service_cat1': ServiceItem.objects.filter(category='cat1'),
        'service_cat2': ServiceItem.objects.filter(category='cat2'),
        'steps': WorkStep.objects.all(),
        'stats': StatItem.objects.all(),
        'advantages_section': AdvantagesSection.load(),
        'advantages': AdvantageItem.objects.all(),
        'contact': ContactSection.load(),
        'faq_section': FAQSection.load(),
        'faq_items': FAQItem.objects.all(),
    }


class IndexView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(_get_context())
        return ctx


class LeadFormView(View):
    def post(self, request):
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        interest = request.POST.get('interest', 'consult')

        if name and phone:
            LeadSubmission.objects.create(name=name, phone=phone, interest=interest)

        contact = ContactSection.load()
        return render(request, 'landing/htmx/lead_success.html', {'contact': contact})
