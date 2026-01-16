def parse_log(logfile_path):
    """
        Streams an Apache-style access log one line at a time
        Designed to handle large files without loading into memory 
    """
    try: 
        with open(logfile_path,"r") as file:
            for raw_line in file:
                cleaned = raw_line.strip()
                if cleaned == "":
                    continue
                yield cleaned
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file not found: {logfile_path}")
    except IOError as err:
        raise IOError(f"Error reading log file: {err}")