# Generated by Django 3.1.5 on 2021-01-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatweb', '0004_auto_20210122_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonality',
            name='password',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userpersonality',
            name='username',
            field=models.TextField(default='chatroom', max_length=20, primary_key=True, serialize=False),
        ),
    ]
