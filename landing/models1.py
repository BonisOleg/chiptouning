from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    logo = models.ImageField(
        upload_to='site/', blank=True, null=True,
        verbose_name='Логотип'
    )
    phone = models.CharField(
        max_length=30, default='+380 00 000 00 00',
        verbose_name='Телефон'
    )
    email = models.EmailField(
        default='info@example.com',
        verbose_name='Email'
    )
    address = models.CharField(
        max_length=255, blank=True,
        verbose_name='Адреса офісу'
    )
    telegram_url = models.URLField(blank=True, verbose_name='Telegram')
    viber_url = models.URLField(blank=True, verbose_name='Viber')
    whatsapp_url = models.URLField(blank=True, verbose_name='WhatsApp')
    call_btn_text = models.CharField(
        max_length=60, default='Замовити дзвінок',
        verbose_name='Текст кнопки дзвінка'
    )

    class Meta:
        verbose_name = 'Налаштування сайту'
        verbose_name_plural = 'Налаштування сайту'

    def __str__(self):
        return 'Налаштування сайту'


class HeroSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='Заголовок вашого лендінгу',
        verbose_name='Заголовок'
    )
    subtitle = models.TextField(
        default='Короткий опис вашої основної пропозиції або переваги.',
        verbose_name='Підзаголовок'
    )
    btn_buy_text = models.CharField(
        max_length=60, default='Дізнатися більше',
        verbose_name='Текст кнопки 1'
    )
    btn_sell_text = models.CharField(
        max_length=60, default='Зв\'язатися з нами',
        verbose_name='Текст кнопки 2'
    )
    bg_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Фонове зображення'
    )
    overlay_opacity = models.FloatField(
        default=0.65,
        verbose_name='Прозорість фільтра (0–1)'
    )

    class Meta:
        verbose_name = 'Hero-секція'
        verbose_name_plural = 'Hero-секція'

    def __str__(self):
        return 'Hero-секція'


class AboutSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='Про нас',
        verbose_name='Заголовок секції'
    )
    philosophy_title = models.CharField(
        max_length=160,
        default='Наша філософія та підхід',
        verbose_name='Заголовок підблоку'
    )
    philosophy_text = models.TextField(
        verbose_name='Текст опису',
        default='Тут ви можете описати вашу компанію, місію та цінності.'
    )

    class Meta:
        verbose_name = 'Секція «Про нас»'
        verbose_name_plural = 'Секція «Про нас»'

    def __str__(self):
        return 'Про нас'


class ServiceItem(models.Model):
    CATEGORY_CHOICES = [
        ('cat1', 'Категорія 1'),
        ('cat2', 'Категорія 2'),
    ]
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES,
        verbose_name='Категорія'
    )
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['category', 'order']
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'

    def __str__(self):
        return f'{self.get_category_display()} — {self.title}'
