# Generated by Django 3.1.1 on 2020-11-11 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('eav', '0005_auto_20201104_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='generic_value_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='value_values', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='value',
            name='value_enum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eav_values', to='eav.enumvalue'),
        ),
    ]