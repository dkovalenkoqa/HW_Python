def user_info(email, user_emails, users_storage):
    if email in user_emails:

        message = f'user_email = {email} \n user_info = {users_storage[email]}'

        return message
    else:
        message = 'No user with email: ', email
        return message


def all_users_info(users_storage):
    for key, value in users_storage.items():
        user_email = f'User_email: {key}'
        user_info_1 = f'User_info: {value}'

        print(f'{user_email} \n {user_info_1}')
