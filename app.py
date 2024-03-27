from flask import Flask
from collections import Counter

app = Flask(__name__)

# Sample list of visited sites
visited_sites = [
    "example.com",
    "google.com",
    "stackoverflow.com",
    "example.com",
    "github.com",
    "stackoverflow.com",
    "google.com",
    "github.com",
    "example.com",
    "wikipedia.org",
    "stackoverflow.com",
    "google.com",
    "github.com",
    "wikipedia.org",
    "example.com"
]

@app.route('/')
def most_visited():
    # Count the occurrences of each site
    site_counter = Counter(visited_sites)

    # Get the 5 most common sites
    most_visited_sites = site_counter.most_common(5)

    # Create HTML content
    html_content = "<h1>Most Visited Sites:</h1>"
    html_content += "<ul>"
    for site, count in most_visited_sites:
        html_content += f"<li>{site}: {count} visits</li>"
    html_content += "</ul>"

    return html_content

if __name__ == '__main__':
    app.run(debug=True)
