# Generated by Django 5.0.1 on 2024-01-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]