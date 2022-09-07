# Generated by Django 4.0.4 on 2022-08-10 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_country_isavailable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
                ('submittedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'report',
            },
        ),
    ]
