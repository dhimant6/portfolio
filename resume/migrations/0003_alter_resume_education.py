# Generated by Django 3.2.4 on 2021-06-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_resume_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='Education',
            field=models.TextField(blank=True),
        ),
    ]