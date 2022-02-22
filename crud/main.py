from create_1 import create_user
from read_1 import user_info, all_users_info
from update_1 import update_user
from delete_1 import delete_user
from help_1 import user_help

user_emails = []
users_storage = {}

help_descr = {
    'create' : 'this command create new user',
    'read' : 'this command write info about user',
    'read_all' : 'this command write info about all users',
    'update' : 'this command update info about user',
    'delete' : 'this command delete user from storage'
}

while True:

    action = input('Please enter action: ')

    if action == 'create':

        email = input('Email: ')
        if email in users_storage.keys():
            print('Пользоветель с такой почтой уже существует')
            continue
        name = input('Name: ')
        password = input('Password: ')
        phone = input('Phone: ')

        create_user(email,
                    name,
                    password,
                    phone,
                    user_emails,
                    users_storage)

        print('users_email: ', user_emails)
        print('users_storage: ', users_storage)

    elif action == 'read_all':
        all_users_info(users_storage)

    elif action == 'read_user':
        user_e = input('Enter user email: ')
        message = user_info(user_e, user_emails, users_storage)

        print(f'User: \n {message}')

    elif action == 'update':
        user_e = input('Enter email of user you want to update: ')
        user_item = input('Enter user info you want to change: ')
        new_item = input(f'Enter new {user_item}: ')

        update_user(user_e, user_item, new_item, users_storage)

        print(user_info(user_e, user_emails, users_storage))

    elif action == 'delete':
        user_e = input('Enter email of user you want to delete: ')

        print(delete_user(user_e, users_storage))

    elif action == 'help':
        user_help(help_descr)

    else:
        print('Please enter create or read, or update, or delete')
