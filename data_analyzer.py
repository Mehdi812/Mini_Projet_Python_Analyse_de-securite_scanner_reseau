# data_analyzer.py
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(ip_counts, user_agent_data, ports_scan_results, top_n=5):
    # Conversion en DataFrame
    df = pd.DataFrame(ip_counts.items(), columns=['IP', 'Occurrences'])
    df = df.sort_values(by='Occurrences', ascending=False)
    
    # Top IPs
    top_ips = df.head(top_n)
    print("Top IPs:")
    print(top_ips)
    
    # Détection de bots/scanners via User-Agent
    suspicious_ips = []
    for ip, user_agents in user_agent_data.items():
        for ua in user_agents:
            if any(bot_keyword in ua for bot_keyword in ['bot', 'spider', 'crawl', 'scanner']):
                suspicious_ips.append(ip)
                break
    
    # Détails ports par IP
    ports_info = {}
    for ip in ip_counts.keys():
        ports_info[ip] = {
            'open_ports': ports_scan_results.get(ip, {}).get('open', []),
            'closed_ports': ports_scan_results.get(ip, {}).get('closed', [])
        }
    
    # Générer la visualisation graphique
    plt.figure(figsize=(10,6))
    plt.bar(top_ips['IP'], top_ips['Occurrences'])
    plt.xlabel('IP Address')
    plt.ylabel('nombre de tentatives')
    plt.title('Top IPs')
    plt.tight_layout()
    plt.savefig('top_ips_bargraph.png')  # Sauvegarde du graphique
    plt.show()

    # Génération du rapport HTML
    html_content = "<html><head><title>Rapport d'analyse</title></head><body>"
    html_content += "<h2>Classement des IPs par Occurrences</h2>"
    html_content += top_ips.to_html(index=False)
    html_content += "<h2>Top 5 IPs</h2>"
    html_content += top_ips.to_html(index=False)

    html_content += "<h2>IPs Suspects (potentiellement bots)</h2><ul>"
    for ip in set(suspicious_ips):
        html_content += f"<li>{ip}</li>"
    html_content += "</ul>"

    # Détails port
    html_content += "<h2>Détails Ports</h2>"
    for ip, ports in ports_info.items():
        html_content += f"<h3>IP: {ip}</h3>"
        open_ports = ports['open_ports']
        closed_ports = ports['closed_ports']
        html_content += "<b>Ports ouverts:</b> " + (', '.join(map(str, open_ports)) if open_ports else 'Aucun') + "<br>"
        html_content += "<b>Ports fermés:</b> " + (', '.join(map(str, closed_ports)) if closed_ports else 'Aucun') + "<br>"

    # Ajout de l'image du graphique dans le HTML
    html_content += '<h2>Graphique : Top IPs</h2>'
    html_content += '<img src="top_ips_bargraph.png" alt="Graphique Top IPs">'

    # Enregistrement HTML
    with open('full_ip_analysis_report.html', 'w') as f:
        f.write(html_content)
    print("Rapports CSV et HTML générés : 'full_ip_report.csv' et 'full_ip_report.html'.")

    # Export CSV global
    df.to_csv('full_ip_report.csv', index=False)

    return top_ips, suspicious_ips, ports_info