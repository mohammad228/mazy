import subprocess
import re


class Search:
    def run(self, wordlist, domain, path):
        domain = domain.rstrip()
        cmd = 'feroxbuster.exe -w ' + wordlist + ' -k -u ' + domain + ' -r --no-state --silent -o ' + path+'_content.txt'
        print(cmd)
        subprocess.call(cmd, shell=True)
