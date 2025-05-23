import requests
import pandas as pd

# Set up the basic request parameters
base_params = {
    'api_key': 'C05AAB4D47E6404E90F577EB203A8F28',  # Replace with your actual VALUESERP API key
    'location': 'United Kingdom',
    'google_domain': 'google.com',
    'gl': 'uk',
    'hl': 'en',
    'device': 'desktop',
    'include_answer_box': 'true',
    'num': '10',
    'output': 'json'
}

# Define the list of queries
queries = ['construction software', 'construction management software', 'construction project management software', 'construction estimating software', 'construction document management software', 'construction bidding software', 'best construction management software', 'best construction project management software']

# Initialize an empty list to hold all results
all_results = []

# Loop over each query
for query in queries:
    # Update the query parameter
    params = base_params.copy()
    params['q'] = query

    # Make the HTTP GET request
    api_result = requests.get('https://api.valueserp.com/search', params=params)

    # Check if the request was successful
    if api_result.status_code == 200:
        # Parse the JSON response
        data = api_result.json()

        # Extract results
        results = data.get('organic_results', [])

        # Append results with query info to the list
        for index, result in enumerate(results, start=1):
            all_results.append({
                "Query": query,
                "Result Number": index,
                "Title": result.get('title', 'N/A'),
                "Link": result.get('link', 'N/A'),
                "Snippet": result.get('snippet', 'N/A')
            })
    else:
        print(f"Error for query '{query}': {api_result.status_code}")

# Create a DataFrame for all queries
df = pd.DataFrame(all_results)

# Export DataFrame to CSV in the current directory
csv_file_path = 'search_results.csv'
df.to_csv(csv_file_path, index=False)

print(f"Data has been saved to {csv_file_path}")
