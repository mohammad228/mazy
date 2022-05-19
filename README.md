# Mazy
It's a tools that create with merging other tools
You can use it for automation scan and include Asset and Content Discovery, Port Scan, Vulnerability Assessment, Technology Detection.

# How to install
## Requirement 
###### Install Amass
Install Amass from [Amass Github page](https://github.com/OWASP/Amass/releases)
###### Install Httpx
Install Amass from [Httpx Github page](https://github.com/projectdiscovery/httpx/releases)
###### Install Naabu
Install Amass from [Naabu Github page](https://github.com/projectdiscovery/naabu/releases)
###### Install Webanalyze
Install Amass from [Webanalyze Github page](https://github.com/rverton/webanalyze/releases)
###### Install Feroxbuster
Install Amass from [Feroxbuster Github page](https://github.com/epi052/feroxbuster/releases)
###### Install Nuclei with Templates
Install Amass from [Nuclei Github page](https://github.com/projectdiscovery/nuclei/releases)

## Install Mazy
```
git clone mohammad228/mazy 
```
# Usage
```
python mazy -h 
```
```
usage: mazy.py [-h] [-d DOMAIN] [-l DOMAINSLIST] [-w WORDLIST] [-nsd NO_SUBDOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        set domain
  -l DOMAINSLIST, --domainslist DOMAINSLIST
                        path list of domain
  -w WORDLIST, --wordlist WORDLIST
                        path of wordlist for content discovery
  -nsd NO_SUBDOMAIN, --no_subdomain NO_SUBDOMAIN
                        no subdomain scan just this domain scan
```

