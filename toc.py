#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

root = '.'

print('Notes Overview')
print('==============')

print('')

for path, subdirs, files in os.walk(root):

    subdirs.sort()
    files.sort()

    if '.git' in path or '.idea' in path:
        continue
    print('')
    if path is '.':
        print('# Personal Notes')
    else:
        print( '# ' + path.replace('./', '').title() )
    print('')
    for name in files:
        if 'toc.py' in name or '.git' in name:
            continue
        total_path = str(os.path.join(path, name))

        print ('- [' + name.replace('.md', '').title() + '](' + (os.path.join(path, name)) + ')')
