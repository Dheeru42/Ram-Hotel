# Generated by Django 3.2.25 on 2024-09-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
    ]