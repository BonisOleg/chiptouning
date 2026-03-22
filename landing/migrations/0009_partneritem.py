# Generated manually (simulating makemigrations)

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_fix_experience_10_rokiv'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Назва')),
                ('logo', models.ImageField(upload_to='partners/', verbose_name='Логотип')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('description_uk', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('url', models.URLField(blank=True, verbose_name='Посилання')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнери',
                'ordering': ['order'],
            },
        ),
    ]
