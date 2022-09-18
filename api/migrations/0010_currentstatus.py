# Generated by Django 4.0.4 on 2022-09-18 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.country')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.status')),
            ],
            options={
                'db_table': 'current_state',
            },
        ),
        migrations.RunSQL("ALTER TABLE `current_state` CHANGE `status_id` `status_id` BIGINT NOT NULL DEFAULT '1';"),
    ]
