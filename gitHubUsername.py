#GIT HUB USERNAME INFORMATION EXTRACTOR 

# Import libraries
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt


# Function to fetch GitHub user data using GitHub API
def get_github_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json()
#return response.json()converts this JSON content into a Python dictionary
#JSON: GitHub API typically returns data in JSON format


# Function to extract relevant information using regular expressions
    # Extracts counts of followers, following, and public repositories
    # The extracted counts are then returned as a dictionary
def extract_information(data):
    pattern = r"\d+"
    # d+: finds and captures one or more digits 
    followers_count = re.search(pattern, str(data['followers']))[0]
    following_count = re.search(pattern, str(data['following']))[0]
    repositories_count = re.search(pattern, str(data['public_repos']))[0]
    return {
        'Followers': int(followers_count),
        'Following': int(following_count),
        'Repositories': int(repositories_count)
    }
# re.search: Finds the first occurrence of the pattern (one or more digits) in the string representation


# Function to create a bar chart using Matplotlib
    #takes the extracted data (dictionary) as input.
    #converts the data into a Pandas DataFrame and uses Matplotlib to create a bar chart.
    #The bar chart shows the counts of followers, following, and public repositories.
    #VERY Similar to rstudio
def plot_data(data):
    df = pd.DataFrame(list(data.items()), columns=['Category', 'Count'])
    df.plot(x='Category', y='Count', kind='bar', legend=False)
    plt.title('GitHub User Data')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()


# THE MAIN FUNCTION OF THE PROGRAM
def main():
    # Input GitHub username
    username = input("Enter GitHub username: ")

    # Fetches GitHub user data
    user_data = get_github_user_data(username)

    # Extracts relevant information
    extracted_data = extract_information(user_data)

    # Display extracted information
    print("\n Here is your Extracted Information:")
    for key, value in extracted_data.items():
        print(f"{key}: {value}")
#key takes on the values 'Followers', 'Following', and 'Repositories'
#value takes on the corresponding counts

    # Plot data using Matplotlib
    plot_data(extracted_data)

if __name__ == "__main__":
    main()

