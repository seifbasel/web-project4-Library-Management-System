# Generated by Django 4.2.4 on 2023-08-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
