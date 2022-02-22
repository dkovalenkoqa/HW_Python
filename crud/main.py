from create_1 import create_user
from read_1 import user_info, all_users_info
from update_1 import update_user
from delete_1 import delete_user

user_emails = []
users_storage = {}

while True:

    action = input('Please enter action: ')

    if action == 'create':

        print('action = ', action)

        email = input('Email: ')
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
        print('action = ', action)

        all_users_info(users_storage)

    elif action == 'read_user':
        user_e = input('Enter user email: ')
        message = user_info(user_e, user_emails, users_storage)

        print('action = ', action)
        print(f'User: \n {message}')

    elif action == 'update':
        print('action = ', action)

        user_e = input('Enter email of user you want to update: ')
        user_item = input('Enter user info you want to change: ')
        new_item = input(f'Enter new {user_item}: ')

        update_user(user_e, user_item, new_item, users_storage)

        print(user_info(user_e, user_emails, users_storage))

    elif action == 'delete':
        print('action = ', action)
        user_e = input('Enter email of user you want to delete: ')

        print(delete_user(user_e, users_storage))


    else:
        print('Please enter create or read, or update, or delete')
