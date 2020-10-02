# Generated by Django 3.1.1 on 2020-10-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0003_attribute_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='category',
        ),
        migrations.AddField(
            model_name='attribute',
            name='tag',
            field=models.CharField(blank=True, help_text='Tag the attribute for categorisation', max_length=128, null=True, verbose_name='Tag'),
        ),
    ]
