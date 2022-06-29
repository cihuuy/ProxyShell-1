# ProxyShell
CVE-2021-34473 Microsoft Exchange Server Remote Code Execution Vulnerability



### CVE-2021-34473 - Pre-auth Path Confusion
This faulty URL normalization lets us access an arbitrary backend URL while running as the Exchange Server machine account. Although this bug is not as powerful as the SSRF in ProxyLogon, and we could manipulate only the path part of the URL, it’s still powerful enough for us to conduct further attacks with arbitrary backend access.
```
https://xxx.xxx.xxx.xxx/autodiscover/autodiscover.json?@foo.com/mapi/nspi/?&Email=autodiscover/autodiscover.json%3f@foo.com
```

1) CVE-2021-34523 - Exchange PowerShell Backend Elevation-of-Privilege
2) CVE-2021-31207 - Post-auth Arbitrary-File-Write



### Features
* No email address needs to be supplied
* Attempts to enumerate emails from Active Directory
* Attempts to enumerate LegacyDNs from Active Directory
* Attempts to discover LegacyDNs from builtin emails
* Attempts to discover SID of Exchange server in load-balanced deployments
* Handles exploitation in load-balanced environments
