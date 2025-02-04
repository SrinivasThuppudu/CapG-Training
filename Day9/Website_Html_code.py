import requests
import threading

def fetch_website_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.python.org"  # Replace with the URL of the website you want to fetch
    html_content = fetch_website_html(url)
    if html_content:
        with open("website_content1.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        def fetch_url(url, results):
            try:
                response = requests.get(url)
                response.raise_for_status()
                html_content = response.text
                results.append((url, html_content))
            except requests.exceptions.RequestException as e:
                results.append((url, f"Error: {e}"))

        urls = [
            "https://example.com",
            "https://www.python.org",
            "https://www.github.com"
        ]

        threads = []
        results = []

        for url in urls:
            thread = threading.Thread(target=fetch_url, args=(url, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Save results to files after all threads are done
        for url, content in results:
            if "Error" not in content:
                filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Website content saved to {filename}")
                
            else:
                print(f"Failed to fetch {url}: {content}")

print("abc @ 123")