#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("target_ip") 	# Host info
ftp.set_debuglevel(2)		# Set error reporting level
ftp.connect()			# Connect
ftp.login()			# user anonymous, passwd anonymous@
ftp.dir() 			# File listing
ftp.close()			# Close connection





# Ideas
# from ftplib import FTP
# ftp = FTP('ftp.us.debian.org')  # connect to host, default port
# ftp.login()                     # user anonymous, passwd anonymous@

# ftp.cwd('debian')               # change into "debian" directory
# ftp.retrlines('LIST')           # list directory contents

# with open('README', 'wb') as fp:
#     ftp.retrbinary('RETR README', fp.write)

# ftp.quit()
