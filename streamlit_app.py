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
selected_path = st.sidebar.selectbox("Choose a Path:", ["Frontend Development", "Backend Development", "DevOps", "Data Science", "Data Engineering"])

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
    },
    "Data Engineering": {
        "Data Warehousing": "Understand the principles of data warehousing and ETL processes.",
        "Big Data Technologies": "Familiarize yourself with technologies like Hadoop and Spark.",
        "Data Modeling": "Learn about data modeling techniques for organizing data efficiently.",
        "Data Pipelines": "Explore tools and techniques for building data pipelines.",
        "Cloud Services": "Get familiar with cloud data services like AWS Redshift or Google BigQuery."
    }
}

# Main content based on the selected roadmap
st.title(f"{selected_path} Roadmap")

# Special handling for Frontend Development
if selected_path == "Frontend Development":
    st.markdown("### Frontend Development Roadmap")
    st.image("https://github.com/Meshugah/FullStack-Roadmap/raw/master/frontend.png", caption="Frontend Development Roadmap")
    
    # Create buttons for Frontend topics
    st.markdown("### Explore Frontend Topics")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("HTML & CSS"):
            st.write("Learn the basics of HTML and CSS for structuring and styling web pages.")
        
        if st.button("JavaScript"):
            st.write("Understand core JavaScript concepts like variables, functions, and DOM manipulation.")

    with col2:
        if st.button("React.js"):
            st.write("Dive into React.js for building modern frontend applications.")
        
        if st.button("Version Control"):
            st.write("Get familiar with Git and GitHub for version control.")

# Special handling for Backend Development
elif selected_path == "Backend Development":
    st.markdown("### Backend Development Roadmap")
    st.image("https://github.com/Meshugah/FullStack-Roadmap/raw/master/backend.png", caption="Backend Development Roadmap")
    
    # Create buttons for Backend topics
    st.markdown("### Explore Backend Topics")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Programming Languages"):
            st.write("Learn Python, Java, or Node.js for backend development.")
        
        if st.button("APIs"):
            st.write("Understand how to build REST APIs and handle HTTP requests.")

    with col2:
        if st.button("Databases"):
            st.write("Familiarize yourself with databases like MySQL, PostgreSQL, or MongoDB.")
        
        if st.button("Authentication"):
            st.write("Learn how to handle user authentication using JWT, OAuth, etc.")

# Special handling for Data Science
elif selected_path == "Data Science":
    st.markdown("### Data Science Roadmap")
    st.image("https://user-images.githubusercontent.com/20041231/211718743-d6604ff7-8828-422b-9b60-ec156cdaf054.JPG", caption="Data Science Roadmap")
    
    # Create buttons for Data Science topics
    st.markdown("### Explore Data Science Topics")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Python Libraries"):
            st.write("Master data manipulation libraries like Pandas and Numpy.")
        
        if st.button("Data Visualization"):
            st.write("Create visualizations using Matplotlib, Seaborn, or Plotly.")

    with col2:
        if st.button("Machine Learning"):
            st.write("Learn the basics of supervised and unsupervised machine learning.")
        
        if st.button("Deep Learning"):
            st.write("Get familiar with frameworks like TensorFlow and PyTorch.")

# Special handling for Data Engineering
elif selected_path == "Data Engineering":
    st.markdown("### Data Engineering Roadmap")
    st.image("https://github.com/ErdemOzgen/Data-Engineering-Roadmap/raw/main/DataEngRoadmapFull.png", caption="Data Engineering Roadmap")
    
    # Create buttons for Data Engineering topics
    st.markdown("### Explore Data Engineering Topics")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Data Warehousing"):
            st.write("Understand the principles of data warehousing and ETL processes.")
        
        if st.button("Big Data Technologies"):
            st.write("Familiarize yourself with technologies like Hadoop and Spark.")

    with col2:
        if st.button("Data Modeling"):
            st.write("Learn about data modeling techniques for organizing data efficiently.")
        
        if st.button("Data Pipelines"):
            st.write("Explore tools and techniques for building data pipelines.")

# Special handling for DevOps
elif selected_path == "DevOps":
    # Display the DevOps roadmap image
    st.markdown("### Explore Topics in the DevOps Roadmap")
    st.image("https://github.com/milanm/DevOps-Roadmap/raw/master/DevOps%20Roadmap.png", caption="DevOps Roadmap")

    # Create buttons for each topic in the image
    st.markdown("### Explore DevOps Topics")

    # Create a layout with columns to simulate buttons near the image
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust columns to simulate positioning

    with col1:
        # Buttons aligned to left
        if st.button("Version Control"):
            st.write("Learn Git for source code management, including branching, merging, and workflows.")

        if st.button("Containerization"):
            st.write("Explore Docker and Kubernetes for container management and orchestration in production environments.")

    with col2:
        # Buttons aligned near the center
        if st.button("CI/CD"):
            st.write("CI/CD stands for Continuous Integration and Continuous Deployment. Use tools like Jenkins, GitHub Actions, or CircleCI.")

    with col3:
        # Buttons aligned to the right
        if st.button("Cloud Providers"):
            st.write("Get familiar with cloud platforms like AWS, GCP, or Azure for deploying and scaling applications.")

        if st.button("Monitoring"):
            st.write("Learn to use tools like Prometheus and Grafana to monitor applications and infrastructure.")

# Footer
st.markdown("---")
st.markdown("Created by [M L R GOUTHAM](https://www.linkedin.com/in/mlr-goutham-6a31962aa/)")
