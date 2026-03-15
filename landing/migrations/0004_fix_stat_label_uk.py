from django.db import migrations

def fix_stat_label_uk(apps, schema_editor):
    StatItem = apps.get_model('landing', 'StatItem')
    for item in StatItem.objects.all():
        if 'лет' in item.label:
            item.label_uk = 'років досвіду'
            item.save()
        elif 'Лет' in item.label:
            item.label_uk = 'Років досвіду'
            item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_faqitem_faqsection_delete_auctionsection_and_more'),
    ]

    operations = [
        migrations.RunPython(fix_stat_label_uk),
    ]
