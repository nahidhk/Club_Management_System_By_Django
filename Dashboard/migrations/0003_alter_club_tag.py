# Generated by Django 5.0.4 on 2024-06-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_club_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='tag',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]