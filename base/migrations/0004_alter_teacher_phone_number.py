# Generated by Django 4.1.2 on 2023-02-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_exam_end_time_remove_exam_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
