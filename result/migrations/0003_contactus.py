# Generated by Django 4.1.7 on 2023-03-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_rename_username_login_lemail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=20)),
                ('query_text', models.CharField(max_length=100)),
            ],
        ),
    ]
