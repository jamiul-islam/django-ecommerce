# Generated by Django 5.1.2 on 2024-10-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='-', max_length=10),
            preserve_default=False,
        ),
    ]
