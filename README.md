# ReconSweep 🔍

**OSINT Username Recon Tool** — ek username daalo, 20+ platforms pe check karo ki wo kahan-kahan exist karta hai.

Made with 🐍 by [**D4emon404**](https://github.com/D4emon404)

---

## ✨ Features

- 🔎 20+ platforms check karta hai — GitHub, Instagram, Reddit, Twitter/X, TryHackMe, HackTheBox, Telegram, YouTube, aur more
- ⚡ Multi-threaded — fast parallel scanning
- 🎨 Colored CLI output (Found / Not Found / Unclear)
- 💾 Results ko `.txt` file mein export kar sakte ho
- 🛡️ 100% legal & ethical — sirf public HTTP requests, koi login/bypass/exploit nahi

## 📦 Installation

```bash
git clone https://github.com/D4emon404/reconsweep.git
cd reconsweep
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python3 osint_recon.py <username>

# Results ko file mein save karo
python3 osint_recon.py <username> -o results.txt

# Color output disable karo
python3 osint_recon.py <username> --no-color

# Version check
python3 osint_recon.py -v
```

### Example

```bash
$ python3 osint_recon.py D4emon404
```

Output kuch aisa dikhega:

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

New platform add karna ho toh `PLATFORMS` dictionary mein bas ek line add karo — `osint_recon.py` ke top mein.

## ⚠️ Disclaimer

Ye tool sirf **educational aur ethical OSINT purposes** ke liye hai — apni khud ki digital footprint check karna, authorized penetration testing, bug bounty recon, ya CTF challenges. Kisi ki bhi privacy violate karne ya unauthorized surveillance ke liye use mat karo. Har platform ke Terms of Service ka respect karo.

## 🛠️ Tech Stack

- Python 3
- `requests` — HTTP calls ke liye
- `concurrent.futures` — multi-threading ke liye

## 📄 License

MIT License — free to use, modify, aur distribute karo.

---

⭐ Agar ye tool kaam aaya toh repo ko star karna mat bhoolna!
