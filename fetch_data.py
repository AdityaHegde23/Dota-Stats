import os
import json
import requests
from datetime import datetime
import time

# Configuration
API_ENDPOINT = "https://api.opendota.com/api/matches/{match_id}"
API_KEY = "YOUR_OPENDOTA_API_KEY"  # Replace with your OpenDota API key, if needed
LOCAL_SAVE_DIR = "/home/ad-magus-apex/Downloads/Q4/EDA/Dota-Stats/data/match_data/parsed_matches/parsed_match_data"  # Local directory to save JSON files
RATE_LIMIT = 60  # Number of requests per minute

# Fetched till match id: 8034875166, 8034779806, 8034611701, 8034479774, 8034441203, 8034051300, 8033743058, 8033624756
def fetch_and_save_match_data(match_id):
    """Fetches match data from OpenDota API and saves it locally as a JSON file."""
    try:
        # Fetch data from API
        response = requests.get(API_ENDPOINT.format(match_id=match_id)) 
        response.raise_for_status()
        match_data = response.json()
        
        # Prepare filename and path
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"match_{match_id}.json"
        #filename = "pubic_match_data.json"
        local_path = os.path.join(LOCAL_SAVE_DIR, filename)
        
        # Ensure local directory exists
        os.makedirs(LOCAL_SAVE_DIR, exist_ok=True)
        print("Writing data to disk")
        # Save data locally
        with open(local_path, 'w') as f:
            json.dump(match_data, f, indent=4)
        print(f"Match data saved locally: {local_path} {match_id}")
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch match data for match_id {match_id}: {e}")
        return


def fetch_and_save_match_ids(preferred_id, target_count=10000):
    url = "https://api.opendota.com/api/parsedMatches"
    match_ids = []
    calls_per_day = 2000
    rate_limit = 60  # 60 calls per minute
    request_interval = 60 / rate_limit  # Interval in seconds per request

    while len(match_ids) < target_count:
        params = {"less_than_match_id": preferred_id}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            if not data:
                print("No more matches available to fetch.")
                break

            # Extract match IDs and update preferred_id
            for match in data:
                match_id = match["match_id"]
                match_ids.append(match_id)

            # Update preferred_id to fetch the next batch of older matches
            preferred_id = match_ids[-1]  # Get the last match ID fetched for the next request
            print(preferred_id)
            print(f"Fetched {len(match_ids)} match IDs so far...")
            
            # # Check if we reached the call limit
            # if len(match_ids)/100 >= calls_per_day:
            #     print("Reached daily call limit. Waiting until tomorrow...")
            #     time.sleep(24 * 60 * 60)  # Wait for a day if the daily call limit is reached

            # Wait to avoid rate limiting
            time.sleep(request_interval)
        
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            time.sleep(request_interval)

    ids_dir_path = "/home/ad-magus-apex/Downloads/Q4/EDA/Dota-Stats/data/match_data/parsed_matches/parsed_match_ids.json"
    # Save match IDs to file
    with open(ids_dir_path, "w") as f:
        json.dump(match_ids, f)
    print(f"Saved {target_count} match IDs")


#fetch_and_save_match_ids(preferred_id=8033743058)

    
def extract_match_ids():
    """Extracts match IDs from a locally stored JSON file."""
    preferred_id = 8033743058
    match_ids_path = f"data/match_data/parsed_matches/parsed_match_ids.json"
    with open(match_ids_path, 'r') as f:
        data = json.load(f)
    
    # Extract match IDs
    match_ids = data#["matches"]#[match["match_id"] for match in data if "match_id" in match]
    index = match_ids.index(8033624756)
    match_ids = match_ids[index:] 
    print(match_ids[0])
    # Print match IDs
    #print("Extracted match IDs:", match_ids)
    
    return match_ids

def fetch_matches_in_sequence():
    """Fetch multiple match data sequentially with rate limiting."""

    match_ids = extract_match_ids()
    for match_id in match_ids:
        
        fetch_and_save_match_data(match_id)
        
        # Rate limit to avoid hitting API limits (2000 calls/day at 60 calls/min)
        time.sleep(60 / RATE_LIMIT)

# Example usage
start_match_id = 8008769471  # Replace with a valid starting match ID
num_matches = 110  # Number of matches to fetch

fetch_matches_in_sequence() # fetches match in given 