# Generated by Django 4.2.7 on 2023-11-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=120)),
                ('content', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]
