from django.contrib import admin
from .admin1 import SingletonAdmin
from .models2 import (
    WorkStep, StatItem, AdvantageItem, AdvantagesSection,
    ServicesSection, ContactSection, FAQSection, FAQItem, LeadSubmission, ReviewItem, PartnerItem,
)


@admin.register(WorkStep)
class WorkStepAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_highlighted', 'order')
    list_editable = ('order', 'is_highlighted')
    ordering = ('order',)


@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(AdvantageItem)
class AdvantageItemAdmin(admin.ModelAdmin):
    list_display = ('icon_key', 'title', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(AdvantagesSection)
class AdvantagesSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секция «Преимущества»', {
            'fields': ('title', 'subtitle', 'footer_quote'),
        }),
    )


@admin.register(ServicesSection)
class ServicesSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секция «Услуги»', {
            'fields': ('title', 'steps_title'),
        }),
    )


@admin.register(ContactSection)
class ContactSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секция «Контакты»', {
            'fields': ('title', 'description', 'form_title', 'form_btn_text', 'privacy_note'),
        }),
    )


@admin.register(FAQSection)
class FAQSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секция FAQ', {
            'fields': ('title',),
        }),
    )


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(LeadSubmission)
class LeadSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'is_processed')
    list_filter = ('is_processed',)
    list_editable = ('is_processed',)
    readonly_fields = ('name', 'phone', 'message', 'created_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False


@admin.register(ReviewItem)
class ReviewItemAdmin(admin.ModelAdmin):
    list_display = ('author', 'car', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(PartnerItem)
class PartnerItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('order',)
