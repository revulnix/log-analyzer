import argparse
from pathlib import Path
from .parser import parse_log

def main():
    parser = argparse.ArgumentParser(description='Log Analyzer')
    parser.add_argument('file', nargs='?', default='/var/log/auth.log', help='path to auth log')
    parser.add_argument('--top', type=int, default=10, help='top N results')
    args = parser.parse_args()
    path = Path(args.file)
    if not path.exists():
        print('File not found:', path)
        return
    report = parse_log(path)
    print('Total lines analyzed:', report['total_lines'])
    print()
    print('Top failed IPs:')
    for ip, count in sorted(report['failed_by_ip'].items(), key=lambda x: -x[1])[:args.top]:
        print(ip, '\t', count)
    print()
    print('Top successful IPs:')
    for ip, count in sorted(report['successful_by_ip'].items(), key=lambda x: -x[1])[:args.top]:
        print(ip, '\t', count)
    print()
    print('Top users:')
    for u, c in sorted(report['user_counts'].items(), key=lambda x: -x[1])[:args.top]:
        print(u, '\t', c)

if __name__ == '__main__':
    main()
