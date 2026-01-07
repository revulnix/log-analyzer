# Log Analyzer

Simple Python tool to parse authentication logs and report failed and successful login attempts by IP and by user.

Installation

1. Clone the repository
   git clone https://github.com/revulnix/log-analyzer.git
   cd log-analyzer

2. Create a virtual environment and install
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

Usage

Analyze a log file (defaults to /var/log/auth.log)
   python -m log_analyzer [path/to/auth.log] --top 10

Run tests

   pip install -r requirements.txt
   pytest


