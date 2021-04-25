# Year of the Jellyfish (YotJF)
> rnbochsr 4/23/2021 

## Target configuration info

 * Website IP changes each time the machine spins up. 
 * URL: https://robyns-petshop.thm
 * Apache 2.4.29 Ubuntu 


### Things to try 
 * `nmap` all ports - Done. Found 7 open ports.
 * Modify `/etc/hosts` file to add the machine IP so the DNS will resolve and display the website. 
 * `wget` website to get code
 * `curl` website to get code
 * BurpSuite to look for cookies
 * Metasploit for CVE analysis
 * MD5 & SHA-1 hashes in `nmap` scan. Crackable??
 * User: Robyn MacKenzie `robyn@robyns-petshop.thm`
 * Amazonaws exploits
 * Email server??
 * Figure out how to install the website's certificate from the nmap scan into Firefox
 * Dirbuster
 * Nikto
 * Use the various `Password Attack` options in Kali
 * `ftp` & `sftp` - In process
 * Don't forget OSINT


### Results that worked
 * `nmap` of all ports found 7 open ports.
 * `ftp` didn't connect in a useful manner from my IP. It would connect but then I couldn't pass anything. 
 * `sftp` connected and was *interactive!!* Now try to use some password cracking for `robyn`, `admin`, & `anonymous`.
 * Modifying the `/etc/hosts` file allowed the website to load! Remember this for future pentests.
 * `ftp` on the Kali attack box connects without any issues. It allowed me to interact. Now to see if I can brute the password.


#### Things that didn't work
Website won't load. Initially couldn't get anything useful from `wget` or `curl` of website.
Hashcat couldn't crack the MD5 from the `nmap` scan.
