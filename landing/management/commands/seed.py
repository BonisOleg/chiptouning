from django.core.management.base import BaseCommand
from landing.models1 import SiteSettings, HeroSection, AboutSection, ServiceItem
from landing.models2 import (
    WorkStep, StatItem, AdvantageItem, AdvantagesSection,
    ServicesSection, ContactSection, FAQSection, FAQItem,
)


class Command(BaseCommand):
    help = 'Seed database with default landing page content'

    def handle(self, *args, **options):
        self._seed_site()
        self._seed_hero()
        self._seed_about()
        self._seed_services()
        self._seed_steps()
        self._seed_stats()
        self._seed_advantages()
        self._seed_contact()
        self._seed_faq()
        self.stdout.write(self.style.SUCCESS('Seed completed successfully.'))

    def _seed_site(self):
        obj = SiteSettings.load()
        obj.phone = '+380 00 000 00 00'
        obj.email = 'info@example.com'
        obj.address = 'Адреса офісу'
        obj.call_btn_text = 'Замовити дзвінок'
        obj.save()

    def _seed_hero(self):
        obj = HeroSection.load()
        obj.title = 'ЗАГОЛОВОК ВАШОГО ЛЕНДІНГУ'
        obj.subtitle = 'Короткий опис вашої основної пропозиції або переваги вашого продукту.'
        obj.btn_buy_text = 'ДІЗНАТИСЯ БІЛЬШЕ'
        obj.btn_sell_text = 'ЗВ\'ЯЗАТИСЯ З НАМИ'
        obj.overlay_opacity = 0.65
        obj.save()

    def _seed_about(self):
        obj = AboutSection.load()
        obj.title = 'Про нас'
        obj.philosophy_title = 'Наша філософія та підхід до роботи'
        obj.philosophy_text = (
            'Тут ви можете описати історію вашої компанії, її цінності та місію. '
            'Розкажіть про те, що робить вас особливими та чому клієнти обирають саме вас.\n\n'
            'Цей текст є плейсхолдером і його слід замінити на ваш власний унікальний контент.'
        )
        obj.save()

    def _seed_services(self):
        ServicesSection.objects.get_or_create(pk=1, defaults={
            'title': 'Наші послуги',
            'steps_title': 'Як ми працюємо: основні етапи',
        })
        ServiceItem.objects.all().delete()
        
        cat1 = [
            ('Послуга 1.1', 'Опис першої послуги з першої категорії.'),
            ('Послуга 1.2', 'Опис другої послуги з першої категорії.'),
            ('Послуга 1.3', 'Опис третьої послуги з першої категорії.'),
        ]
        cat2 = [
            ('Послуга 2.1', 'Опис першої послуги з другої категорії.'),
            ('Послуга 2.2', 'Опис другої послуги з другої категорії.'),
            ('Послуга 2.3', 'Опис третьої послуги з другої категорії.'),
        ]
        for i, (t, d) in enumerate(cat1):
            ServiceItem.objects.create(category='cat1', title=t, description=d, order=i)
        for i, (t, d) in enumerate(cat2):
            ServiceItem.objects.create(category='cat2', title=t, description=d, order=i)

    def _seed_steps(self):
        WorkStep.objects.all().delete()
        steps = [
            (1, 'Етап 1: Знайомство',
             'Перший крок у нашій співпраці. Ми обговорюємо ваші потреби та цілі.', False),
            (2, 'Етап 2: Аналіз',
             'Ми проводимо детальний аналіз ситуації та розробляємо оптимальний план дій.', False),
            (3, 'Етап 3: Підготовка',
             'Збір необхідних даних та ресурсів для реалізації проекту.', False),
            (4, 'Етап 4: Реалізація',
             'Основний етап роботи, де ми втілюємо заплановане в життя.', True),
            (5, 'Етап 5: Результат',
             'Завершення проекту та отримання фінального результату.', False),
        ]
        for num, title, desc, highlighted in steps:
            WorkStep.objects.create(
                number=num, title=title, description=desc,
                is_highlighted=highlighted, order=num
            )

    def _seed_stats(self):
        StatItem.objects.all().delete()
        items = [
            ('100+', 'Задоволених клієнтів', 0),
            ('5 років', 'Досвіду на ринку', 1),
            ('500+', 'Успішних проектів', 2),
            ('24/7', 'Підтримка клієнтів', 3),
        ]
        for val, lbl, order in items:
            StatItem.objects.create(value=val, label=lbl, order=order)

    def _seed_advantages(self):
        obj = AdvantagesSection.load()
        obj.title = 'Чому обирають нас?'
        obj.subtitle = 'Основні переваги нашої компанії та підходу до роботи.'
        obj.footer_quote = 'Ми працюємо на ваш результат, забезпечуючи найвищу якість.'
        obj.save()

        AdvantageItem.objects.all().delete()
        items = [
            ('clock', 'Професіоналізм', 'Досвідчені фахівці, які знають свою справу.', 0),
            ('checkmark', 'Якість', 'Гарантуємо високу якість виконання кожного завдання.', 1),
            ('eye', 'Прозорість', 'Повна прозорість процесів та відкритість.', 2),
            ('chart', 'Ефективність', 'Сучасні інструменти для найкращих результатів.', 3),
            ('key', 'Індивідуальність', 'Рішення, розроблені під ваші потреби.', 4),
            ('shield', 'Надійність', 'Партнер, на якого можна покластися.', 5),
        ]
        for icon_key, title, desc, order in items:
            AdvantageItem.objects.create(
                icon_key=icon_key, title=title, description=desc, order=order
            )

    def _seed_contact(self):
        obj = ContactSection.load()
        obj.title = 'Зв\'яжіться з нами'
        obj.description = 'Ми готові відповісти на всі ваші запитання.'
        obj.form_title = 'Залишити заявку'
        obj.form_btn_text = 'ВІДПРАВИТИ'
        obj.privacy_note = 'Ваші дані в безпеці. Ми гарантуємо конфіденційність.'
        obj.save()

    def _seed_faq(self):
        obj = FAQSection.load()
        obj.title = 'Часті запитання'
        obj.save()

        FAQItem.objects.all().delete()
        items = [
            ('Яка вартість ваших послуг?', 'Вартість залежить від обсягу та складності проекту. Зв\'яжіться з нами для розрахунку.', 0),
            ('Які терміни виконання робіт?', 'Терміни обговорюються індивідуально для кожного проекту.', 1),
            ('Чи надаєте ви підтримку після завершення?', 'Так, ми забезпечуємо технічну та консультаційну підтримку.', 2),
        ]
        for q, a, order in items:
            FAQItem.objects.create(question=q, answer=a, order=order)
