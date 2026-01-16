def analyze_log(log_lines):
    status_counts = {}
    errors_by_hour = {}
    endpoints_5xx = {}

    for log_line in log_lines:
        parts = log_line.split() 

        status_code = parts[8]
        endpoint = parts[6]
        hour = parts[3][1:3]

        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        if status_code.startswith("5"):
            errors_by_hour[hour] = errors_by_hour.get(hour, 0) + 1
            endpoints_5xx[endpoint] = endpoints_5xx.get(endpoint, 0) + 1

    return  status_counts, errors_by_hour, endpoints_5xx