import subprocess
import os
import sys

class SuperScraper:
    
    def __init__(self, headers_raw, url, data=None, proxy=None, filename=None):
        """
        data must be url encoded
        """
        self.headers_raw = headers_raw
        self.headers = {}
        self.filename = filename
        header_lines = filter(lambda x: len(x) > 1, [line.split('\t') for line in \
                                                     headers_raw.split('\n')])
        # Split header line into key value. Discard any inbetween spaces
        for header_line in header_lines:
            hl_elts = filter(lambda header_line: len(header_line) > 1, header_line)
            self.headers[hl_elts[0]] = hl_elts[1]
        self.data = data
        self.url = url
        self.proxy = proxy
            
    def build_curl_cmd(self):
        cmd = ['curl']
        for key, value in self.headers.items():
            cmd.append('-H')
            cmd.append("%s: %s" % (key, value))
        if not(self.data is None):
            cmd.append('-d')
            cmd.append("%s" % self.data)
        if not(self.proxy is None): #127.0.0.1:8888 to use with Charles
            cmd.append("--proxy")
            cmd.append(self.proxy)
            cmd.append("-k") # Using Charles. Fuck it. It's ok if it's unsafe
        if '[' in self.url:
            cmd.append('--globoff')
        cmd.append(self.url)
        return cmd

    def run_cmd(self, cmd):
        print ' '.join(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = p.communicate()
        return out

    def scrape(self):
        cmd = self.build_curl_cmd()
        resp_text = self.run_cmd(cmd)
        return resp_text

