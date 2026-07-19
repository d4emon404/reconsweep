#!/usr/bin/env python3
"""
ReconSweep - OSINT Username Recon Tool
========================================

Takes a username as input and checks whether it exists across multiple platforms.
Uses only public HTTP requests — no login, bypass, or exploitation involved.
Built for legal and ethical OSINT purposes (personal research, bug bounty scope, CTF recon).

Author  : D4emon404
GitHub  : https://github.com/D4emon404
License : MIT
Version : 1.0.0

Usage:
    python3 osint_recon.py <username>
    python3 osint_recon.py <username> -o results.txt
    python3 osint_recon.py <username> --no-color

Disclaimer:
    Built for educational and ethical OSINT purposes only.
    Use only for your own research, authorized engagements, or public info gathering.
    Respect the Terms of Service of every platform.
"""

import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

__author__ = "D4emon404"
__version__ = "1.0.0"

# ANSI colors for terminal output
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

BANNER = f"""{Colors.CYAN}{Colors.BOLD}
   ____                     _____                       
  |  _ \\ ___  ___ ___  _ __/ ____|_      _____  ___ _ __  
  | |_) / _ \\/ __/ _ \\| '_ \\___ \\\\ \\ /\\ / / _ \\/ _ \\ '_ \\ 
  |  _ <  __/ (_| (_) | | | |__) |\\ V  V /  __/  __/ |_) |
  |_| \\_\\___|\\___\\___/|_| |_|____/  \\_/\\_/ \\___|\\___| .__/ 
                                                     |_|    
  OSINT Username Recon Tool  |  by {__author__}  |  v{__version__}
{Colors.RESET}"""

# Platform: URL template
# Some sites return 404 for a missing user, others always return 200 (JS-rendered pages)
# — those cases fall into the "unclear" bucket for manual verification.
PLATFORMS = {
    "GitHub":        "https://github.com/{}",
    "Twitter/X":     "https://x.com/{}",
    "Instagram":     "https://www.instagram.com/{}/",
    "Reddit":        "https://www.reddit.com/user/{}/",
    "TryHackMe":     "https://tryhackme.com/p/{}",
    "HackTheBox":    "https://app.hackthebox.com/profile/search/{}",
    "YouTube":       "https://www.youtube.com/@{}",
    "TikTok":        "https://www.tiktok.com/@{}",
    "Telegram":      "https://t.me/{}",
    "Steam":         "https://steamcommunity.com/id/{}",
    "Twitch":        "https://www.twitch.tv/{}",
    "Medium":        "https://medium.com/@{}",
    "GitLab":        "https://gitlab.com/{}",
    "Pinterest":     "https://www.pinterest.com/{}/",
    "Dev.to":        "https://dev.to/{}",
    "Keybase":       "https://keybase.io/{}",
    "Replit":        "https://replit.com/@{}",
    "HackerOne":     "https://hackerone.com/{}",
    "SoundCloud":    "https://soundcloud.com/{}",
    "Facebook":      "https://www.facebook.com/{}",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}

TIMEOUT = 6


def check_platform(name, url_template, username):
    url = url_template.format(username)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        # Simple heuristic: 200/999(LinkedIn-style block) = likely exists, 404 = not found
        if resp.status_code == 404:
            return name, url, False
        elif resp.status_code in (200, 999):
            return name, url, True
        else:
            return name, url, None  # unclear / rate-limited / blocked
    except requests.RequestException:
        return name, url, None  # site down / timeout / blocked


def run_recon(username, max_workers=15):
    found, not_found, unclear = [], [], []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(check_platform, name, url, username): name
            for name, url in PLATFORMS.items()
        }
        for future in as_completed(futures):
            name, url, status = future.result()
            if status is True:
                found.append((name, url))
            elif status is False:
                not_found.append((name, url))
            else:
                unclear.append((name, url))

    return found, not_found, unclear


def print_results(username, found, not_found, unclear, use_color=True):
    c = Colors if use_color else type("NoColor", (), {k: "" for k in vars(Colors) if not k.startswith("_")})

    print(f"\n{c.BOLD}{'='*58}{c.RESET}")
    print(f"{c.BOLD}  Recon Report  —  username: {username}{c.RESET}")
    print(f"{c.BOLD}{'='*58}{c.RESET}\n")

    print(f"{c.GREEN}{c.BOLD}[+] FOUND ({len(found)}){c.RESET}")
    for name, url in sorted(found):
        print(f"    {c.GREEN}✔{c.RESET} {name:<15} {url}")

    print(f"\n{c.RED}{c.BOLD}[-] NOT FOUND ({len(not_found)}){c.RESET}")
    for name, url in sorted(not_found):
        print(f"    {c.RED}✘{c.RESET} {name:<15}")

    if unclear:
        print(f"\n{c.YELLOW}{c.BOLD}[?] UNCLEAR / BLOCKED ({len(unclear)}){c.RESET} — manually verify")
        for name, url in sorted(unclear):
            print(f"    {c.YELLOW}?{c.RESET} {name:<15} {url}")

    print(f"\n{c.BOLD}{'='*58}{c.RESET}\n")


def save_results(username, found, not_found, unclear, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"OSINT Recon Report — username: {username}\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"FOUND ({len(found)}):\n")
        for name, url in sorted(found):
            f.write(f"  {name}: {url}\n")
        f.write(f"\nNOT FOUND ({len(not_found)}):\n")
        for name, url in sorted(not_found):
            f.write(f"  {name}\n")
        if unclear:
            f.write(f"\nUNCLEAR ({len(unclear)}):\n")
            for name, url in sorted(unclear):
                f.write(f"  {name}: {url}\n")
    print(f"[i] Results saved to: {filepath}")


def main():
    parser = argparse.ArgumentParser(
        prog="reconsweep",
        description="ReconSweep - OSINT Username Recon Tool",
        epilog=f"Made by {__author__}  |  github.com/{__author__}",
    )
    parser.add_argument("username", help="Username to search across platforms")
    parser.add_argument("-o", "--output", help="Save results to a text file")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")
    parser.add_argument("-v", "--version", action="version", version=f"ReconSweep {__version__} by {__author__}")
    args = parser.parse_args()

    use_color = not args.no_color
    print(BANNER if use_color else f"ReconSweep v{__version__} by {__author__}")
    print(f"[i] Scanning {len(PLATFORMS)} platforms for '{args.username}'... this may take a few seconds")

    found, not_found, unclear = run_recon(args.username)
    print_results(args.username, found, not_found, unclear, use_color=use_color)

    if args.output:
        save_results(args.username, found, not_found, unclear, args.output)


if __name__ == "__main__":
    main()
