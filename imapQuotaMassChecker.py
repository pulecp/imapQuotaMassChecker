#!/usr/bin/python
        
# Source: http://segfault.in/2010/07/check-your-imap-quota-using-python-imaplib/
# or: http://pastebin.com/raw.php?i=yJje6Ua0	
    
import getpass, imaplib, re

def check(IMAP_USER, IMAP_PASS):
    p = re.compile('\d+')
      
    IMAP_SERVER='imap.yourserver.com'	# CHANGE
    IMAP_PORT=993
	      
    M = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    M.login(IMAP_USER, IMAP_PASS)
    quotaStr = M.getquotaroot("INBOX")[1][1][0]
    r = p.findall(str(quotaStr))
    if r == []:
      print("Unlimited Quota Account")
      r.append(0)
      r.append(0)

    print('use: %8.3f from %11.3f MB'.rjust(20) %(float(r[0])/1024, float(r[1])/1024))

    M.logout()

f = open('./mail_accounts.txt', 'r')
for line in f:
    name, password = line.split()
    print('%20s '%name, end = ' ')
    check(name,password)
f.close()
input("press Enter any key to exit")
