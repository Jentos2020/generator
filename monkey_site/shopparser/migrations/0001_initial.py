# Generated by Django 4.1.5 on 2023-01-31 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_update', models.TimeField(auto_now_add=True)),
                ('BM_count', models.BigIntegerField()),
                ('BM_cost', models.BigIntegerField()),
                ('ZRD_count', models.BigIntegerField()),
                ('ZRD_cost', models.BigIntegerField()),
                ('Farm_count', models.BigIntegerField()),
                ('Farm_cost', models.BigIntegerField()),
                ('Autoreg_count', models.BigIntegerField()),
                ('Autoreg_cost', models.BigIntegerField()),
                ('FP_count', models.BigIntegerField()),
                ('FP_cost', models.BigIntegerField()),
                ('PZRDFP_count', models.BigIntegerField()),
                ('PZRDFP_cost', models.BigIntegerField()),
                ('Undef_count', models.BigIntegerField()),
                ('Undef_cost', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShopState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_update', models.TimeField(auto_now_add=True)),
                ('BM_count', models.BigIntegerField()),
                ('BM_cost', models.BigIntegerField()),
                ('ZRD_count', models.BigIntegerField()),
                ('ZRD_cost', models.BigIntegerField()),
                ('Farm_count', models.BigIntegerField()),
                ('Farm_cost', models.BigIntegerField()),
                ('Autoreg_count', models.BigIntegerField()),
                ('Autoreg_cost', models.BigIntegerField()),
                ('FP_count', models.BigIntegerField()),
                ('FP_cost', models.BigIntegerField()),
                ('PZRDFP_count', models.BigIntegerField()),
                ('PZRDFP_cost', models.BigIntegerField()),
                ('Undef_count', models.BigIntegerField()),
                ('Undef_cost', models.BigIntegerField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shopparser.shop')),
            ],
        ),
    ]
