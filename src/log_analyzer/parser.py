import re
from pathlib import Path
from collections import Counter

IP_RE = re.compile(r'(\d{1,3}(?:\.\d{1,3}){3})')
FAILED_KEYWORDS = [
    'Failed password',
    'authentication failure',
    'Failed publickey',
    'Invalid user',
]

def extract_user(line):
    m = re.search(r'for(?: invalid user)?\s+([A-Za-z0-9._-]+)', line)
    if m:
        return m.group(1)
    m2 = re.search(r'Accepted .* for\s+([A-Za-z0-9._-]+)', line)
    if m2:
        return m2.group(1)
    return None

def parse_log(path):
    path = Path(path)
    failed = Counter()
    successful = Counter()
    users = Counter()
    total = 0
    text = path.read_text(errors='ignore')
    for line in text.splitlines():
        total += 1
        ip_match = IP_RE.search(line)
        ip = ip_match.group(1) if ip_match else None
        is_failed = False
        for kw in FAILED_KEYWORDS:
            if kw in line:
                is_failed = True
                if ip:
                    failed[ip] += 1
                user = extract_user(line)
                if user:
                    users[user] += 1
                break
        if not is_failed:
            if 'Accepted password' in line or 'Accepted publickey' in line:
                if ip:
                    successful[ip] += 1
                user = extract_user(line)
                if user:
                    users[user] += 1
    return {
        'total_lines': total,
        'failed_by_ip': dict(failed),
        'successful_by_ip': dict(successful),
        'user_counts': dict(users),
    }
