import requests
import json
import sys
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init()
    c1 = Fore.CYAN
    c2 = Fore.GREEN
    c3 = Fore.YELLOW
    c4 = Fore.MAGENTA
    c5 = Fore.RED
    c6 = Fore.WHITE
    cr = Fore.RESET
    bold = Style.BRIGHT
except ImportError:
    c1 = c2 = c3 = c4 = c5 = c6 = cr = bold = ""

def githubuserinfo(username):
    endpoints = {
        "profile": f"https://api.github.com/users/{username}",
        "hovercard": f"https://api.github.com/users/{username}/hovercard",
        "followers": f"https://api.github.com/users/{username}/followers",
        "following": f"https://api.github.com/users/{username}/following",
        "repos": f"https://api.github.com/users/{username}/repos",
        "repos_owner": f"https://api.github.com/users/{username}/repos?type=owner",
        "repos_member": f"https://api.github.com/users/{username}/repos?type=member",
        "repos_created": f"https://api.github.com/users/{username}/repos?sort=created",
        "repos_updated": f"https://api.github.com/users/{username}/repos?sort=updated",
        "starred": f"https://api.github.com/users/{username}/starred",
        "subscriptions": f"https://api.github.com/users/{username}/subscriptions",
        "gists": f"https://api.github.com/users/{username}/gists",
        "orgs": f"https://api.github.com/users/{username}/orgs",
        "events": f"https://api.github.com/users/{username}/events",
        "events_public": f"https://api.github.com/users/{username}/events/public",
        "received_events": f"https://api.github.com/users/{username}/received_events",
        "received_events_public": f"https://api.github.com/users/{username}/received_events/public",
        "keys": f"https://api.github.com/users/{username}/keys",
        "gpg_keys": f"https://api.github.com/users/{username}/gpg_keys",
        "follows_check": f"https://api.github.com/users/{username}/following/dummy"
    }
    
    print(f"\n{c1}{bold}╔══════════════════════════════════════════════════════════════════╗{cr}")
    print(f"{c1}{bold}║{cr} {c2}{bold}GITHUB USER INFO{cr}                                                       {c1}{bold}║{cr}")
    print(f"{c1}{bold}╠══════════════════════════════════════════════════════════════════╣{cr}")
    print(f"{c1}{bold}║{cr} {c3}target:{cr} {c6}{bold}{username}{cr}                                                       {c1}{bold}║{cr}")
    print(f"{c1}{bold}╚══════════════════════════════════════════════════════════════════╝{cr}\n")
    
    for name, url in endpoints.items():
        try:
            r = requests.get(url)
            
            if r.status_code == 200:
                data = r.json()
                if isinstance(data, list):
                    print(f"{c4}{bold}┌─ {name.upper().replace('_', ' ')}{cr}")
                    print(f"{c5}│{cr} {c2}count: {c6}{len(data)}{cr}")
                    if data and len(data) > 0:
                        for i, item in enumerate(data[:5]):
                            if isinstance(item, dict):
                                itemname = item.get('login') or item.get('name') or item.get('id') or list(item.keys())[0]
                                print(f"{c5}│{cr}   {c3}{i+1}.{cr} {c6}{itemname}{cr}")
                    else:
                        print(f"{c5}│{cr} {c3}empty{cr}")
                    print(f"{c4}{bold}└─────────────────────────────────────────────────────────────{cr}\n")
                elif isinstance(data, dict):
                    print(f"{c4}{bold}┌─ {name.upper().replace('_', ' ')}{cr}")
                    if name == "profile":
                        print(f"{c5}│{cr} {c2}name:{cr} {c6}{data.get('name', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}bio:{cr} {c6}{data.get('bio', 'n/a')[:60]}{cr}")
                        print(f"{c5}│{cr} {c2}company:{cr} {c6}{data.get('company', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}location:{cr} {c6}{data.get('location', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}email:{cr} {c6}{data.get('email', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}twitter:{cr} {c6}{data.get('twitter_username', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}blog:{cr} {c6}{data.get('blog', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}followers:{cr} {c6}{data.get('followers', 0)}{cr} {c2}following:{cr} {c6}{data.get('following', 0)}{cr}")
                        print(f"{c5}│{cr} {c2}public repos:{cr} {c6}{data.get('public_repos', 0)}{cr} {c2}gists:{cr} {c6}{data.get('public_gists', 0)}{cr}")
                        print(f"{c5}│{cr} {c2}created:{cr} {c6}{data.get('created_at', 'n/a')[:10]}{cr}")
                        print(f"{c5}│{cr} {c2}id:{cr} {c6}{data.get('id', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}type:{cr} {c6}{data.get('type', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}hireable:{cr} {c6}{data.get('hireable', 'n/a')}{cr}")
                        print(f"{c5}│{cr} {c2}profile:{cr} {c3}{data.get('html_url', 'n/a')}{cr}")
                    elif name == "hovercard":
                        contexts = data.get('contexts', [])
                        for ctx in contexts[:5]:
                            print(f"{c5}│{cr} {c6}{ctx.get('message', 'n/a')}{cr}")
                    else:
                        flatdata = {}
                        for k, v in list(data.items())[:10]:
                            if not isinstance(v, (dict, list)):
                                flatdata[k] = v
                        for k, v in flatdata.items():
                            print(f"{c5}│{cr} {c2}{k}:{cr} {c6}{v}{cr}")
                    print(f"{c4}{bold}└─────────────────────────────────────────────────────────────{cr}\n")
                    
        except:
            pass

def main():
    print(f"{c2}{bold}")
    print(""" 
    ╔═══════════════════════════════════════════╗
    ║         AXOMIC GITHUB TOOL               ║
    ╔═══════════════════════════════════════════╝
    """)
    print(f"{cr}")
    
    while True:
        print(f"{c1}{bold}┌─────────────────────────────────────────┐{cr}")
        print(f"{c1}{bold}│{cr}  {c2}[1]{cr} github user info                   {c1}{bold}│{cr}")
        print(f"{c1}{bold}│{cr}  {c5}[2]{cr} exit                                 {c1}{bold}│{cr}")
        print(f"{c1}{bold}└─────────────────────────────────────────┘{cr}")
        
        choice = input(f"\n{c3}{bold}→{cr} {c6}select: {cr}")
        
        if choice == "1":
            name = input(f"{c3}{bold}→{cr} {c6}username: {cr}").strip()
            if name:
                githubuserinfo(name)
            else:
                print(f"{c5}{bold}username required{cr}")
        elif choice == "2":
            print(f"{c2}{bold}goodbye{cr}")
            sys.exit(0)
        else:
            print(f"{c5}{bold}[-] invalid{cr}")

if __name__ == "__main__":
    main()
