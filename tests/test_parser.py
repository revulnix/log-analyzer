from log_analyzer import parser
from pathlib import Path

def test_parse_sample():
    p = Path('sample_logs/auth.log')
    r = parser.parse_log(p)
    assert r['total_lines'] == 6
    assert r['failed_by_ip'].get('203.0.113.5') == 3
    assert r['successful_by_ip'].get('198.51.100.2') == 1
    assert r['user_counts'].get('root') == 2
