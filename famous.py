#!/usr/bin/python

import random
from subprocess import call
from os import system
# Add some cool people to this list
a = [
    #('username','email@address.com'),
]

random = random.randint(0, len(a)-1)

system('git config --global user.name \"{}\"'.format(a[random][0]))
system('git config --global user.email {}'.format(a[random][1]))

print('You are not commiting as:')
call(['git', 'config', 'user.name'])
call(['git', 'config', 'user.email'])

b = raw_input('Continue :')
#system('echo \"......The end\" >> README.md')
system('git add .')
system('git commit -m \"last update\"')
system('git push')

