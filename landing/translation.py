from modeltranslation.translator import register, TranslationOptions
from .models1 import SiteSettings, HeroSection, AboutSection, ServiceItem
from .models2 import (
    WorkStep, StatItem, AdvantageItem, AdvantagesSection,
    ServicesSection, ContactSection, FAQSection, FAQItem, ReviewItem,
)


@register(SiteSettings)
class SiteSettingsTO(TranslationOptions):
    fields = ('call_btn_text', 'address')


@register(HeroSection)
class HeroSectionTO(TranslationOptions):
    fields = ('title', 'subtitle', 'btn_buy_text', 'btn_sell_text')


@register(AboutSection)
class AboutSectionTO(TranslationOptions):
    fields = ('title', 'philosophy_title', 'philosophy_text')


@register(ServiceItem)
class ServiceItemTO(TranslationOptions):
    fields = ('title', 'description')


@register(WorkStep)
class WorkStepTO(TranslationOptions):
    fields = ('title', 'description')


@register(StatItem)
class StatItemTO(TranslationOptions):
    fields = ('value', 'label')


@register(AdvantageItem)
class AdvantageItemTO(TranslationOptions):
    fields = ('title', 'description')


@register(AdvantagesSection)
class AdvantagesSectionTO(TranslationOptions):
    fields = ('title', 'subtitle', 'footer_quote')


@register(ServicesSection)
class ServicesSectionTO(TranslationOptions):
    fields = ('title', 'steps_title')


@register(ContactSection)
class ContactSectionTO(TranslationOptions):
    fields = ('title', 'description', 'form_title', 'form_btn_text', 'privacy_note')


@register(FAQSection)
class FAQSectionTO(TranslationOptions):
    fields = ('title',)


@register(FAQItem)
class FAQItemTO(TranslationOptions):
    fields = ('question', 'answer')


@register(ReviewItem)
class ReviewItemTO(TranslationOptions):
    fields = ('text',)
