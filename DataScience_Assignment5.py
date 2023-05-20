import requests
import html2text

def download_data(api_url):
    # Send a GET request to the API URL
    response = requests.get(api_url)

    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Extract the show details
        show_name = data["name"]
        show_language = data["language"]
        show_status = data["status"]

        print("Show Name:", show_name)
        print("Language:", show_language)
        print("Status:", show_status)

        # Extract and format episode details
        episodes = data["_embedded"]["episodes"]
        print("\nEpisode List:")
        for episode in episodes:
            episode_id = episode["id"]
            episode_url = episode["url"]
            episode_name = episode["name"]
            episode_season = episode["season"]
            episode_number = episode["number"]
            episode_type = episode["type"]
            episode_airdate = episode["airdate"]
            episode_airtime = episode["airtime"]
            episode_runtime = episode["runtime"]
            episode_rating = episode["rating"]["average"]
            episode_summary = episode["summary"]
            episode_image_medium = episode["image"]["medium"]
            episode_image_original = episode["image"]["original"]

            # Remove HTML tags from the episode summary
            episode_summary = html2text.html2text(episode_summary).strip()

            print(f"Episode ID: {episode_id}")
            print(f"Episode URL: {episode_url}")
            print(f"Name: {episode_name}")
            print(f"Season: {episode_season}")
            print(f"Number: {episode_number}")
            print(f"Type: {episode_type}")
            print(f"Airdate: {episode_airdate}")
            print(f"Airtime: {episode_airtime}")
            print(f"Runtime: {episode_runtime} minutes")
            print(f"Average Rating: {episode_rating}")
            print(f"Summary: {episode_summary}")
            print(f"Medium Image Link: {episode_image_medium}")
            print(f"Original Image Link: {episode_image_original}")
            print("-----------------------------------------")

    else:
        print("Failed to download data. Status code:", response.status_code)

# API URL for Westworld show
api_url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Download and extract data
download_data(api_url)
