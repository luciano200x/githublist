import requests

def get_github_ips():
    # Fetch data from GitHub meta API
    response = requests.get('https://api.github.com/meta')
    data = response.json()
    
    # Create a set to store unique IPs (avoid duplicates)
    all_ips = set()
    
    # Iterate through all IP-containing fields
    ip_fields = [
        'hooks', 'web', 'api', 'git', 'packages', 'actions'
    ]
    
    # Collect all IPs
    for field in ip_fields:
        if field in data:
            all_ips.update(data[field])
    
    # Sort IPs for consistent output
    return sorted(list(all_ips))

def write_ip_list(filename="github_ips.txt"):
    try:
        ips = get_github_ips()
        
        with open(filename, 'w') as f:
            # Write header similar to Spamhaus format
            f.write("; GitHub IP List - Generated from api.github.com/meta\n")
            f.write("; https://api.github.com/meta\n\n")
            
            # Write IPs
            for ip in ips:
                f.write(f"{ip}\n")
                
        print(f"Successfully wrote {len(ips)} IP addresses to {filename}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    write_ip_list()