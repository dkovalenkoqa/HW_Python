def delete_user(email, users_storage):
    if email in users_storage.keys():
        users_storage.pop(email)
        return users_storage