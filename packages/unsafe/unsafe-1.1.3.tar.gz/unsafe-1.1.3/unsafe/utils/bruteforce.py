from unsafe.utils.strings import aspx_login, asp_login, php_login, html_login, cgi_login, brf_login, cfm_login, js_login, slash_login, ua
import requests
import random
from threading import Thread

founded = []

class BruteForcer:

    def __init__(self) -> None:
        pass
    
    def send_req_admin_finder(self, domain: str, timeout: int, links: list, user_agent: str | None = None,
              cookie: str | None = None, proxy: str | None = None, proxies: list | None = None):

        if "http://" in domain:
            domain = domain.replace("http://", "")
        elif "https://" in domain:
            domain = domain.replace("https://", "")
        else:
            pass
        domain = "http://" + domain
        global founded
        for i in links:
            try:
                if proxy:
                    proxy = {"http": "http://" +
                             str(proxy), "https": "http://" + str(proxy)}
                elif proxies:
                    random_proxy = random.choice(proxies)
                    proxy = {
                        "http": "http://" + str(random_proxy), "https": "http://" + str(random_proxy)}
                if not user_agent:
                    user_agent = random.choice(ua)
                header = {"User-Agent": user_agent}
                if cookie:
                    header.update({"Cookie": cookie})
                if domain[len(domain) - 1] == "/":
                    domain = domain[0: len(domain) - 1]

                full_link = domain + i
                try:
                    if proxy or proxies:
                        r = requests.get(
                            full_link,
                            headers=header,
                            allow_redirects=False,
                            proxies=proxy,
                            timeout=timeout,
                            verify=False,
                        )
                    else:
                        r = requests.get(
                            full_link,
                            headers=header,
                            allow_redirects=False,
                            timeout=timeout,
                            verify=False,
                        )
                except Exception as e:
                    if len(founded) >= 1:
                        return founded
                    else:
                        return e
                if r.status_code == 200:
                    founded.append(full_link)
                else:
                    pass
            except KeyboardInterrupt:
                break
        return founded

    def admin_finder(self, domain: str, workers: int = 3, timeout: int = 10, ext: str = "php", user_agent: str | None = None,
              cookie: str | None = None, proxy: str | None = None, proxies: list | None = None):
        links = []
        ext = ext.strip().lower()
        if ext == "php":
            links = php_login
        elif ext == "asp":
            links = asp_login
        elif ext == "aspx":
            links = aspx_login
        elif ext == "js":
            links = js_login
        elif ext == "slash":
            links = slash_login
        elif ext == "cfm":
            links = cfm_login
        elif ext == "cgi":
            links = cgi_login
        elif ext == "brf":
            links = brf_login
        elif ext == "html":
            links = html_login
        else:
            raise ValueError("This ext(Argument) Not Allowed !")
        if workers == 1:
            t = Thread(target=self.send_req_admin_finder, args=(domain, timeout, links, user_agent, cookie, proxy, proxies))
            t.start()
            t.join()
            return founded
        elif workers == 2:
            calcu_div = int(len(links) / workers)
            links1 = links[:calcu_div]
            links2 = links[calcu_div:]
            t = Thread(target=self.send_req_admin_finder, args=(domain, timeout, links1, user_agent, cookie, proxy, proxies))
            t.start()
            t2 = Thread(target=self.send_req_admin_finder, args=(domain, timeout, links2, user_agent, cookie, proxy, proxies))
            t2.start()
            t2.join()
            return founded
        elif workers == 3:
            calcu_div = int(len(links) / workers)
            links1 = links[:calcu_div]
            links2 = links[calcu_div:calcu_div*2]
            links3 = links[calcu_div*2:]
            t = Thread(target=self.send_req_admin_finder, args=(domain, timeout, links1, user_agent, cookie, proxy, proxies))
            t.start()
            t2 = Thread(target=self.send_req_admin_finder, args=(domain, timeout, links2, user_agent, cookie, proxy, proxies))
            t2.start()
            t3 = Thread(target=self.send_req_admin_finder, args=(domain, timeout, links3, user_agent, cookie, proxy, proxies))
            t3.start()
            t3.join()
            return founded