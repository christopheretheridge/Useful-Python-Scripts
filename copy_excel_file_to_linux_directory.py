import os
from shutil import copy2

src = os.path.dirname(os.path.realpath(__file__)) + '/move_me.xlsx'
dst = os.path.dirname(os.path.realpath(__file__)) + '/copy_here'

copy2(src,dst)
