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


SERVICE_ICON_CHOICES = [
    ('filter', 'Фильтр (DPF/FAP)'),
    ('recycle', 'Рециркуляция (EGR)'),
    ('droplet', 'Мочевина (AdBlue)'),
    ('gauge', 'Датчик (Lambda/CAT)'),
    ('wind', 'Заслонки (Flaps/TVA)'),
    ('alert', 'Ошибки (DTC)'),
    ('engine', 'Двигатель'),
    ('speed', 'Мощность (Stage)'),
    ('wrench', 'Настройка'),
]


class SiteSettings(SingletonModel):
    logo = models.ImageField(
        upload_to='site/', blank=True, null=True,
        verbose_name='Логотип'
    )
    phone = models.CharField(
        max_length=30, default='+38095-073-41-18',
        verbose_name='Телефон'
    )
    email = models.EmailField(
        default='distageavto@gmail.com',
        verbose_name='Email'
    )
    address = models.CharField(
        max_length=255, blank=True,
        verbose_name='Адрес'
    )
    telegram_url = models.URLField(blank=True, verbose_name='Telegram')
    viber_url = models.URLField(blank=True, verbose_name='Viber')
    whatsapp_url = models.URLField(blank=True, verbose_name='WhatsApp')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram')
    call_btn_text = models.CharField(
        max_length=60, default='Получить консультацию',
        verbose_name='Текст кнопки звонка'
    )

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self) -> str:
        return 'Настройки сайта'


class HeroSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='БЫСТРЕЕ. МОЩНЕЕ. ЭКОНОМИЧНЕЕ.',
        verbose_name='Заголовок'
    )
    subtitle = models.TextField(
        default='Профессиональный чип-тюнинг и калибровка ЭБУ.',
        verbose_name='Подзаголовок'
    )
    btn_buy_text = models.CharField(
        max_length=60, default='Получить консультацию',
        verbose_name='Текст кнопки 1'
    )
    btn_sell_text = models.CharField(
        max_length=60, default='Наши услуги',
        verbose_name='Текст кнопки 2'
    )
    bg_image = models.ImageField(
        upload_to='hero/', blank=True, null=True,
        verbose_name='Фоновое изображение'
    )
    overlay_opacity = models.FloatField(
        default=0.7,
        verbose_name='Прозрачность оверлея (0–1)'
    )

    class Meta:
        verbose_name = 'Hero-секция'
        verbose_name_plural = 'Hero-секция'

    def __str__(self) -> str:
        return 'Hero-секция'


class AboutSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='Что такое чип-тюнинг?',
        verbose_name='Заголовок секции'
    )
    philosophy_title = models.CharField(
        max_length=160,
        default='Раскройте потенциал вашего двигателя',
        verbose_name='Заголовок подблока'
    )
    philosophy_text = models.TextField(
        verbose_name='Текст описания',
        default='Чип-тюнинг — это оптимизация заводской прошивки ЭБУ двигателя.'
    )

    class Meta:
        verbose_name = 'Секция «О нас»'
        verbose_name_plural = 'Секция «О нас»'

    def __str__(self) -> str:
        return 'О нас'


class ServiceItem(models.Model):
    CATEGORY_CHOICES = [
        ('removal', 'Удаление систем'),
        ('tuning', 'Настройка мощности'),
    ]
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES,
        verbose_name='Категория'
    )
    icon_key = models.CharField(
        max_length=20, choices=SERVICE_ICON_CHOICES,
        default='engine', blank=True,
        verbose_name='Иконка'
    )
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['category', 'order']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self) -> str:
        return f'{self.get_category_display()} — {self.title}'
