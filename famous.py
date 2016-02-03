#!/usr/bin/python

import random
from subprocess import call

# Add more cool people to this list
a = [
    #('username','email@address.com'),
    ('jherrlin','jherrlin@gmail.com'),
]

random = random.randint(0, len(a)-1)

call(['git', 'config', '--global', 'user.name', a[random][0]])
call(['git', 'config', '--global', 'user.email', a[random][1]])
print('You are not commiting as:')
call(['git', 'config', 'user.name'])
call(['git', 'config', 'user.email'])


