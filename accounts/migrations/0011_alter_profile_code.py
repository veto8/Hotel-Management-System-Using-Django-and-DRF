# Generated by Django 5.0.3 on 2024-06-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='XUFnhpp2rHqVjXG76wlk', max_length=200, null=True),
        ),
    ]
