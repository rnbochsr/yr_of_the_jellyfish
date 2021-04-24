# Year of the Jellyfish 
> rnbochsr 4/23/2021 

Website IP: 54.229.22.118 URL: https://robyns-petshop.thm
Initial IP may change, but I don't know. It is a public IP.


### Things to try 
 * `nmap` all ports - Done. Found 7 open ports.
 * `wget` website to get code
 * `curl` website to get code
 * BurpSuite to look for cookies
 * Metasploit for CVE analysis
 * MD5 & SHA-1 hashes in `nmap` scan. Crackable??
 * User: `robyn@robyns-petshop.thm`
 * Amazonaws exploits
 * Email server??
 * Figure out how to install the website's certificate from the nmap scan into Firefox
 * Dirbuster
 * Nikto
 * Use the various `Password Attack` options in Kali
 * `ftp` & `sftp` - Done


#### Results that worked
`nmap` of all ports found 7 open ports.
`ftp` didn't connect in a useful manner. It would connect but then I couldn't pass anything. 
`sftp` connected and was interactive!! Now try to use some password cracking for `robyn`, `admin`, & `anonymous`.


#### Things that didn't work
Website won't load. 
Initially couldn't get anything useful from `wget` or `curl` of website.
