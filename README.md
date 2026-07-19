# ReconSweep 🔍

**OSINT Username Recon Tool** — enter a username, check 20+ platforms to see where it exists.

Made with 🐍 by [**D4emon404**](https://github.com/D4emon404)

---

## ✨ Features

- 🔎 Checks 20+ platforms — GitHub, Instagram, Reddit, Twitter/X, TryHackMe, HackTheBox, Telegram, YouTube, and more
- ⚡ Multi-threaded — fast parallel scanning
- 🎨 Colored CLI output (Found / Not Found / Unclear)
- 💾 Export results to a `.txt` file
- 🛡️ 100% legal & ethical — only public HTTP requests, no login/bypass/exploit involved

## 📦 Installation

```bash
git clone https://github.com/D4emon404/reconsweep.git
cd reconsweep
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python3 osint_recon.py <username>

# Save results to a file
python3 osint_recon.py <username> -o results.txt

# Disable colored output
python3 osint_recon.py <username> --no-color

# Check version
python3 osint_recon.py -v
```

### Example

```bash
$ python3 osint_recon.py D4emon404
```

Output will look something like this:

```
[+] FOUND (3)
    ✔ GitHub          https://github.com/D4emon404
    ✔ TryHackMe       https://tryhackme.com/p/D4emon404
    ✔ HackTheBox       https://app.hackthebox.com/profile/search/D4emon404

[-] NOT FOUND (12)
    ✘ Facebook
    ...

[?] UNCLEAR / BLOCKED (5) — manually verify
    ? Instagram        https://www.instagram.com/D4emon404/
```

## 🧩 Platforms Covered

GitHub, GitLab, Twitter/X, Instagram, Facebook, Reddit, TryHackMe, HackTheBox, HackerOne, YouTube, TikTok, Telegram, Steam, Twitch, Medium, Dev.to, Pinterest, Keybase, Replit, SoundCloud.

Want to add a new platform? Just add a line to the `PLATFORMS` dictionary at the top of `osint_recon.py`.

## ⚠️ Disclaimer

This tool is built for **educational and ethical OSINT purposes only** — checking your own digital footprint, authorized penetration testing, bug bounty recon, or CTF challenges. Do not use it to violate anyone's privacy or for unauthorized surveillance. Respect the Terms of Service of every platform.

## 🛠️ Tech Stack

- Python 3
- `requests` — for HTTP calls
- `concurrent.futures` — for multi-threading

## 📄 License

MIT License — free to use, modify, and distribute.

---

⭐ If this tool was useful, don't forget to star the repo!
