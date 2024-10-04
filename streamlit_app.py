# roadmap_app.py
import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Roadmap App", layout="wide")

# Function to fetch additional information about a topic (for DevOps roadmap)
def get_topic_info(topic):
    topic_info = {
        "Version Control": "Learn Git for source code management, including branching, merging, and GitHub workflows.",
        "CI/CD": "Understand Continuous Integration and Continuous Deployment using tools like Jenkins, GitHub Actions, or CircleCI.",
        "Containerization": "Explore Docker and Kubernetes for container management and orchestration in development and production environments.",
        "Cloud Providers": "Get familiar with cloud platforms like AWS, GCP, or Azure to deploy and scale applications.",
        "Monitoring": "Set up monitoring tools like Prometheus and Grafana to track the health and performance of your applications.",
    }
    return topic_info.get(topic, "Information not available")


# Sidebar for selecting career path/technology
st.sidebar.title("Roadmap Explorer")
selected_path = st.sidebar.selectbox("Choose a Path:", ["Frontend Development", "Backend Development", "DevOps", "Data Science"])

# Dictionary of roadmaps (Text-based for all roles except DevOps, where image and buttons will be used)
roadmaps = {
    "Frontend Development": {
        "HTML & CSS": "Learn the basics of HTML and CSS for structuring and styling web pages.",
        "JavaScript": "Understand core JavaScript concepts like variables, functions, and DOM manipulation.",
        "React.js": "Dive into React.js for building modern frontend applications.",
        "Version Control": "Get familiar with Git and GitHub for version control.",
        "CSS Frameworks": "Explore frameworks like Bootstrap, Tailwind CSS for faster UI design."
    },
    "Backend Development": {
        "Programming Languages": "Learn Python, Java, or Node.js for backend development.",
        "APIs": "Understand how to build REST APIs and handle HTTP requests.",
        "Databases": "Familiarize yourself with databases like MySQL, PostgreSQL, or MongoDB.",
        "Authentication": "Learn how to handle user authentication using JWT, OAuth, etc.",
        "Deployment": "Deploy your backend services using platforms like Heroku or AWS."
    },
    "Data Science": {
        "Python Libraries": "Master data manipulation libraries like Pandas and Numpy.",
        "Data Visualization": "Create visualizations using Matplotlib, Seaborn, or Plotly.",
        "Machine Learning": "Learn the basics of supervised and unsupervised machine learning.",
        "Deep Learning": "Get familiar with frameworks like TensorFlow and PyTorch.",
        "Data Wrangling": "Work with large datasets and clean data for analysis."
    }
}

# Main content based on the selected roadmap
st.title(f"{selected_path} Roadmap")

# Special handling for DevOps (displaying image with clickable topics)
if selected_path == "DevOps":
    # Display the DevOps roadmap image
    st.image("https://github.com/milanm/DevOps-Roadmap/raw/master/DevOps%20Roadmap.png", caption="DevOps Roadmap")

    # Create buttons for each topic in the image
    st.markdown("### Explore Topics in the DevOps Roadmap")
    
    # Buttons for each topic
    if st.button("Version Control"):
        info = get_topic_info("Version Control")
        st.write(info)

    if st.button("CI/CD"):
        info = get_topic_info("CI/CD")
        st.write(info)

    if st.button("Containerization"):
        info = get_topic_info("Containerization")
        st.write(info)

    if st.button("Cloud Providers"):
        info = get_topic_info("Cloud Providers")
        st.write(info)

    if st.button("Monitoring"):
        info = get_topic_info("Monitoring")
        st.write(info)

# Default roadmaps for other paths (Frontend Development, Backend Development, Data Science)
elif selected_path in roadmaps:
    for topic, description in roadmaps[selected_path].items():
        with st.expander(topic):
            st.write(description)

# Footer
st.markdown("---")
st.markdown("Created by [Your Name](https://your-profile-link)")
