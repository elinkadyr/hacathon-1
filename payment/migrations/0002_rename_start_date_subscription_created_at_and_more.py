# Generated by Django 4.2.1 on 2023-05-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='start_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_cvv',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_exp_month',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_exp_year',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='subscription',
            name='card_number',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='subscription',
            name='cardholder_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='subscription',
            name='transaction_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
