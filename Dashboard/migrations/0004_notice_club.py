# Generated by Django 5.0.4 on 2024-07-15 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_alter_club_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.club'),
        ),
    ]
