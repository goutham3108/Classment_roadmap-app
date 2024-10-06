import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to scrape the roadmap for a specific role
def scrape_roadmap(role):
    # URL of the roadmap.sh role page
    url = f"https://roadmap.sh/{role}"
    
    # Make a request to fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve the roadmap. Please try again."
    
    # Parse the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the relevant data from the page
    roadmap_data = []
    for section in soup.find_all('section'):
        heading = section.find('h2')
        if heading:
            heading_text = heading.get_text().strip()
            roadmap_data.append(f"## {heading_text}\n")
        for topic in section.find_all('li'):
            topic_text = topic.get_text().strip()
            roadmap_data.append(f"- {topic_text}")
    
    # Return the scraped data as a string
    return "\n".join(roadmap_data)

# Streamlit app to display the roadmaps
st.title("Roadmap Explorer")

# Create a sidebar to select the role
role = st.sidebar.selectbox("Select a Role:", ["frontend", "backend", "devops", "data-engineer"])

# When a role is selected, scrape and display its roadmap
if role:
    st.markdown(f"### {role.capitalize()} Roadmap")
    
    roadmap_content = scrape_roadmap(role)  # Scrape the roadmap for the selected role
    
    if roadmap_content:
        st.markdown(roadmap_content)  # Display the scraped data
    else:
        st.error("Unable to load the roadmap content.")
