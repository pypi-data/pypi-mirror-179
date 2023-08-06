# ScrapingHelper

This library intends to make parsing HTML with using request_html.
So, When using this library you automatically get (same as request_html):

- **Full JavaScript support**!
- *CSS Selectors* (a.k.a jQuery-style, thanks to PyQuery).
- *XPath Selectors*, for the faint of heart.
- Mocked user-agent (like a real web browser).
- Automatic following of redirects.
- Connection– pooling and cookie persistence.
- The Requests experience you know and love, with magical parsing abilities.
- **Async Support**

And new features.

- URL / PROXY parser with validator.
- UserAgent manager using collected real user-agents.
- proxy rotation suppport.
- access with random wait time
- shell environment options.
- logging support.

## Tutorial and Usage

### class URL

 - validator()
 - unquote() / decode()
 - enquote() / encode()


```python
In [1]: from scrapinghelper import URL

In [2]: u = URL()

In [3]: u.validator('http://sample.om')
Out[3]: True

In [4]: u.validator('http://sample.')
Out[4]: False

In [5]: url = URL('http://www.example.com/sample?src=git&encode=jp')

In [6]: url.is_valid
Out[6]: True

In [7]: url.attrs
Out[7]:
{'url': 'http://www.example.com/sample?src=git&encode=jp',
 'is_valid': True,
 'scheme': 'http',
 'netloc': 'www.example.com',
 'username': None,
 'password': None,
 'hostname': 'www.example.com',
 'port': None,
 'path': '/sample',
 'params': '',
 'query': 'src=git&encode=jp',
 'fragment': '',
 'basename': 'sample'}

In [8]: url = URL('http://www.example.com/データ.txt')

In [9]: url.attrs
Out[9]:
{'url': 'http://www.example.com/%E3%83%87%E3%83%BC%E3%82%BF.txt',
 'is_valid': True,
 'scheme': 'http',
 'netloc': 'www.example.com',
 'username': None,
 'password': None,
 'hostname': 'www.example.com',
 'port': None,
 'path': '/%E3%83%87%E3%83%BC%E3%82%BF.txt',
 'params': '',
 'query': '',
 'fragment': '',
 'basename': 'データ.txt'}

In [10]: url.query
Out[10]: 'src=git&encode=jp'

In [11]: url.get_query_val('src')
Out[11]: 'git'

In [12]: url.set_query_val('src', 'csv')
Out[12]: 'http://www.example.com/sample?src=csv&encode=jp'

In [13]: url
Out[13]: http://www.example.com/sample?src=git&encode=jp

In [14]: url.set_query_val('src', 'csv',update=True)
Out[14]: 'http://www.example.com/sample?src=csv&encode=jp'

In [15]: url
Out[15]: http://www.example.com/sample?src=csv&encode=jp

In [16]: url.get_root_address()
Out[16]: 'http://www.example.com'

In [17]: url.strip_query()
Out[17]: 'http://www.example.com/sample'

In [18]: url = URL('https://ja.wikipedia.org/wiki/日本語')

In [19]: url
Out[19]: https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E

In [20]: url.unquote()
Out[20]: 'https://ja.wikipedia.org/wiki/日本語'

In [21]: url.decode()
Out[21]: 'https://ja.wikipedia.org/wiki/日本語'

```

### class UserAgent

 - load_datafile(keep_user_agents: int=50, datapath: Optional[str]=None)
 - get_random_user_agent()
 - get_next_user_agent()

 attributes
 - first_user_agent

### class Scraper

 -  get_random_user_agent()  pass to UserAgent.get_random_user_agent()
 -  get_random_ipv4()
 -  get_random_ipv6()
 -  request()
 -  request_async()
 -  get_filename()
 -  get_links()
 -  get_texts()
 -  download_file()


```python
n [1]: from scrapinghelper import Scraper

In [2]: sc = Scraper()

In [3]: sc.get_random_user_agent()
Out[3]: 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

In [4]: sc.get_random_user_agent()
Out[4]: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/'

In [5]: sc.get_random_user_agent()
Out[5]: 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

In [6]: sc.get_random_user_agent()
Out[6]: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

In [7]: sc.get_random_user_agent()
Out[7]: 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'

In [8]: sc.get_random_user_agent()
Out[8]: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

In [9]: sc.get_random_user_agent()
Out[9]: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

In [10]: sc.get_random_ipv4()
Out[10]: '121.162.233.190'

In [11]: sc.get_random_ipv4()
Out[11]: '178.172.98.169'

In [12]: sc.get_random_ipv6()
Out[12]: '3d18:cb77:5387:3ee9:1e60:d5f3:d987:283a'

In [13]: sc.get_random_ipv6()
Out[13]: 'cfc1:a00d:9013:37a0:ed94:5e92:7fe7:e356'

In [14]:
```

the request headers with user agents will be automatically created.

```python
In [1]: # %load examples/check_headers.py
   ...: import scrapinghelper as sch
   ...: from pprint import pprint
   ...:
   ...: scraper = sch.Scraper()
   ...: response = scraper.request('http://httpbin.org/headers')
   ...:
   ...: pprint(response.json())
{'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             'Accept-Encoding': 'gzip, deflate, br',
             'Accept-Language': 'en',
             'Host': 'httpbin.org',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) '
                           'AppleWebKit/600.1.4 (KHTML, like Gecko) '
                           'Mobile/12B440',
             'X-Amzn-Trace-Id': 'Root=1-62de3626-07daf491262b96356486884d'}}

In [2]:
```

**[Important note regardings trie]

the datasets of UserAgents from [51Degrees/DeviceDetection](https://github.com/51Degrees/device-detection-data).
data file '20000 User Agents.csv' is licenced under the European Union Public Licence V.1.2.

```python
from scrapinghelper import Scraper

scrapper = Scraper(datapath="path_to_new_user_agent_csvfile")
  # ...
```

or set shell Environmnet "SCRAPINGHELPER_USERAGENT_PATH".

```bash
export SCRAPINGHELPER_USERAGENT_PATH="/path/to/new_user_agent_csvfile"
```

```python
In [2]: from scrapinghelper import URL, Scraper, LogConfig
   ...:
   ...: logconfig = LogConfig()
   ...: logconfig.level = 'INFO'
   ...: sc = Scraper(logconfig=logconfig)
   ...:
   ...: url = URL('https://www.houjin-bangou.nta.go.jp/download/zenken/#csv-unic
   ...: ode')
   ...: response = sc.request(url)
   ...:
   ...: content = response.content
   ...: print(f'code: {response.status_code}')
   ...:
code: 200
```

```python
In [2]: # %load examples/yahoo_finance.py
   ...: from typing import Any
   ...: import numpy as np
   ...: from scrapinghelper import Scraper, URL
   ...:
   ...: MARKET_SUMMARY = (
   ...:     '#market-summary > div > div.D\(ib\).Fl\(start\).W\(100\%\) '
   ...:     '> div.Carousel-Mask.Pos\(r\).Ov\(h\).market-summary'
   ...:     '.M\(0\).Pos\(r\).Ov\(h\).D\(ib\).Va\(t\) > ul'
   ...: )
   ...:
   ...: class YHFinance(Scraper):
   ...:     Finance = URL('https://finance.yahoo.com/')
   ...:
   ...:     def __init__(self, **kwargs: Any):
   ...:         super().__init__(browser_args='--incognito', **kwargs)
   ...:         self.response = self.request(self.Finance.url)
   ...:
   ...:     def get_market_summary(self)->list:
   ...:         contents = self.get_texts(MARKET_SUMMARY)[0]
   ...:         return contents
   ...:
   ...: if __name__ == '__main__':
   ...:     from scrapinghelper.utils import split_chunks
   ...:
   ...:     yahoo = YHFinance()
   ...:     summary = yahoo.get_market_summary()
   ...:     for data in split_chunks(summary, 5):
   ...:         print(data)
   ...:
['S&P Futures', '', '4,215.50', '-16.00', '(-0.38%)']
['Dow Futures', '', '33,583.00', '-123.00', '(-0.36%)']
['Nasdaq Futures', '', '13,207.00', '-61.50', '(-0.46%)']
['Russell 2000 Futures', '', '1,952.70', '-6.40', '(-0.33%)']
['Crude Oil', '', '89.87', '-0.90', '(-0.99%)']
['Gold', '', '1,759.70', '-3.20', '(-0.18%)']

In [3]:
```

```python

In [3]: from scrapinghelper import Scraper, LogConfig
   ...:
   ...: logconfig = LogConfig()
   ...: logconfig.level = 'DEBUG'
   ...: sc = Scraper(logconfig=logconfig)
   ...:
   ...: url = URL('https://www.houjin-bangou.nta.go.jp/download/zenken/#csv-unic
   ...: ode')
   ...: response = sc.request(url)
   ...:
   ...: content = response.content
   ...: print(f'code: {response.status_code}')
2022-06-02T19:34:31.885790+0900 LOG configure: {'handlers': [{'sink': <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>, 'level': 'DEBUG', 'format': '<green>{time}</green> <level>{message}</level>', 'colorize': True, 'serialize': False}]}
2022-06-02T19:34:31.886414+0900 URL: https://www.houjin-bangou.nta.go.jp/download/zenken/#csv-unicode
2022-06-02T14:34:32.092599+0900 response status_code: 200
code: 200

In [4]: logconfig
Out[4]: LogConfig(sink=None, level=DEBUG, format=<green>{time}</green> <level>{message}</level>, colorize=True, serialize=False

In [5]:
```

## render() and PROXY
if passed `render=False`, `request()` skip call `render()`.
`render()` of requests-html does not work with proxy.
scrapinghelper support `render()` with proxy.

```python
In [2]: # %load examples/check_ipaddress.py
   ...: from scrapinghelper import Scraper, ProxyManager, ProxyRotate
   ...:
   ...: # tiny socks5 proxy
   ...: proxies = [ 'socks5://127.0.0.1:9050']
   ...: url = 'https://httpbin.org/ip'
   ...:
   ...: scraper = Scraper(proxies=proxies)
   ...:
   ...: # default proxy_rotate is ProxyRotate.NO_PROXY
   ...: # does not call render()
   ...: response = scraper.request(url, render=False)
   ...: print(response.html.text)
   ...:
   ...: # using next proxy server.
   ...: response = scraper.request(url, proxy_rotate=ProxyRotate.NEXT, render=Fa
   ...: lse)
   ...: print(response.html.text)
   ...:
   ...: # using current proxy server.
   ...: response = scraper.request(url, proxy_rotate=ProxyRotate.KEEP, render=Fa
   ...: lse)
   ...: print(response.html.text)
   ...:
   ...: # using random proxy server.
   ...: response = scraper.request(url, proxy_rotate=ProxyRotate.RANDOM)
   ...: print(response.html.text)
   ...:

{ "origin": "221.186.103.38" }
{ "origin": "185.220.101.182" }
{ "origin": "185.220.101.182" }
{ "origin": "185.220.101.182" }

In [3]:
```

## PROXY

Get public proxies list from url.
default is [github.com/hookzof](https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt).
Please keep in mind, there proxies are ABSOLUTELY NO WARRANTY.

```python
In [1]: from scrapinghelper import ProxyManager, PROXY

In [2]: pm = ProxyManager()

In [3]: pm.load_proxies('https://raw.githubusercontent.com/hookzof/socks5_list/m
   ...: aster/proxy.txt', proxy_type='socks5')

In [4]: pm.proxies[:5]
Out[4]:
['101.67.215.147:44844',
 '103.110.84.199:7497',
 '103.108.228.185:7497',
 '103.74.121.46:27102',
 '1.57.21.59:7302']

In [5]: pm.proxy_pool
Out[5]: <itertools.cycle at 0x11bdd1b80>

In [6]: pm.next_proxy()
Out[6]: 101.67.215.147:44844

In [7]: pm.next_proxy()
Out[7]: 103.110.84.199:7497

In [8]: pm.random_proxy()
Out[8]: 72.210.252.134:46164

In [9]: pm.random_proxy().proxy_map
Out[9]: {'http': 'socks5://1.57.21.59:7302', 'https': 'socks5://1.57.21.59:7302'}

In [10]: pm.current_proxy
Out[10]: 1.57.21.59:7302

In [11]: pm.current_proxy.attrs
Out[11]:
{'proxy_url': '1.57.21.59:7302',
 'is_valid': True,
 'scheme': 'socks5',
 'netloc': '1.57.21.59:7302',
 'username': None,
 'password': None,
 'hostname': '1.57.21.59',
 'port': 7302,
 'proxy_map': {'http': 'socks5://1.57.21.59:7302',
  'https': 'socks5://1.57.21.59:7302'}}

In [12]:

```

you can filename as url. i.e.:

```python
p = ProxyManager('file://./myproxy_list.txt')
```

there uri expand as follows.

```python
        if proxies_url.startswith('file://.'):
            proxies_url = proxies_url.replace('file://.','')
            this_directory = Path(__file__).parent
            proxies_url = 'file://{}/{}'.format(this_directory, proxies_url)
```

  **CAUTION**
  if you use a free proxy to login to something or enter personal information and POST it, you must be assured that it will be leaked.
  Keep in mind, it is like writing your credit card number and security code on a postcard.


## KNOWN PROBLEM
if you want to use this module(and/or requests_html, selenium) on ubuntu, you should add system libraries. try folloings.

```bash
sudo apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
```

See Also: https://techoverflow.net/2020/09/29/how-to-fix-pyppeteer-pyppeteer-errors-browsererror-browser-closed-unexpectedly/

