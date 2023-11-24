#module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

from message import * #improts whole module

import message as msg #imports module with a alias

hello()

bye()

msg.hello()
msg.bye()
