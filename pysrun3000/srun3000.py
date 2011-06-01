import pycurl
import StringIO
import urllib

b = StringIO.StringIO()
c = pycurl.Curl()

def reset():
    b.truncate(0)
    c.reset()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    
def get_mac():
    from uuid import uuid1
    mac = uuid1().hex[-12:]
    mac = list(mac)
    for i in (10, 8, 6, 4, 2):
        mac.insert(i, ':')
    return ''.join(mac)
        
def login(host, mac, username, password):
    reset()
    c.setopt(pycurl.URL, 'http://%s:3333/cgi-bin/do_login' % host)
    c.setopt(pycurl.POST, True)
    c.setopt(pycurl.POSTFIELDS, urllib.urlencode({
        'username': username,
        'password': password,
        'mac': mac,
        'n': '99',
        'type': '3',
        'drop': '0',
    }))
    c.perform()
    return b.getvalue()
    
def logout(host, uid):
    reset()
    c.setopt(pycurl.URL, 'http://%s:3333/cgi-bin/do_logout' % host)
    c.setopt(pycurl.POST, True)
    c.setopt(pycurl.POSTFIELDS, urllib.urlencode({
        'uid': uid,
    }))
    c.perform()
    return b.getvalue()
    
uid = login('202.112.136.131', get_mac(), 'username', 'password')
print uid
#print logout('202.112.136.131', uid)
