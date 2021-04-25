#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("machine_ip")	# Host info
ftp.set_debuglevel(2)		# Set error reporting level
ftp.connect()			# Connect
ftp.login()			# user anonymous, passwd anonymous@
ftp.dir()			# Directory listing
ftp.close()			# Close connection



# ftp.cwd('debian')             # change into "debian" directory
# ftp.retrlines('LIST')         # list directory contents

# with open('README', 'wb') as fp:
#     ftp.retrbinary('RETR README', fp.write)

# ftp.quit()
