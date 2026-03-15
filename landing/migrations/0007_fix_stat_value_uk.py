from django.db import migrations

def fix_stat_value_uk(apps, schema_editor):
    StatItem = apps.get_model('landing', 'StatItem')
    for item in StatItem.objects.all():
        if 'лет' in item.value:
            item.value_uk = item.value.replace('лет', 'років')
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_seed_reviews'),
    ]

    operations = [
        migrations.RunPython(fix_stat_value_uk),
    ]
