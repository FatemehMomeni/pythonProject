# Generated by Django 3.1.5 on 2021-01-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.TextField(default='channel')),
                ('mem1_name', models.TextField(default='member1', max_length=20)),
                ('mem2_name', models.TextField(default='member2', max_length=20)),
                ('mem3_name', models.TextField(default='member3', max_length=20)),
                ('mem4_name', models.TextField(default='member4', max_length=20)),
                ('mem5_name', models.TextField(default='member5', max_length=20)),
                ('password', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PublicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.TextField(default='Group')),
                ('mem1_name', models.TextField(default='member1', max_length=20)),
                ('mem2_name', models.TextField(default='member2', max_length=20)),
                ('mem3_name', models.TextField(default='member3', max_length=20)),
                ('mem4_name', models.TextField(default='member4', max_length=20)),
                ('mem5_name', models.TextField(default='member5', max_length=20)),
                ('password', models.TextField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='channel',
            name='mem1_name',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='mem2_name',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='mem3_name',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='mem4_name',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='mem5_name',
        ),
        migrations.RemoveField(
            model_name='public',
            name='mem1_name',
        ),
        migrations.RemoveField(
            model_name='public',
            name='mem2_name',
        ),
        migrations.RemoveField(
            model_name='public',
            name='mem3_name',
        ),
        migrations.RemoveField(
            model_name='public',
            name='mem4_name',
        ),
        migrations.RemoveField(
            model_name='public',
            name='mem5_name',
        ),
        migrations.AddField(
            model_name='channel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='channel',
            name='adminMsg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='private',
            name='contactMsg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='private',
            name='myMsg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='public',
            name='mem1Msg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='public',
            name='mem2Msg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='public',
            name='mem3Msg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='public',
            name='mem4Msg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='public',
            name='mem5Msg',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='public',
            name='myMsg',
            field=models.TextField(default=''),
        ),
    ]
