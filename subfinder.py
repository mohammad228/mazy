import subprocess
import re


class Subdomain:

    def __init__(self, domain):
        self.domain = domain

    def run(self):
        self.sublist()
        self.liveness()
        self.reformat_file()
        self.subdomain_takeover()

    def sublist(self):
        cmd = 'amass enum -nolocaldb -noalts -timeout 3 -d ' + self.domain + ' -o results/' + self.domain + '/subResult.txt'
        # cmd = 'python sublist3r.py -d ' + self.domain + ' -o results/' + self.domain + '/subResult.txt'
        # print(cmd)
        subprocess.call(cmd, shell=True)

    def liveness(self):
        cmd = 'httpx -l results/' + self.domain + '/subResult.txt -fc 500,501,502,503,504 -o results/' + self.domain + '/httpxResult.txt'
        # print(cmd)
        subprocess.call(cmd, shell=True)

    def subdomain_takeover(self):
        cmd = 'subjack -w results/' + self.domain + '/subResult.txt -t 100 -timeout 30 -o results/' + self.domain + '/subtakeResult.txt'
        subprocess.call(cmd, shell=True)

    def reformat_file(self):
        with open('results/' + self.domain + '/httpxResult.txt') as file1, open(
                'results/' + self.domain + '/reformat.txt', 'w') as file2:
            for line in file1:
                text = re.sub('http[s]?://', '', line, flags=re.MULTILINE)
                file2.writelines(text)
