# Generated by Django 3.0.2 on 2020-01-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField(blank=True, db_column='TIME', null=True)),
                ('date', models.DateTimeField(blank=True, db_column='DATE', null=True)),
                ('fee_long', models.FloatField(blank=True, db_column='FEE_LONG', null=True)),
                ('fee_short', models.FloatField(blank=True, db_column='FEE_SHORT', null=True)),
                ('hedge_okex', models.FloatField(blank=True, db_column='HEDGE_OKEX', null=True)),
                ('hedge_bitmex', models.FloatField(blank=True, db_column='HEDGE_BITMEX', null=True)),
                ('option_okex', models.FloatField(blank=True, db_column='OPTION_OKEX', null=True)),
            ],
        ),
    ]
