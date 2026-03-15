from django.db import migrations

def fix_experience_value(apps, schema_editor):
    StatItem = apps.get_model('landing', 'StatItem')
    for item in StatItem.objects.all():
        # Find the experience/years stat (has 'лет' or 'років' in value)
        if 'лет' in item.value or 'років' in item.value:
            item.value = '10 лет'
            item.value_ru = '10 лет'
            item.value_uk = '10 років'
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_fix_stat_value_uk'),
    ]

    operations = [
        migrations.RunPython(fix_experience_value),
    ]
