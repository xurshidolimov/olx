# Generated by Django 4.0.5 on 2022-06-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
