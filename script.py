import requests as req

print("gravando dns...")
dns_base = 'https://neetcine.lat/'

with req.Session() as session:
    session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    })
    response = session.get(dns_base, allow_redirects=True, verify=False)
    url = response.url
    if url:
        with open('dns.txt', 'w') as file:
            file.write(url)
        print("dns gravado com sucesso")
    else:
        print("falha ao gravar dns")
