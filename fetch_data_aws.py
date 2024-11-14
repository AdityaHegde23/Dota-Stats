import os
import json
import requests
import boto3
from datetime import datetime

# Environment variables for easy configuration
API_ENDPOINT = "https://api.opendota.com/api/matches/{match_id}"
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
API_KEY = os.getenv("API_KEY")  # Optional if OpenDota requires an API key

# Initialize S3 client
s3_client = boto3.client("s3")

def lambda_handler(event, context):
    match_id = event.get("match_id", 123456789)  # Example match ID; replace with logic to cycle through match IDs
    
    try:
        # Call the OpenDota API
        response = requests.get(API_ENDPOINT.format(match_id=match_id), params={'api_key': API_KEY})
        response.raise_for_status()
        
        # Load JSON response data
        match_data = response.json()
        
        # Define S3 key for storing the JSON data with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        s3_key = f"match_data/match_{match_id}_{timestamp}.json"
        
        # Upload the JSON data to S3
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(match_data),
            ContentType="application/json"
        )
        
        print(f"Match data for match_id {match_id} saved to S3 as {s3_key}")
        
        return {
            "statusCode": 200,
            "body": f"Match data for match_id {match_id} saved successfully."
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching match data: {e}")
        return {
            "statusCode": 500,
            "body": f"Error: {e}"
        }
        