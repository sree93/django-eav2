# Generated by Django 3.1.1 on 2020-10-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0002_auto_20201001_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='category',
            field=models.CharField(blank=True, help_text='Category', max_length=128, null=True, verbose_name='Category'),
        ),
    ]
