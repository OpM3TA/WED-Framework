import sys, os, socket, random, struct, ctypes, binascii,re
from binascii import unhexlify, hexlify
import subprocess
NDISASM = "ndisasm.exe"

def execute(cmd):
    return  subprocess.check_output(cmd, shell=True)
def to_hexstr(a):
    return "".join(["\\x%02x" % ord(i) for i in a])
