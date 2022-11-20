# Generated by Django 4.1.2 on 2022-10-31 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teldb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telephone',
            name='code',
        ),
        migrations.AddField(
            model_name='department',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_code', to='teldb.code'),
        ),
    ]
