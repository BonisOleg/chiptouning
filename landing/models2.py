from django.db import models
from .models1 import SingletonModel


class WorkStep(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Номер шага')
    title = models.CharField(max_length=160, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    is_highlighted = models.BooleanField(
        default=False,
        verbose_name='Выделить (акцент)'
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Шаг работы'
        verbose_name_plural = 'Этапы работы'

    def __str__(self) -> str:
        return f'Шаг {self.number}: {self.title}'


class StatItem(models.Model):
    value = models.CharField(max_length=40, verbose_name='Значение')
    label = models.CharField(max_length=120, verbose_name='Подпись')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика (цифры)'

    def __str__(self) -> str:
        return f'{self.value} — {self.label}'


ICON_CHOICES = [
    ('shield', 'Щит (безопасность)'),
    ('chart', 'График (выгода)'),
    ('clock', 'Часы (опыт)'),
    ('key', 'Ключ (под ключ)'),
    ('eye', 'Глаз (мониторинг)'),
    ('checkmark', 'Галочка (гарантия)'),
    ('star', 'Звезда'),
    ('map', 'Карта'),
    ('engine', 'Двигатель'),
    ('speed', 'Спидометр'),
    ('fuel', 'Топливо'),
    ('wrench', 'Гаечный ключ'),
    ('power', 'Молния (мощность)'),
    ('headset', 'Поддержка'),
]


class AdvantageItem(models.Model):
    icon_key = models.CharField(
        max_length=20, choices=ICON_CHOICES, default='shield',
        verbose_name='Иконка'
    )
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self) -> str:
        return self.title


class AdvantagesSection(SingletonModel):
    title = models.CharField(
        max_length=120,
        default='Почему выбирают нас?',
        verbose_name='Заголовок секции'
    )
    subtitle = models.CharField(
        max_length=200,
        default='Качество, поддержка и индивидуальный подход.',
        verbose_name='Подзаголовок'
    )
    footer_quote = models.TextField(
        default='Мы не бросаем в трудной ситуации.',
        verbose_name='Цитата внизу блока'
    )

    class Meta:
        verbose_name = 'Секция «Преимущества»'
        verbose_name_plural = 'Секция «Преимущества»'

    def __str__(self) -> str:
        return 'Преимущества'


class ServicesSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='Наши услуги',
        verbose_name='Заголовок секции'
    )
    steps_title = models.CharField(
        max_length=160,
        default='Как мы работаем',
        verbose_name='Заголовок блока шагов'
    )

    class Meta:
        verbose_name = 'Секция «Услуги»'
        verbose_name_plural = 'Секция «Услуги»'

    def __str__(self) -> str:
        return 'Услуги'


class ContactSection(SingletonModel):
    title = models.CharField(
        max_length=120,
        default='Свяжитесь с нами',
        verbose_name='Заголовок'
    )
    description = models.TextField(
        default='Оставьте заявку — мы перезвоним в кратчайшее время.',
        verbose_name='Описание'
    )
    form_title = models.CharField(
        max_length=120,
        default='Оставить заявку',
        verbose_name='Заголовок формы'
    )
    form_btn_text = models.CharField(
        max_length=80,
        default='ОТПРАВИТЬ',
        verbose_name='Текст кнопки формы'
    )
    privacy_note = models.CharField(
        max_length=200,
        default='Ваши данные в безопасности. Мы гарантируем конфиденциальность.',
        verbose_name='Прим. конфиденциальности'
    )

    class Meta:
        verbose_name = 'Секция «Контакты»'
        verbose_name_plural = 'Секция «Контакты»'

    def __str__(self) -> str:
        return 'Контакты'


class FAQSection(SingletonModel):
    title = models.CharField(
        max_length=120, default='Частые вопросы',
        verbose_name='Заголовок секции'
    )

    class Meta:
        verbose_name = 'Секция FAQ'
        verbose_name_plural = 'Секция FAQ'

    def __str__(self) -> str:
        return 'FAQ'


class FAQItem(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'FAQ (Вопросы-ответы)'

    def __str__(self) -> str:
        return self.question


class LeadSubmission(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(blank=True, default='', verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_processed = models.BooleanField(
        default=False, verbose_name='Обработано'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self) -> str:
        return f'{self.name} ({self.phone})'


class ReviewItem(models.Model):
    author = models.CharField(max_length=80, verbose_name='Автор')
    car = models.CharField(max_length=80, blank=True, verbose_name='Авто')
    text = models.TextField(verbose_name='Текст відгуку')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self) -> str:
        return f'Відгук від {self.author}'


class PartnerItem(models.Model):
    name = models.CharField(max_length=120, verbose_name='Назва')
    logo = models.ImageField(upload_to='partners/', verbose_name='Логотип', blank=True)
    description = models.TextField(blank=True, verbose_name='Опис')
    url = models.URLField(blank=True, verbose_name='Посилання')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'

    def __str__(self) -> str:
        return self.name
