from django.contrib import admin
from django.utils.html import format_html
from .models1 import SiteSettings, HeroSection, AboutSection, ServiceItem


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    class Media:
        css = {'all': ('css/admin_extra.css',)}

    fieldsets = (
        ('Логотип и контакты', {
            'fields': ('logo', 'logo_preview', 'phone', 'email', 'address'),
        }),
        ('Мессенджеры', {
            'fields': ('telegram_url', 'viber_url', 'whatsapp_url', 'instagram_url'),
        }),
        ('Кнопки', {
            'fields': ('call_btn_text',),
        }),
    )
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" class="admin-img-preview--logo" alt="logo preview" />',
                obj.logo.url
            )
        return '—'
    logo_preview.short_description = 'Предпросмотр'


@admin.register(HeroSection)
class HeroSectionAdmin(SingletonAdmin):
    class Media:
        css = {'all': ('css/admin_extra.css',)}

    fieldsets = (
        ('Тексты', {
            'fields': ('title', 'subtitle', 'btn_buy_text', 'btn_sell_text'),
        }),
        ('Фон', {
            'fields': ('bg_image', 'bg_preview', 'overlay_opacity'),
        }),
    )
    readonly_fields = ('bg_preview',)

    def bg_preview(self, obj):
        if obj.bg_image:
            return format_html(
                '<img src="{}" class="admin-img-preview--bg" alt="bg preview" />',
                obj.bg_image.url
            )
        return '—'
    bg_preview.short_description = 'Предпросмотр'


@admin.register(AboutSection)
class AboutSectionAdmin(SingletonAdmin):
    fieldsets = (
        ('Секция «О нас»', {
            'fields': ('title', 'philosophy_title', 'philosophy_text'),
        }),
    )


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'icon_key', 'title', 'order')
    list_editable = ('order',)
    list_filter = ('category',)
    ordering = ('category', 'order')
