import urllib.request
try:
    urllib.request.urlopen("https://images.unsplash.com/photo-1626245389650-8b1b8606c117?q=80&w=1200")
    print("URL works")
except Exception as e:
    print(f"URL failed: {e}")
