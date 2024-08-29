user_info = {
    'list_a' : ['first name', 'last_name', 'role'],
    'list_b' : ['Jose', 'Monge', 'Student']
}

for index in range(len(user_info['list_a'])):
    print(f"{user_info['list_a'][index]}: {user_info['list_b'][index]}")