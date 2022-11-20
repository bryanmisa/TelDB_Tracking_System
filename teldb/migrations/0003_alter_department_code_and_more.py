# Generated by Django 4.1.3 on 2022-11-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teldb', '0002_remove_telephone_code_department_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dep_code', to='teldb.code'),
        ),
        migrations.AlterField(
            model_name='directinwarddialin',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Free', 'Free'), ('Inactive', 'Inactive')], default='Free', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to='teldb.department'),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to', to='teldb.employee'),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='extension_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extension_number', to='teldb.directinwarddialin'),
        ),
    ]