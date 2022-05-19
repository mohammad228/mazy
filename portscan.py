import subprocess


class Naabu:
    domain = ''

    def checkport(self, domain):
        self.domain = domain
        cmd = 'naabu.exe -list results/' + self.domain + '/subResult.txt -tp 100 -o  results/' + self.domain + '/portsScan.txt '
        subprocess.call(cmd, shell=True)
