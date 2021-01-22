from django.db import models


class UserPersonality(models.Model):
    first_name = models.TextField(max_length=20, default='first name')
    last_name = models.TextField(max_length=50, default='last name')
    email = models.EmailField()
    username = models.TextField(max_length=20, default='chatroom')
    password = models.TextField(primary_key=True, max_length=15)

    objects = models.Manager()


class Contacts(models.Model):
    name = models.TextField(max_length=20, default='name')
    email = models.EmailField(primary_key=True)
    has_chat = models.BooleanField(default=False)
    password = models.TextField(max_length=15)

    objects = models.Manager()


class Private(models.Model):
    name = models.TextField(max_length=20, default='name')
    password = models.TextField(max_length=15)
    myMsg = models.TextField(default='')
    contactMsg = models.TextField(default='')
    msgTime = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = models.Manager()


class PublicInfo(models.Model):
    group_name = models.TextField(default='Group')
    mem1_name = models.TextField(max_length=20, default='member1', null=True)
    mem2_name = models.TextField(max_length=20, default='member2', null=True)
    mem3_name = models.TextField(max_length=20, default='member3', null=True)
    mem4_name = models.TextField(max_length=20, default='member4', null=True)
    mem5_name = models.TextField(max_length=20, default='member5', null=True)

    objects = models.Manager()


class Public(models.Model):
    group_name = models.TextField(default='Group')
    mem1Msg = models.TextField(default='', null=True)
    mem2Msg = models.TextField(default='', null=True)
    mem3Msg = models.TextField(default='', null=True)
    mem4Msg = models.TextField(default='', null=True)
    mem5Msg = models.TextField(default='', null=True)
    msgTime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    objects = models.Manager()


class ChannelInfo(models.Model):
    channel_name = models.TextField(default='channel')
    mem1_name = models.TextField(max_length=20, default='member1', null=True)
    mem2_name = models.TextField(max_length=20, default='member2', null=True)
    mem3_name = models.TextField(max_length=20, default='member3', null=True)
    mem4_name = models.TextField(max_length=20, default='member4', null=True)
    mem5_name = models.TextField(max_length=20, default='member5', null=True)

    objects = models.Manager()


class Channel(models.Model):
    channel_name = models.TextField(default='channel')
    adminMsg = models.TextField(default='', null=True)
    is_admin = models.BooleanField(default=False)
    msgTime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    objects = models.Manager()
