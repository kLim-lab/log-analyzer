import argparse
from parser import parse_log
from analysis import analyze_log

def main():
    parser = argparse.ArgumentParser(description="Apache Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to Apache access log")
    args = parser.parse_args()

    log_lines = parse_log(args.file)
    status_counts,  errors_by_hour, endpoints_5xx = analyze_log(log_lines)

    print("\n=== APACHE LOG ANALYSIS REPORT ===")

    print("\nStatus Code Frequency:")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")

    if errors_by_hour:
        peak_hour = max(errors_by_hour, key=errors_by_hour.get)
        print(f"\nPeak 5xx Error Hour: {peak_hour}:00")
    
    if endpoints_5xx:
        top_endpoint = max(endpoints_5xx, key=endpoints_5xx.get)
        print(f"Most Failing Endpoint: {top_endpoint}")
    
    print("\nRecommendation:")
    if errors_by_hour:
        print("Investigate server-side errors and affected endpoints.")
    else:
        print("No critical server errors detected.")

if __name__ == "__main__":
    main()