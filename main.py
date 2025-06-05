# main.py
import argparse
import socket
from log_parser import parse_logs
from data_analyzer import analyze_data
from network_scanner import scan_ports

def main():
    parser = argparse.ArgumentParser(description='Analyse logs & scan réseau')
    parser.add_argument('--logfile', type=str, default='test_log.log', help='Fichier log source')
    parser.add_argument('--scan', action='store_true', help='Lancer le scan de ports')
    parser.add_argument('--verbose', action='store_true', help='Afficher ports fermés')
    parser.add_argument('--detect', type=int, default=10, help='Seuil pour IP suspecte')
    args = parser.parse_args()

    # Partie 1 : Analyse logs
    ip_counts, user_agents = parse_logs(args.logfile)

    # Détection des IP suspectes (avec seuil)
    suspect_ips = [ip for ip, count in ip_counts.items() if count >= args.detect]
    print(f"IPs suspectes détectées (>= {args.detect} accès) : {suspect_ips}")

    # Partie 2 : scan de ports sur les IP suspectes
    ports_to_scan = [22, 80, 443, 8080, 21]
    ports_scan_results = {}
    if args.scan:
        for ip in suspect_ips:
            print(f"\nScan des ports pour {ip}...")
            open_ports, closed_ports = scan_ports(ip, ports_to_scan, verbose=args.verbose)
            ports_scan_results[ip] = {'open': open_ports, 'closed': closed_ports}
            print(f"Ports ouverts pour {ip} : {open_ports}")
            if args.verbose:
                print(f"Ports fermés pour {ip} : {closed_ports}")

    # Partie 3 : analyse et rapport
    top_ips, suspects, ports_info = analyze_data(ip_counts, user_agents, ports_scan_results, top_n=5)

if __name__ == "__main__":
    main()