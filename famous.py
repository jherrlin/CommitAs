#!/usr/bin/python

import random
from subprocess import call
from os import system
# Add some cool people to this list
people = [
    #('username','email@address.com'),
]

message = [
    'Fix this shit up',
    'Add Elvis operator',
    '10 * nested loop',
    'To drunk....',
    'Writing som heavy code',
    'Commiting like a pro',
    'Git is the sh*t',
    'I can kive',
    'Cobol is easy',
    'removing all tests',
    'changed all variables to a,b,c,...',
    'rm -rf /'
]

#random = random.randint(0, len(people)-1)

#system('git config --global user.name \"{}\"'.format(people[random][0]))
#system('git config --global user.email {}'.format(people[random][1]))

print('You are not commiting as:')
call(['git', 'config', 'user.name'])
call(['git', 'config', 'user.email'])

b = raw_input('Continue :')

random = random.randint(0, len(message)-1)
system('echo \"yeah\" >> README.md')
system('git add .')
system('git commit -m \"{}\"'.format(message[random]))
system('git push')
system('sed -i \'$s/yeah$//\' README.md')

