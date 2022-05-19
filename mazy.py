import os
import subfinder
import argparse
import contentdiscovery
import techdetection
import portscan
import vulnerabilityScan
import re

# define global variables
domain = ''
domainslist = ''
wordlist = 'wordlists/seclist2.txt'
no_subdomain = '0'


def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="set domain")
    parser.add_argument("-l", "--domainslist", help="path list of domain")
    parser.add_argument("-w", "--wordlist", help="path of wordlist for content discovery")
    parser.add_argument("-nsd", "--no_subdomain", help="no subdomain scan just this domain scan")
    args = parser.parse_args()
    if args.domain:
        global domain
        domain = args.domain
    if args.domainslist:
        global domainslist
        domainslist = args.domainslist
    if args.wordlist:
        global wordlist
        wordlist = args.wordlist
    if args.no_subdomain:
        global no_subdomain
        no_subdomain = args.no_subdomain

if __name__ == '__main__':
    arg()
    if domain:
        os.mkdir('results/' + domain + '')
        sub = subfinder.Subdomain(domain)
        sub.run()
        ports = portscan.Naabu()
        ports.checkport(domain)
        vul = vulnerabilityScan.Scan()
        vul.nuclei(domain)
        with open('results/' + domain + '/httpxResult.txt') as file:
            for line in file:
                line = line.rstrip()
                subdomain = re.sub('http[s]?://', '', line, flags=re.MULTILINE)
                tech = techdetection.WebAnalyze()
                tech.run(domain, subdomain)
                con = contentdiscovery.Search()
                con.run(wordlist, line, 'results/' + domain + '/' + subdomain)
    if domainslist:
        with open(domainslist) as file:
            for line in file:
                line = line.rstrip()
                os.mkdir('results/' + line + '')
                sub = subfinder.Subdomain(line)
                sub.run()
                ports = portscan.Naabu()
                ports.checkport(line)
                vul = vulnerabilityScan.Scan()
                vul.nuclei(line)
                with open('results/' + line + '/httpxResult.txt') as file2:
                    for line2 in file2:
                        line2 = line2.rstrip()
                        subdomain = re.sub('http[s]?://', '', line2, flags=re.MULTILINE)
                        tech = techdetection.WebAnalyze()
                        tech.run(line, subdomain)
                        con = contentdiscovery.Search()
                        con.run(wordlist, line2, 'results/' + line + '/' + subdomain)
    print("Done")
