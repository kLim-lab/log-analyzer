# Apache log-analyzer
A lightweight Python command-line program that examines Apache logs to return error patterns and operational insights. Quick utility for poking at large log files.

## Overview
This tool reads large Apache-style logs line by line without loading them into memory. Its features include:
- HTTP status code frequency analysis
- Detection of the hour with the most 5xx errors 
- Most frequently failing endpoints identification

## Usage
- Tested with Python 3.12

### 1. Clone the repository
git clone https://github.com/kLim-lab/log-analyzer.git
cd log-analyzer

### 2. Run the analysis
python main.py --file logs/apache.log

## Example output

=== APACHE LOG ANALYSIS REPORT ===

Status Code Frequency:
200: 9126
206: 45
301: 164
304: 445
403: 2
404: 213
416: 2
500: 3

Peak 5xx Error Hour: 18:00
Most Failing Endpoint: /misc/Title.php.txt

Recommendation:
Investigate server-side errors and affected endpoints.

## Design Tradeoffs
- Assumes standard Apache access log format
- Uses simple string parsing instead of regex for readability
- Processes logs as a stream to keep memory usage low

## Log format
192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395

NOTE: if the format differs significantly, index-based parsing may need adjusting

## What I learned
- Streaming file processing in Python is powerful
- Separating parsing from analysis keeps the code easier to extend
- Simple metrics can help guide operational decisions
