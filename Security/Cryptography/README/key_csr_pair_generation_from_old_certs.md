
# RSA Key and CSR pair generation from old certificate Subject Info details

## Store all the old certs in the same path where the script is located
```bash
$ ll
total 48
-rw-r--r-- 1 rv3h3x rv3h3x  117 Jun 26 14:28 cert_list.txt
-rw-r--r-- 1 rv3h3x rv3h3x 3664 Jun 26 14:49 key_csr_from_old_cert.py
drwxr-xr-x 2 rv3h3x rv3h3x 4096 Jun 26 14:50 output
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_1.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_2.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_3.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_4.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_5.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_6.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_7.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_8.crt
-rw-r--r-- 1 rv3h3x rv3h3x 1391 Jun 26 14:24 server_9.crt
```
## Create a new file called ```cert_list.txt``` and list all the old certs within it.
```bash                                                                                                                                        
$ cat cert_list.txt   
server_1.crt
server_2.crt
server_3.crt
server_4.crt
server_5.crt
server_6.crt
server_7.crt
server_8.crt
server_9.crt
```
## Displaying all the Subject Info from the old certificates
```bash                                                                                                                                        
$ for i in {1..9}; do openssl x509 -in server_${i}.crt -noout -text | grep 'Subject:'; done          
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver1.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver2.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver3.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver4.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver5.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver6.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver7.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver8.company.local
        Subject: C=GB, ST=London, L=London, O=Company, OU=Organization, CN=myserver9.company.local
```
## Running the python script
```bash
$ python key_csr_from_old_cert.py                                                       
New key and CSR for server_1.crt have been saved to output/server_1_key.pem and output/server_1_csr.pem respectively.
New key and CSR for server_2.crt have been saved to output/server_2_key.pem and output/server_2_csr.pem respectively.
New key and CSR for server_3.crt have been saved to output/server_3_key.pem and output/server_3_csr.pem respectively.
New key and CSR for server_4.crt have been saved to output/server_4_key.pem and output/server_4_csr.pem respectively.
New key and CSR for server_5.crt have been saved to output/server_5_key.pem and output/server_5_csr.pem respectively.
New key and CSR for server_6.crt have been saved to output/server_6_key.pem and output/server_6_csr.pem respectively.
New key and CSR for server_7.crt have been saved to output/server_7_key.pem and output/server_7_csr.pem respectively.
New key and CSR for server_8.crt have been saved to output/server_8_key.pem and output/server_8_csr.pem respectively.
New key and CSR for server_9.crt have been saved to output/server_9_key.pem and output/server_9_csr.pem respectively.
```
##  Displaying all the Subject Info from the newly created CSR files.
```bash
$ for i in {1..9}; do openssl req -in output/server_${i}_csr.pem -noout -text | grep 'Subject:'; done
        Subject: CN=myserver1.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver2.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver3.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver4.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver5.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver6.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver7.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver8.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
        Subject: CN=myserver9.company.local, C=GB, ST=London, L=London, O=Company, OU=Organization
```
## Listing all newly created files Keys/CSRs
```bash
$ ll output 
total 72
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_1_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1675 Jun 26 15:35 server_1_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_2_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1679 Jun 26 15:35 server_2_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_3_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1675 Jun 26 15:35 server_3_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_4_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1679 Jun 26 15:35 server_4_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_5_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1675 Jun 26 15:35 server_5_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_6_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1679 Jun 26 15:35 server_6_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_7_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1675 Jun 26 15:35 server_7_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_8_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1679 Jun 26 15:35 server_8_key.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1029 Jun 26 15:35 server_9_csr.pem
-rw-r--r-- 1 rv3h3x rv3h3x 1675 Jun 26 15:35 server_9_key.pem
```
