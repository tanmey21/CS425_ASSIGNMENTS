import dns.message # type: ignore
import dns.query    # type: ignore
import dns.rdatatype # type: ignore
import dns.resolver # type: ignore
import time

# Root DNS servers used to start the iterative resolution process
ROOT_SERVERS = {
    "198.41.0.4": "Root (a.root-servers.net)",
    "199.9.14.201": "Root (b.root-servers.net)",
    "192.33.4.12": "Root (c.root-servers.net)",
    "199.7.91.13": "Root (d.root-servers.net)",
    "192.203.230.10": "Root (e.root-servers.net)"
}

TIMEOUT = 7  # Timeout in seconds for each DNS query attempt

def send_dns_query(server, domain):
    """ 
    Sends a DNS query to the given server for an A record of the specified domain.
    Returns the response if successful, otherwise returns None.
    """
    try:
        query = dns.message.make_query(domain, dns.rdatatype.A)  # Construct the DNS query
        response=dns.query.udp(query,server) #Getting and returning the response
        return response
    except dns.exception.Timeout:
        print(f"[ERROR] Timeout while querying {server}")
    except dns.query.BadResponse:
        print(f"[ERROR] Bad response from {server}")
    except dns.query.TransferError:
        print(f"[ERROR] Transfer error while querying {server}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

        return None  # If an error occurs (timeout, unreachable server, etc.), return None

def extract_next_nameservers(response):
    """ 
    Extracts nameserver (NS) records from the authority section of the response.
    Then, resolves those NS names to IP addresses.
    Returns a list of IPs of the next authoritative nameservers.
    """
    ns_ips = []  # List to store resolved nameserver IPs
    ns_names = []  # List to store nameserver domain names
    
    try:
        if not response.authority:
            print("[ERROR] No authority section found in response.")
            return []  # No NS records found, return empty list

        for rrset in response.authority:
            if rrset.rdtype == dns.rdatatype.NS:
                for rr in rrset:
                    ns_name = rr.to_text()
                    ns_names.append(ns_name)  # Extract nameserver hostname
                    print(f"Extracted NS hostname: {ns_name}")

        for ns_name in ns_names:
            try:
                #Geting the value of IP Address of NS hosts
                tmp_id = dns.resolver.resolve(ns_name, 'A', lifetime=TIMEOUT)
                tmp_name = tmp_id[0].to_text()
                print(f"Resolved {ns_name} to {tmp_name}")
                ns_ips.append(tmp_name)
            except dns.resolver.NXDOMAIN:
                print(f"[ERROR] NS lookup failed: {ns_name} does not exist.")
            except dns.resolver.NoAnswer:
                print(f"[ERROR] NS lookup failed: No A record found for {ns_name}")
            except dns.resolver.Timeout:
                print(f"[ERROR] Timeout while resolving {ns_name}")
            except Exception as e:
                print(f"[ERROR] Unexpected error resolving {ns_name}: {e}")

    except Exception as e:
        print(f"[ERROR] Unexpected error extracting NS records: {e}")

    return ns_ips  # Return list of resolved nameserver IPs

def iterative_dns_lookup(domain):
    """ 
    Performs an iterative DNS resolution starting from root servers.
    It queries root servers, then TLD servers, then authoritative servers,
    following the hierarchy until an answer is found or resolution fails.
    """
    print(f"[Iterative DNS Lookup] Resolving {domain}")

    next_ns_list = list(ROOT_SERVERS.keys())  # Start with the root server IPs
    stage = "ROOT"  # Track resolution stage (ROOT, TLD, AUTH)

    while next_ns_list:
        ns_ip = next_ns_list[0]  # Pick the first available nameserver to query
        response = send_dns_query(ns_ip, domain)
        
        if response: #checks if response is not NONE
            print(f"[DEBUG] Querying {stage} server ({ns_ip}) - SUCCESS")
            
            # If an answer is found, print and return
            if response.answer:
                print(f"[SUCCESS] {domain} -> {response.answer[0][0]}")
                return
            
            # If no answer, extract the next set of nameservers
            next_ns_list = extract_next_nameservers(response)

            if stage=="ROOT":
                stage="TLD"
            else:
                stage="AUTH"
            # TODO: Move to the next resolution stage, i.e., it is either TLD, ROOT, or AUTH
        else:
            print(f"[ERROR] Query failed for {stage} {ns_ip}")
            return  # Stop resolution if a query fails
    
    print("[ERROR] Resolution failed.")  # Final failure message if no nameservers respond

def recursive_dns_lookup(domain):
    print(f"[Recursive DNS Lookup] Resolving {domain}")
    try:
        #Querying the names of different NS hosts
        answer = dns.resolver.resolve(domain, "NS")
        for rdata in answer:
            print(f"[SUCCESS] {domain} -> {rdata}")

        answer = dns.resolver.resolve(domain, "A")
        for rdata in answer:
            print(f"[SUCCESS] {domain} -> {rdata}")
    except Exception as e:
        print(f"[ERROR] Recursive lookup failed: {e}")  # Handle resolution failure

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3 or sys.argv[1] not in {"iterative", "recursive"}:
        print("Usage: python3 dns_server.py <iterative|recursive> <domain>")
        sys.exit(1)

    mode = sys.argv[1]  # Get mode (iterative or recursive)
    domain = sys.argv[2]  # Get domain to resolve
    start_time = time.time()  # Record start time
    
    # Execute the selected DNS resolution mode
    if mode == "iterative":
        iterative_dns_lookup(domain)
    else:
        recursive_dns_lookup(domain)
    
    print(f"Time taken: {time.time() - start_time:.3f} seconds")  # Print execution time

