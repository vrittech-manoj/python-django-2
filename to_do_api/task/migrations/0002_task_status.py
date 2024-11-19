# Generated by Django 4.2.16 on 2024-11-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('processing', 'processing'), ('completed', 'completed')], default='pending', max_length=200),
        ),
    ]
