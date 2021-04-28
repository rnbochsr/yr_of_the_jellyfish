# Year of the Jellyfish (YotJF)
> rnbochsr 4/23/2021 

## Target configuration info

 * Website IP changes each time the machine spins up. 
 * URL: `https://robyns-petshop.thm`
 * Website Platform: AmazonAWS. *Version #?*
 * Web server: Apache 2.4.29 Ubuntu.
 * Site runs using Picocms. *Version #?*
 * OpenSSH 8.4.p1
 * OpenSSL 1.1.1k

### CVE List
Apache 2.4.29
 * CVE-2018-1312	Apache httpd 2.2.0 - 2.4.29
 * CVE-2018-1283	Apache httpd 2.4.0 - 2.4.29
 * CVE-2017-15715	Apache httpd 2.4.0 - 2.4.29
 * CVE-2017-15710	Apache httpd 2.4.0 - 2.4.29

PicoCMS
 * CVE-2008-6604	PicoFlat CMS 0.5.9
 * CVE-2007-5920	PicoFlat CMS pre 0.4.18
 * CVE-2007-5390	PicoFlat CMS 0.4.14 and earlier

Amazon AWS lists 28 CVEs. 

OpenSSH 8.4.p1 lists 129 CVEs.
 * CVE-2020-14145	OpenSSH 5.7 - 8.4 Newest listing

OpenSSL 1.11k
 * CVE-2021-3450	OpenSSL 1.1.1k
 * CVE-2021-3449	OpenSSL 1.1.1k


### Things to try 
 * `nmap` all ports - Done. Found 7 open ports.
 * Modify `/etc/hosts` file to add the machine IP so the DNS will resolve and display the website. 
 * `wget` website to get code - Initial results don't show much.
 * `curl` website to get code - Initial results don't show much.
 * BurpSuite to look for cookies
 * Metasploit for CVE analysis
 * MD5 & SHA-1 hashes in `nmap` scan. Crackable??
 * Users: Robyn MacKenzie `robyn@robyns-petshop.thm`
	`admin@robyns-petshop.thm`
	`staff@robyns-petshop.thm`

 * AmazonAWS exploits
 * Email server??
 * Figure out how to install the website's certificate from the nmap scan into Firefox
 * Dirbuster - In process. See dirbuster_output.md for listing and notes.
 * Gobuster `-k` flag? `gobuster -k dir -u http://<IP> -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt`
 * Hydra
 * Nitko
 * Use various `password attack` options in Kali
 * `ftp` & `sftp` - In process
 * Don't forget OSINT


### Notes and possible additional resources
 * `https://github.com/wwong99/pentest-notes/blob/master/oscp_resources/OSCP-Survival-Guide.md#enumeration`
 * `https://github.com/theonlykernel/enumeration/wiki`
 * `https://github.com/theonlykernel/EasyEnumeration/wiki`
 * Possible new 0day exploit 4/25/21. I read it as LATimes, but it is LATlmes. Use caution if I pursue this. Might be a malicious website. `https://www.latlmes.com/tech/the-ultimate-0day-1` <= Rickroll!
 * Honeypot `https://github.com/cowrie/cowrie`


### Results that worked
 * `http://robyns-petsshop.thm:8000` gets you to a page that says enter your ID `...:8000/ID_Here`. `robyn`, `admin`, & `staff` don't work. Look for other options.
 * `https://robyns-petshop.thm/business` is a login page. It is asking for `Business Credentials Please`. User Name/password.
 * `nmap` of all ports found 7 open ports.
 * `ftp` didn't connect in a useful manner from my IP. It would connect but then I couldn't pass anything. 
 * `sftp` connected and was *interactive!!* Now try to use some password cracking for `robyn`, `admin`, & `anonymous`.
 * Modifying the `/etc/hosts` file allowed the website to load! Remember this for future pentests.
 * `ftp` on the Kali attack box connects without any issues. It allowed me to interact. Now to see if I can brute the password.


#### Things that didn't work
Website won't load. Domain doesn't resolve until `/etc/hosts` updated. Initially didn't get anything useful from `wget` or `curl` of website.
Hashcat couldn't crack the MD5 from the `nmap` scan. That was disappointing. Hoped it was a site or user specific password. O

