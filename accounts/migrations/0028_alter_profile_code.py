# Generated by Django 5.0.7 on 2024-07-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_alter_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='5ItN7UIPCUvDG3bDWCME', max_length=200, null=True),
        ),
    ]