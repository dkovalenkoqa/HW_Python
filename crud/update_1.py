def update_user(email, item, new_item, users_storage):
    if email in users_storage.keys():
        for key, value in users_storage[email].items():
            if key == item:
                users_storage[email][key] = new_item
