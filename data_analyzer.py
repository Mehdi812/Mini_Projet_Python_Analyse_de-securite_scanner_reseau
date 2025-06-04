import matplotlib.pyplot as plt

def afficher_top_ips(ips, echecs, succes, top_n=5):
    top_indexes = sorted(range(len(echecs)), key=lambda i: echecs[i], reverse=True)[:top_n]

    top_ips = [ips[i] for i in top_indexes]
    top_echecs = [echecs[i] for i in top_indexes]
    top_succes = [succes[i] for i in top_indexes]

    x = list(range(len(top_ips)))
    bar_width = 0.4

    plt.figure(figsize=(10, 6))
    plt.bar([i - bar_width/2 for i in x], top_echecs, width=bar_width, color='red', label='Échecs')
    plt.bar([i + bar_width/2 for i in x], top_succes, width=bar_width, color='green', label='Réussites')

    plt.xticks(x, top_ips, rotation=45)
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre de tentatives")
    plt.title("Top IPs – Connexions SSH (Échecs vs Réussites)")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()