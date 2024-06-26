# Generated by Django 5.0.3 on 2024-04-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profitolio', '0005_rename_current_price_record_sell_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='buy_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='buy_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='returns',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='sell_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
