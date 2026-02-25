import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="EduPerform Pro | Intelligence Suite",
    page_icon="⚡",
    layout="wide",
)

# --- THEME & LAYOUT CSS ---
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
        color: #f8fafc;
    }

    /* Target the Streamlit Container for unified Glass Boxes */
    [data-testid="stVerticalBlock"] > div:has(div.glass-inner) {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
        animation: slideUp 0.8s ease-out;
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Metric Containers */
    .metric-card {
        background: rgba(99, 102, 241, 0.05);
        border: 1px solid rgba(99, 102, 241, 0.2);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        transition: 0.3s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        background: rgba(99, 102, 241, 0.1);
        border-color: #818cf8;
    }
    .metric-val { font-size: 2rem; font-weight: 800; color: #818cf8; }
    .metric-lab { font-size: 0.7rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.5px; }

    /* Login Page Centering */
    .login-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- DATA GENERATION (Varied >20%) ---
def get_data():
    teachers = ["Elena Rodriguez", "Marcus Chen", "Sarah Jenkins", "David Okafor", "Priya Sharma"]
    stats = {"Staff Strength": 62, "Retention Risk": 5, "Incident Log": 112, "Efficiency Index": "88%"}
    return teachers, stats

teachers, dashboard_stats = get_data()

# --- LOGIN PAGE ---
def login_page():
    _, col, _ = st.columns([1, 1.8, 1])
    with col:
        st.markdown('<div style="margin-top: 100px;"></div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="login-box">
                <h1 style='color: #818cf8; margin: 0;'>EduPerform</h1>
                <p style='color: #94a3b8;'>Academic Intelligence Portal</p>
            </div>
        """, unsafe_allow_html=True)
        with st.form("login_form"):
            st.text_input("Username", value="admin")
            st.text_input("Password", type="password", value="admin")
            if st.form_submit_button("Authenticate"):
                st.session_state['logged_in'] = True
                st.rerun()

# --- DASHBOARD VIEW ---
def main_dashboard():
    st.title("🏛️ Institutional Overview")
    m1, m2, m3, m4 = st.columns(4)
    items = list(dashboard_stats.items())
    for i, col in enumerate([m1, m2, m3, m4]):
        with col:
            st.markdown(f'<div class="metric-card"><div class="metric-lab">{items[i][0]}</div><div class="metric-val">{items[i][1]}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        with st.container():
            st.markdown('<div class="glass-inner"></div>', unsafe_allow_html=True)
            st.subheader("Faculty Performance by Department")
            df = pd.DataFrame({'Dept': ['Science', 'Arts', 'Math', 'PE', 'Lang'] * 4, 'Score': np.random.randint(65, 95, 20)})
            fig = px.box(df, x='Dept', y='Score', color='Dept', color_discrete_sequence=px.colors.qualitative.Pastel)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", margin=dict(t=10))
            st.plotly_chart(fig, use_container_width=True)
    with c2:
        with st.container():
            st.markdown('<div class="glass-inner"></div>', unsafe_allow_html=True)
            st.subheader("Task Completion")
            fig_pie = go.Figure(data=[go.Pie(labels=['On-Track', 'Delayed', 'Pending'], values=[70, 15, 15], hole=.6, marker_colors=['#818cf8', '#f59e0b', '#ef4444'])])
            fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", showlegend=False)
            st.plotly_chart(fig_pie, use_container_width=True)

# --- TEACHER VIEW ---
def teacher_tab():
    st.title("👤 Faculty Profiles")
    selected = st.selectbox("Select Faculty Member", teachers)
    col_a, col_b = st.columns([1, 2])
    with col_a:
        with st.container():
            st.markdown('<div class="glass-inner"></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align:center;"><img src="https://ui-avatars.com/api/?name={selected.replace(" ", "+")}&background=818cf8&color=fff&size=128" style="border-radius:50%; margin-bottom:15px;"><h3>{selected}</h3><p style="color:#94a3b8;">Senior Faculty</p></div>', unsafe_allow_html=True)
    with col_b:
        with st.container():
            st.markdown('<div class="glass-inner"></div>', unsafe_allow_html=True)
            st.subheader("Pedagogical Competency Wheel")
            fig = go.Figure(data=go.Scatterpolar(r=[np.random.randint(70, 95) for _ in range(5)], theta=['Tech', 'Engagement', 'Curriculum', 'Assessment', 'Feedback'], fill='toself', line_color='#818cf8'))
            fig.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=True, range=[0, 100])), paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8")
            st.plotly_chart(fig, use_container_width=True)

# --- RISK & ATTRITION VIEW (Interactive & Fixed) ---
def attrition_tab():
    st.title("⚠️ Risk Analysis & Attendance")
    
    # Interaction Widgets
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        risk_threshold = st.slider("Risk Sensitivity Threshold", 0, 100, 65)
    with col_w2:
        dept_filter = st.multiselect("Filter Departments", ['Science', 'Math', 'Arts', 'Languages'], default=['Science', 'Math', 'Arts', 'Languages'])

    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="glass-inner"></div>', unsafe_allow_html=True)
        st.subheader("Departmental Lateness Distribution & Risk Level")
        risk_data = pd.DataFrame({
            'Department': ['Science', 'Math', 'Arts', 'Languages'],
            'Low Risk': [15, 12, 18, 10],
            'High Risk': [2, 1, 4, 3]
        })
        filtered_data = risk_data[risk_data['Department'].isin(dept_filter)]
        fig = px.bar(filtered_data, x='Department', y=['Low Risk', 'High Risk'], 
                     color_discrete_map={'Low Risk': '#818cf8', 'High Risk': '#ef4444'}, barmode='stack')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8")
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('<div class="glass-inner"></div>', unsafe_allow_html=True)
        st.subheader("Lateness vs Performance Correlation")
        scatter_df = pd.DataFrame({'Late': np.random.randint(0, 15, 40), 'Score': np.random.randint(60, 100, 40)})
        fig_scatter = px.scatter(scatter_df, x='Late', y='Score', trendline="ols", color_discrete_sequence=['#a855f7'])
        fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8")
        st.plotly_chart(fig_scatter, use_container_width=True)

# --- NAVIGATION ---
if not st.session_state['logged_in']:
    login_page()
else:
    with st.sidebar:
        st.markdown("<h2 style='color:#818cf8;'>EduPerform</h2>", unsafe_allow_html=True)
        choice = st.radio("Navigation", ["Dashboard", "Faculty Profiles", "Risk & Attrition"])
        if st.button("Sign Out"):
            st.session_state['logged_in'] = False
            st.rerun()

    if choice == "Dashboard": main_dashboard()
    elif choice == "Faculty Profiles": teacher_tab()
    elif choice == "Risk & Attrition": attrition_tab()