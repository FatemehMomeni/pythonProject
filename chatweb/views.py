from django.shortcuts import render
from .models import UserPersonality, Contacts, Private, Public, Channel, PublicInfo, ChannelInfo
import datetime

user_name = ''
user_password = 0
message_location = ''
n_pv = ''
n_group = ''
n_channel = ''


def sign_up(request, username):
    flag = True
    if request.method == 'POST':
        repeat = UserPersonality.objects.filter(username=username)
        if repeat:
            flag = False
        else:
            first_name = request.POST['first-name']
            last_name = request.POST['last-name']
            email = request.POST['email']
            username_in = request.POST['username']
            password_in = request.POST['password']
            global user_password, user_name
            user_password = password_in
            user_name = username_in
            instance = UserPersonality()
            instance.first_name = first_name
            instance.last_name = last_name
            instance.email = email
            instance.username = username_in
            instance.password = password_in
            instance.save()
    return flag


def sign_in(request):
    if request.method == "POST":
        username_in = request.POST['username']
        password_in = request.POST['password']
        global user_password, user_name
        user_password = password_in
        user_name = username_in
        exist = UserPersonality.objects.filter(username=username_in)
        if exist:
            valid = UserPersonality.objects.filter(password=password_in, username=username_in)
            if valid:
                info = main_page()
                return render(request, 'main_page.html', {'username_in': username_in,
                                                          'my_contacts_email': [info[0] for k in range(len(info[0]))][0],
                                                          'my_contacts_name': info[1], 'pv': info[2],
                                                          'group_name': info[3], 'channel_name': info[4]})
            else:
                return render(request, 'index.html', {'message': 'نام کاربری یا رمزعبور اشتباه است'})
        else:
            flag = sign_up(request, username_in)
            if flag:
                info = main_page()
                return render(request, 'main_page.html', {'username_in': username_in,
                                                          'my_contacts_email': info[0],
                                                          'my_contacts_name': info[1], 'pv': info[2],
                                                          'group_name': info[3], 'channel_name': info[4]})
            else:
                return render(request, 'index.html', {'message': 'نام کاربری قبلا انتخاب شده است'})
    else:
        return render(request, 'index.html', {})


def main_page():
    my_contacts = Contacts.objects.filter(password=user_password)
    my_contacts_email = my_contacts.values_list('email')
    my_contacts_name = my_contacts_email.values_list('name')
    privates = my_contacts_email.filter(has_chat=True)
    pv = privates.values_list('name')
    group_name = Public.objects.values_list('group_name')
    channel_name = Channel.objects.values_list('channel_name')

    my_cont_email = []
    my_cont_name = []
    my_pv = []
    my_groups = []
    my_channels = []
    for i in range(len(my_contacts_email)):
        my_cont_email.append(my_contacts_email[i][0])
        my_cont_name.append(my_contacts_name[i][0])
    for i in range(len(pv)):
        my_pv.append(pv[i][0])
    for i in range(len(group_name)):
        my_groups.append(group_name[i][0])
    for i in range(len(channel_name)):
        my_channels.append(channel_name[i][0])

    return my_cont_email, my_cont_name, my_pv, my_groups, my_channels


def start_chat(request):
    global message_location, n_pv, n_group, n_channel
    if request.method == 'POST':
        print("***********************")
        name = request.POST['name']
        print(str(name) + "***********************")
        if (name.find('group')) and (name.find('channel')):
            print("nots are working correctly***********************")
            if Contacts.objects.filter(password=user_password, name=name):
                valid = Contacts.objects.filter(password=user_password, name=name)
                print(str(valid))
                print("contact**********************")
                message_location = 'private'
                n_pv = name
                user_pv = Private.objects.filter(password=user_password)
                valid1 = user_pv.filter(name=name)
                dialog = valid1.values_list('myMsg', 'contactMsg')
                time = valid1.values_list('msgTime')
                return render(request, 'chat_page.html', {'name': name, 'dialog': dialog, 'time': time})
            elif Private.objects.filter(name=name):
                print("private*****************************")
                valid2 = Private.objects.filter(name=name)
                user_pv = valid2.filter(password=user_password)
                if user_pv:
                    message_location = 'private'
                    n_pv = name
                    dialog = user_pv.values_list('myMsg', 'contactMsg')
                    return render(request, 'chat_page.html', {'dialog': dialog})
                else:
                    return render(request, 'mani_page.html', {'message': 'مخاطبی با این نام ندارید'})
            elif Public.objects.filter(group_name=name):
                print("group*****************************")
                valid3 = PublicInfo.objects.filter(group_name=name)
                user_group = find_me(valid3)
                if user_group:
                    message_location = 'group'
                    n_group = name
                    members = valid3.values_list('mem1_name', 'mem2_name', 'mem3_name', 'mem4_name', 'mem5_name')
                    dialog = Public.objects.values_list('mem1Msg', 'mem2Msg', 'mem3Msg', 'mem4Msg', 'mem5Msg')
                    return render(request, 'chat_page.html', {'dialog': dialog, 'members': members})
                else:
                    return render(request, 'mani_page.html', {'message': 'گروهی با این نام ندارید'})
            elif Channel.objects.filter(channel_name=name):
                print("channel*****************************")
                valid4 = ChannelInfo.objects.filter(channel_name=name)
                user_channel = find_me(valid4)
                if user_channel:
                    message_location = 'channel'
                    n_channel = name
                    members = valid4.values_list('mem1_name', 'mem2_name', 'mem3_name', 'mem4_name', 'mem5_name')
                    dialog = Channel.objects.values_list('adminMsg')
                    return render(request, 'chat_page.html', {'dialog': dialog, 'members': members})
                else:
                    return render(request, 'mani_page.html', {'message': 'کانالی با این نام ندارید'})
            else:
                email = request.POST['email']
                print(email)
                if not(email.find('group')) and not(email.find('channel')):
                    print("new contact*****************************")
                    exists = UserPersonality.objects.filter(email=email)
                    if exists:
                        instance = Contacts()
                        instance.name = name
                        instance.password = user_password
                        instance.email = email
                        instance.save()
                        info = main_page()
                        message = 'مخاطب جدید افزوده شد'
                        return render(request, 'main_page.html', {'message': message, 'my_contacts_email': info[0],
                                                                  'my_contacts_name': info[1], 'pv': info[2],
                                                                  'group_name': info[3], 'channel_name': info[4]})
                    else:
                        return render(request, 'main_page.html', {'message': 'مخاطب فاقد حساب کاربری است'})
                elif email.find('channel'):
                    print("new group*****************************")
                    print(email.find('group'))
                    g_name = email.replace('group', '')
                    if PublicInfo.objects.filter(group_name=g_name):
                        return render(request, 'main_page.html', {'message': 'گروهی با این نام وجود دارد'})
                    else:
                        message_location = 'group'
                        nm2 = request.POST['name']
                        nm3 = request.POST['name2']
                        nm4 = request.POST['name3']
                        nm5 = request.POST['name4']
                        instance = PublicInfo()
                        instance.group_name = g_name
                        instance.mem1_name = user_name
                        instance.mem2_name = nm2
                        instance.mem3_name = nm3
                        instance.mem4_name = nm4
                        instance.mem5_name = nm5
                        instance.save()

                        instance2 = Public()
                        instance2.group_name = email
                        instance2.save()

                        info = main_page()
                        message = 'گروه ایجاد شد'
                        return render(request, 'main_page.html', {'message': message, 'my_contacts_email': info[0],
                                                                  'my_contacts_name': info[1], 'pv': info[2],
                                                                  'group_name': info[3], 'channel_name': info[4]})
                elif email.find('group'):
                    print("new channel*****************************")
                    c_name = email.replace('channel', '')
                    if ChannelInfo.objects.filter(channel_name=c_name):
                        return render(request, 'main_page.html', {'message': 'کانالی با این نام وجود دارد'})
                    else:
                        message_location = 'channel'
                        nm2 = request.POST['name']
                        nm3 = request.POST['name2']
                        nm4 = request.POST['name3']
                        nm5 = request.POST['name4']
                        instance = ChannelInfo()
                        instance.channel_name = c_name
                        instance.mem1_name = user_name
                        instance.mem2_name = nm2
                        instance.mem3_name = nm3
                        instance.mem4_name = nm4
                        instance.mem5_name = nm5
                        instance.save()

                        instance2 = Channel()
                        instance2.channel_name = email
                        instance2.is_admin = True
                        instance2.save()

                        info = main_page()
                        message = 'کانال ایجاد شد'
                        return render(request, 'main_page.html', {'message': message, 'my_contacts_email': info[0],
                                                                  'my_contacts_name': info[1], 'pv': info[2],
                                                                  'group_name': info[3], 'channel_name': info[4]})
    else:
        return render(request, 'main_page.html', {})


def chat_page_pv(my_message):
    print("private func*****************************")
    global n_pv, user_name, user_password
    instance = Private()
    instance.name = n_pv
    instance.password = user_password
    instance.myMsg = my_message
    instance.contactMsg = ''
    instance.msgTime = datetime.datetime.now()
    instance.save()
    # -------------------------create a record for my contact------------------------
    send = UserPersonality.objects.filter(username=n_pv)
    find = send.values_list('password')
    pass_word = Private.objects.filter(password=find)
    instance_s = Private()
    instance_s.name = user_name
    instance_s.password = pass_word
    instance_s.myMsg = ''
    instance_s.contactMsg = my_message
    instance_s.msgTime = instance.msgTime
    instance_s.save()

    pv_n = Private.objects.filter(name=n_pv)
    new_dialog = pv_n.values_list('myMsg', 'contactMsg')
    return new_dialog


def chat_page_group(my_message):
    print("group func*****************************")
    global n_group
    instance = Public()
    instance.group_name = n_group
    instance.msgTime = datetime.datetime.now()
    me = PublicInfo.objects.filter(group_ame=n_group)
    num = find_me(me)
    if num == 1:
        instance.mem1Msg = my_message
    elif num == 2:
        instance.mem2Msg = my_message
    elif num == 3:
        instance.mem3Msg = my_message
    elif num == 4:
        instance.mem4Msg = my_message
    elif num == 5:
        instance.mem5Msg = my_message
    instance.save()

    group_n = Public.objects.values_list(group_name=n_group)
    group_n_info = PublicInfo.objects.filter(group_name=n_group)
    members = group_n_info.values_list('mem1_name', 'mem2_name', 'mem3_name', 'mem4_name', 'mem5_name')
    new_dialog = group_n.values_list('mem1Msg', 'mem2Msg', 'mem3Msg', 'mem4Msg', 'mem5Msg', 'myMsg')
    return new_dialog, members


def find_me(valid):
    if valid.filter(mem1_name=user_name):
        return 1
    elif valid.filter(mem2_name=user_name):
        return 2
    elif valid.filter(mem3_name=user_name):
        return 3
    elif valid.filter(mem4_name=user_name):
        return 4
    elif valid.filter(mem5_name=user_name):
        return 5
    else:
        return 0


def chat_page_channel(my_message):
    print("channel func*****************************")
    global n_channel
    valid = Channel.objects.values_list('is_admin')
    flag = False
    if valid:
        flag = True
        instance = Channel()
        instance.adminMsg = my_message
        instance.channel_name = n_channel
        instance.msgTime = datetime.datetime.now()
        instance.save()

        channel_n = Channel.objects.values_list(channel_name=n_channel)
        channel_n_info = ChannelInfo.objects.filter(channel_name=n_channel)
        members = channel_n_info.values_list('mem1_name', 'mem2_name', 'mem3_name', 'mem4_name',
                                             'mem5_name')
        new_dialog = channel_n.values_list('adminMsg')
        return flag, new_dialog, members
    else:
        return flag


def send_msg(request):
    print("sending*****************************")
    global message_location
    if request.method == 'POST':
        my_message = request.POST['message']
        if message_location == 'private':
            dialog = chat_page_pv(my_message)
            return render(request, 'chat_page.html', {'dialog': dialog})
        elif message_location == 'group':
            dialog, members = chat_page_group(my_message)
            return render(request, 'chat_page.html', {'dialog': dialog, 'members': members})
        else:
            flag, dialog, members = chat_page_channel(my_message)
            if flag:
                return render(request, 'chat_page.html', {'dialog': dialog, 'members': members})
            else:
                return render(request, 'chat_page.html', {})
    else:
        return render(request, 'chat_page.html', {})


"""a1 = Public.objects.filter(id=1)
a2 = a1.values_list("group_name")
print(a2[0][0])"""
