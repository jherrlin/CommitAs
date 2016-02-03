#!/usr/bin/python

import random
from subprocess import call
from os import system
# Add some cool people to this list
people = [
    #('username','email@address.com'),
]

message = [
    'Add Elvis operator',
    '10 * nested loop',
    'Writing som heavy code',
    'Commiting like a pro',
    'I can jive',
    'Cobol is easy',
    'removing all tests',
    'changed all variables to a,b,c,...',
]

ranint = random.randint(0, len(people)-1)

system('git config --global user.name \"{}\"'.format(people[ranint][0]))
system('git config --global user.email {}'.format(people[ranint][1]))

print('You are not commiting as:')
call(['git', 'config', 'user.name'])
call(['git', 'config', 'user.email'])

b = raw_input('Continue :')

ranint = random.randint(0, len(message)-1)
system('echo \"yeah\" >> README.md')
system('git add .')
system('git commit -m \"{}\"'.format(message[ranint]))
system('git push')
system('sed -i \'$s/yeah$//\' README.md')

