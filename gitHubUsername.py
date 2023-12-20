# Import libraries
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt

#ADVANCED TOPIC 1 
# Function to fetch GitHub user data using GitHub API
def get_github_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json()
#return response.json()converts this JSON content into a Python dictionary
#JSON: GitHub API typically returns data in JSON format


# Function to extract relevant information using regular expressions
def extract_information(data):
    pattern = r"\d+"
    followers_count = re.search(pattern, str(data['followers']))[0]
    following_count = re.search(pattern, str(data['following']))[0]
    repositories_count = re.search(pattern, str(data['public_repos']))[0]
    return {
        'Followers': int(followers_count),
        'Following': int(following_count),
        'Repositories': int(repositories_count)
    }

# Function to create a bar chart using Matplotlib
def plot_data(data):
    df = pd.DataFrame(list(data.items()), columns=['Category', 'Count'])
    df.plot(x='Category', y='Count', kind='bar', legend=False)
    plt.title('GitHub User Data')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

# Main function
def main():
    # Input GitHub username
    username = input("Enter GitHub username: ")

    # Fetch GitHub user data
    user_data = get_github_user_data(username)

    # Extract relevant information
    extracted_data = extract_information(user_data)

    # Display extracted information
    print("\nExtracted Information:")
    for key, value in extracted_data.items():
        print(f"{key}: {value}")

    # Plot data using Matplotlib
    plot_data(extracted_data)

if __name__ == "__main__":
    main()

