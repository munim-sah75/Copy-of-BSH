import requests

# URL to fetch data from
SOURCE_URL = "https://raw.githubusercontent.com/Hasanmahmud000/Hasan/refs/heads/main/index.html"
# File to save the content
OUTPUT_FILE = "CBSH2.m3u"

def copy_entire_content():
    response = requests.get(SOURCE_URL)
    if response.status_code != 200:
        print("Failed to fetch data.")
        return

    # Write the entire content to the output file
    with open(OUTPUT_FILE, "w") as file:
        file.write(response.text)

    print(f"Entire content copied successfully to {OUTPUT_FILE}.")

if __name__ == "__main__":
    copy_entire_content()
