# Generated by Django 4.0.5 on 2022-06-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_product_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='adress',
            field=models.CharField(blank=True, choices=[('Toshkent', 'Toshkent'), ('Andijon', 'Andijon'), ('Xorazm', 'Xorazm'), ('Buxoro', 'Buxoro'), ('Samarqand', 'Samarqand'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxondaryo', 'Surxondaryo'), ('Namangan', 'Namangan'), ('Sirdaryo', 'Sirdaryo'), ('Jizzax', 'Jizzax'), ('Navoiy', 'Navoiy'), ("Qoraqalpog'iston", "Qoraqalpog'iston"), ("Farg'ona", "Farg'ona"), ("Marg'ilon", "Marg'ilon"), ("Qo'qon", "Qo'qon")], max_length=60, null=True),
        ),
    ]
