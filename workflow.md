# Workflow for Login Access or Reverse Shells

> Bradley Lubow, rnbochsr | May 2021

---------------------------

## The Basics

### `nmap` the IP.
`nmap -v -p- -oN filename IP` for all ports.
`nmap -v -sV -sC -oN filename IP` for just the top ports. 

Look for: 
* Ports
* Services
* Platform
* Applications
* Additional domains, subdomains, or servers
* Weird items that stick out asking for attention

### Web browsing 
* Main IP, any ports, any domains or subdomains
* Try `http:` and `https:` 
* Modify `/etc/hosts` if the site doesn't load. 
* Look at Website Certificates. Especially if certificate errors, look at cert for additional info.
* Add any new domains or subdomains to `/etc/hosts` as needed.
* Browse all pages and links. View source as you go to look for info.
* Browse to any folders noted in source code.
* Platform, version #'s, etc. 
* Try and scrape details from website that can lead to credentials. 
  * Employee names
  * User names
  * Possible password or directory ideas
* Check for cookies and any values they contain that might be required to bypass security constraints.


### Services
* Try default credentials.
* Try anonymous credentials.
  *Examples:*
  * admin:admin	
  * admin:password
  * anonymous:blank
  * anonymous:anonymous
  * guest:blank
  * guest:guest
  * ftp:blank
  * ftpuser:blank
  * blank:blank


### Check for exploits
* `searchsploit` or `msfconsole` to evaluate possible exploits for all of the things discovered. 
* `searchsploit -m ...` to copy the exploit into the `pwd`. That way you can play with the code without modifying the original.
* Check articles and blog posts about an exploit for addtional information.


### Resources
* `nc -lnvp [port]` to receive reverse shell callbacks.
* VPS for web server if needed.
* `ngrok` to set up web server forwarding to internal local port? Need to look into this program and see what it does.
* `g0tmilk` Privilege Escalation Database
* Mitre CVE Database.
* Exploit Database.
