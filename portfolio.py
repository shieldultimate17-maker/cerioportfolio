
#Project: Portfolio Website with Streamlit
#Author: Cerio S. Gbedee


import streamlit as st
from PIL import Image

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💼",
    layout="wide"
)

# ----------------------------
# Header Section
# ----------------------------
with st.container():
    st.title("Hi, I'm cerio 👋")
    st.subheader("Ethical Hacker | A+ Hardware | Tech Enthusiast")
    st.write("Welcome to my portfolio website built with Streamlit!")

# ----------------------------
# Sidebar Navigation
# ----------------------------
st.sidebar.title("🔎 Navigation")
selection = st.sidebar.radio("Go to:", ["Home", "About Me", "Skills", "Projects", "Contact"])

# ----------------------------
# Home Section
# ----------------------------
if selection == "Home":
    st.image("https://images.unsplash.com/photo-1508780709619-79562169bc64", use_column_width=True)
    st.write(
        """
        This website showcases my **skills, projects, and experiences**.  
        Use the sidebar to navigate between sections.  
        """
    )

# ----------------------------
# About Section
# ----------------------------
elif selection == "About Me":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://randomuser.me/api/portraits/men/75.jpg", width=250)
        with col2:
            st.header("About Me")
            st.write(
                """
                I'm a passionate tech professional with a love for solving problems using 
                data, code, and creativity. My journey started with programming in Python, 
                and now I build full-stack applications, dashboards, and AI-powered tools.  

                Outside of work, I enjoy reading, traveling, and photography 📸.
                """
            )

# ----------------------------
# Skills Section
# ----------------------------
elif selection == "Skills":
    st.header("🛠️ Skills")
    skill_cols = st.columns(3)

    with skill_cols[0]:
        st.subheader("Programming")
        st.write("- Python 🐍\n- JavaScript\n- SQL\n- ")

    with skill_cols[1]:
        st.subheader("CyberSecurity")
        st.write("- Wireless Hacking ⚡\n- System Penetration\n- Pentesting\n- Bruteforce")

    with skill_cols[2]:
        st.subheader("Tools & Others")
        st.write("- Git & GitHub 🐙\n- Armitage 🐳\n- Linux 🐧\n- Njrat")

# ----------------------------
# Projects Section
# ----------------------------
elif selection == "Projects":
    st.header("📂 Projects Showcase")

    project_data = [
        {
            "title": "📊 Sales Dashboard",
            "desc": "An interactive dashboard analyzing sales data using Streamlit and Plotly.",
            "link": "https://github.com/shieldultimate17-maker/sales-dashboard"
        },
        {
            "title": "🤖 Chatbot Assistant",
            "desc": "AI-powered chatbot built with Python and NLP libraries.",
            "link": "https://github.com/shieldultimate17-maker"
        },
        {
            "title": "🌐 Cerios' Portfolio Website",
            "desc": "This portfolio website built using Streamlit.",
            "link": "https://www.linkedin.com/in/cerio-gbedee-343a27324/"
            
        }
    ]

    for project in project_data:
        with st.container():
            st.subheader(project["title"])
            st.write(project["desc"])
            st.markdown(f"[🔗 View Project]({project['link']})")
            st.markdown("---")

# ----------------------------
# Contact Section
# ----------------------------
elif selection == "Contact":
    st.header("📬 Get in Touch")
    st.write("I'd love to connect! Feel free to reach out through any of the platforms below:")

    contact_cols = st.columns(3)

    with contact_cols[0]:
        st.markdown("[💼 LinkedIn]( https://www.linkedin.com/in/cerio-gbedee-343a27324/)")

    with contact_cols[1]:
        st.markdown("[🐙 GitHub](https://github.com/shieldultimate17-maker)")

    with contact_cols[2]:
        st.markdown("[✉️ Email Me](shieldultimate17@gmail.com)")

    with st.form("contact_form", clear_on_submit=True):
        st.subheader("📩 Send me a message:")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            if name and email and message:
                st.success("✅ Your message has been sent! I'll reply soon.")
            else:
                st.error("⚠️ Please fill in all fields.")
