# Generated by Django 4.1.7 on 2023-04-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_signin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='semail',
            new_name='suemail',
        ),
        migrations.RenameField(
            model_name='signin',
            old_name='sname',
            new_name='suname',
        ),
        migrations.RenameField(
            model_name='signin',
            old_name='spassword',
            new_name='supassword',
        ),
    ]
