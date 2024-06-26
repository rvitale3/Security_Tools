
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
