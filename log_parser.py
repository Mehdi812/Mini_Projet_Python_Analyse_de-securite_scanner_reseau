# log_parser.py
import re

def parse_logs(filename):
    ip_counts = {}
    user_agent_data = {}
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[.+\] "GET .+" (\d+) "([^"]+)"')
    # On suppose que le User-Agent est la dernière partie entre guillemets

    with open(filename, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                status = int(match.group(2))
                user_agent = match.group(3)
                # On peut filtrer certains statuts si besoin
                if status >= 400:
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1
                    if ip in user_agent_data:
                        user_agent_data[ip].add(user_agent)
                    else:
                        user_agent_data[ip] = {user_agent}
    return ip_counts, user_agent_data