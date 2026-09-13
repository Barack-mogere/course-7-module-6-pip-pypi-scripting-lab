import requests
from datetime import datetime


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log():
    post = fetch_data()

    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched post: {post.get('title', 'No title found')}"
    ]

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    generate_log()