users = []
status = []

def auth(task, username, password):
    global users
    global status
    if task == 'register':
        for user in users:
            if username in user[0]:
                return 'Username already exists.'
        user = [username, password]
        users.append(user)
        return 'Register successfully.'
    elif task == 'login':
        for userInfo in users:
            if username == userInfo[0] and password == userInfo[1]:
                status.append([username, True])
                return 'Logged In Successfully.'
        return 'Login Unsuccessful.'
    elif task == 'logout':    
        for i in range(len(status)):
            if username == status[i][0] and status[i][1]:
                status[i][1] = False
                return 'Logged Out Successfully'
        return 'logout Unsuccessful.'
    return 'Try again.'

task = 'register'
username = 'user05'
password = 'qwerty'
print(auth(task, username, password))

task = 'register'
username = 'user05'
password = 'qwerty'
print(auth(task, username, password))

task = 'login'
username = 'user05'
password = 'qwerty'
print(auth(task, username, password))

task = 'login'
username = 'user'
password = 'qwerty'
print(auth(task, username, password))

task = 'logout'
username = 'user05'
password = '-'
print(auth(task, username, password))


task = 'logout'
username = 'user05'
password = '-'
print(auth(task, username, password))

