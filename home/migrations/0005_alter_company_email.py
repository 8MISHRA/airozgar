# Generated by Django 5.1.1 on 2024-12-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
