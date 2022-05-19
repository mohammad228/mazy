import subprocess
import csv


class WebAnalyze:
    web_server = ''
    reverse_proxy = ''
    programming_language = ''

    def run(self, domain, subdomain):
        cmd = 'webanalyze.exe -host '+domain+' -output csv > results/' + domain + '/' + subdomain + '_pre_techdetect.csv'
        output = subprocess.call(cmd, shell=True)
        # remove empty lines
        with open('results/' + domain + '/' + subdomain + '_pre_techdetect.csv', newline='') as in_file:
            with open('results/' + domain + '/' + subdomain + '_techdetect.csv', 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if any(row):
                        writer.writerow(row)
        #
        with open('results/' + domain + '/' + subdomain + '_techdetect.csv') as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            for row in reader:
                if str(row[1]) == 'Web frameworks,Web servers':
                    self.web_server = str(row[2])
                if str(row[1]) == 'Web servers,Reverse proxies':
                    self.reverse_proxy = str(row[2])
                if str(row[1]) == 'Programming languages':
                    self.programming_language = str(row[2])
