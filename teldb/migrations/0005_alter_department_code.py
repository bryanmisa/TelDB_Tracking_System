# Generated by Django 4.1.3 on 2022-11-07 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teldb', '0004_alter_employee_employee_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_code', to='teldb.code'),
        ),
    ]