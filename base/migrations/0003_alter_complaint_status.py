# Generated by Django 5.0.6 on 2024-09-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Resolved', 'Resolved'), ('Unresolved', 'Unresolved')], default='Unresolved', max_length=100),
        ),
    ]
