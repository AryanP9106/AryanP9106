import streamlit as st
from pathlib import Path

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aryan Pattani · Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Load resume PDF (optional — only shows if the file exists alongside app.py) ─
_resume_path = Path(__file__).parent / "Aryan_Pattani_resume.pdf"
_resume_bytes = _resume_path.read_bytes() if _resume_path.exists() else None

# ══════════════════════════════════════════════════════════════════════════════
# THEME CATALOGUE
# ══════════════════════════════════════════════════════════════════════════════
FONT_PAIRS = {
    "Ocean (Default)": {
        "heading": "Syne",
        "mono":    "IBM Plex Mono",
        "import":  "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Syne:wght@700;800&display=swap",
    },
    "Sharp": {
        "heading": "Space Grotesk",
        "mono":    "Fira Code",
        "import":  "https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Space+Grotesk:wght@700;800&display=swap",
    },
    "Editorial": {
        "heading": "DM Serif Display",
        "mono":    "Source Code Pro",
        "import":  "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Source+Code+Pro:wght@400;600&display=swap",
    },
    "Clean": {
        "heading": "Inter",
        "mono":    "JetBrains Mono",
        "import":  "https://fonts.googleapis.com/css2?family=Inter:wght@700;800&family=JetBrains+Mono:wght@400;600&display=swap",
    },
    "Futuristic": {
        "heading": "Orbitron",
        "mono":    "Share Tech Mono",
        "import":  "https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800&family=Share+Tech+Mono&display=swap",
    },
}
COLOR_THEMES = {
    "Ocean (Default)": {"accent": "#4d9fff", "bg": "#0a0c0f", "card_bg": "#0d141e", "border": "#1a2030"},
    "Terminal":        {"accent": "#00ff88", "bg": "#0a0c0f", "card_bg": "#0d1a12", "border": "#1a2030"},
    "Amber":           {"accent": "#ffb347", "bg": "#0c0a06", "card_bg": "#1a1208", "border": "#2a1e0a"},
    "Violet":          {"accent": "#a855f7", "bg": "#08060f", "card_bg": "#120d1e", "border": "#1e1030"},
    "Cyan":            {"accent": "#00e5ff", "bg": "#060c0f", "card_bg": "#0a1820", "border": "#0f2530"},
    "Crimson":         {"accent": "#ff3355", "bg": "#0f0608", "card_bg": "#1e0a0e", "border": "#300a12"},
    "Teal":            {"accent": "#14b8a6", "bg": "#060f0e", "card_bg": "#0a1a18", "border": "#0f2825"},
    "Catppuccin":      {"accent": "#cba6f7", "bg": "#11111b", "card_bg": "#1e1e2e", "border": "#313244"},
}

# ── Session state defaults ─────────────────────────────────────────────────────
if "show_settings" not in st.session_state:
    st.session_state.show_settings = False
if "color_val" not in st.session_state:
    st.session_state.color_val = "Ocean (Default)"
if "font_val" not in st.session_state:
    st.session_state.font_val = "Ocean (Default)"

font  = FONT_PAIRS[st.session_state.font_val]
theme = COLOR_THEMES[st.session_state.color_val]
accent, bg, card_bg, border = theme["accent"], theme["bg"], theme["card_bg"], theme["border"]
heading_fn, mono_fn = font["heading"], font["mono"]

# ── Dynamic CSS ────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('{font["import"]}');
[data-testid="stAppViewContainer"], [data-testid="stMain"], .main {{
    background-color: {bg} !important;
}}
[data-testid="stHeader"], footer, [data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stSidebar"] {{ display: none !important; }}
h1, h2, h3, h4 {{ font-family: '{heading_fn}', sans-serif !important; color: #eaf0f8 !important; }}
h2 {{ font-size: 26px !important; }}
h3 {{ font-size: 22px !important; }}
h4 {{ font-size: 18px !important; }}
p, li, div, span, label {{ color: #c8d6e5; }}
[data-testid="stMetricLabel"] > div {{
    color: #5a7a9a !important;
    font-size: 11px !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-family: '{mono_fn}', monospace !important;
}}
[data-testid="stMetricValue"] > div {{
    color: {accent} !important;
    font-size: 22px !important;
    font-family: '{mono_fn}', monospace !important;
}}
code {{
    background: {card_bg} !important;
    color: #7aafd4 !important;
    border: 1px solid {border} !important;
    border-radius: 2px !important;
    font-family: '{mono_fn}', monospace !important;
    padding: 2px 8px !important;
}}
hr {{ border-color: {border} !important; margin: 8px 0 !important; }}
[data-testid="stExpander"] {{
    background: {card_bg} !important;
    border: 1px solid {border} !important;
    border-radius: 0 !important;
    transition: border-color 0.2s;
}}
[data-testid="stExpander"]:hover {{ border-color: {accent}40 !important; }}
[data-testid="stExpander"] summary {{
    color: #eaf0f8 !important;
    font-family: '{heading_fn}', sans-serif !important;
    font-weight: 700 !important;
    font-size: 20px !important;
}}
[data-testid="stLinkButton"] > a {{
    background: {card_bg} !important;
    border: 1px solid {accent}40 !important;
    color: {accent} !important;
    border-radius: 0 !important;
    font-family: '{mono_fn}', monospace !important;
    font-size: 12px !important;
    letter-spacing: 1px;
}}
[data-testid="stLinkButton"] > a:hover {{
    background: {accent}15 !important;
    border-color: {accent}88 !important;
    color: {accent} !important;
}}
[data-testid="stDownloadButton"] > button {{
    background: {card_bg} !important;
    border: 1px solid {accent}55 !important;
    color: {accent} !important;
    border-radius: 0 !important;
    font-family: '{mono_fn}', monospace !important;
    font-size: 12px !important;
    letter-spacing: 1px;
    padding: 8px 20px !important;
}}
[data-testid="stDownloadButton"] > button:hover {{
    background: {accent}20 !important;
    border-color: {accent} !important;
    color: #fff !important;
}}
[data-testid="stCaptionContainer"] p {{
    color: #a0b8d0 !important;
    font-family: '{mono_fn}', monospace !important;
    font-size: 12px !important;
}}
[data-testid="stExpander"] [data-testid="stCaptionContainer"] p {{
    color: #c8d6e5 !important;
}}
[data-testid="stExpander"] p,
[data-testid="stExpander"] div,
[data-testid="stExpander"] span {{
    color: #eaf0f8 !important;
}}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def section_header(title: str):
    st.markdown(
        f"<p style='font-size:15px;letter-spacing:4px;text-transform:uppercase;"
        f"color:{accent};opacity:0.85;font-family:{mono_fn},monospace;font-weight:600;"
        f"margin:0 0 4px 0;'>// {title}</p>",
        unsafe_allow_html=True,
    )
    st.divider()


def skill_row(category: str, skills: list):
    st.markdown(
        f"<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        f"color:#3a5a8a;font-family:{mono_fn},monospace;margin:18px 0 6px;font-weight:600;'>"
        f"{category}</p>",
        unsafe_allow_html=True,
    )
    st.markdown("&nbsp;&nbsp;".join(f"`{s}`" for s in skills))


def project_card(title: str, desc: str, tags: list, gh_url: str):
    with st.expander(title):
        st.caption(desc)
        st.markdown("&nbsp;&nbsp;".join(f"`{t}`" for t in tags))
        st.write("")
        st.link_button("→ GitHub", gh_url)


# ══════════════════════════════════════════════════════════════════════════════
# FLOATING SETTINGS BUTTON + PANEL
# ══════════════════════════════════════════════════════════════════════════════
if st.button("⚙", key="fab", help="Customise theme"):
    st.session_state.show_settings = not st.session_state.show_settings

if st.session_state.show_settings:
    with st.container():
        st.markdown(
            f"<p style='font-size:10px;letter-spacing:3px;text-transform:uppercase;"
            f"color:{accent};font-family:{mono_fn},monospace;margin-bottom:8px;'>// Customise</p>",
            unsafe_allow_html=True,
        )

        def save_color():
            st.session_state.color_val = st.session_state.color_widget

        def save_font():
            st.session_state.font_val = st.session_state.font_widget

        st.selectbox(
            "Colour Theme", list(COLOR_THEMES.keys()),
            index=list(COLOR_THEMES.keys()).index(st.session_state.color_val),
            key="color_widget", on_change=save_color,
        )
        st.selectbox(
            "Font Pair", list(FONT_PAIRS.keys()),
            index=list(FONT_PAIRS.keys()).index(st.session_state.font_val),
            key="font_widget", on_change=save_font,
        )
        st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
GITHUB_URL = "https://github.com/AryanP9106"
LINKEDIN_URL = "https://www.linkedin.com/in/aryan-pattani-140976349"
INSTAGRAM_URL = "https://instagram.com/aryan_pattani"
EMAIL = "aryanpattani94@gmail.com"

st.write("")
st.markdown(
    f"<h1 style='font-size:clamp(48px,8vw,88px);font-weight:800;line-height:0.95;"
    f"letter-spacing:-3px;margin-bottom:16px;font-family:{heading_fn},sans-serif;'>"
    f"Aryan <span style='color:{accent};'>Pattani</span></h1>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<p style='font-size:13px;color:#5a7a9a;line-height:1.8;max-width:580px;"
    f"font-family:{mono_fn},monospace;margin-bottom:28px;'>"
    "AI &amp; Backend Engineer.<br>"
    "Building automated pipelines, data-driven tools &amp; robust backend systems."
    "</p>",
    unsafe_allow_html=True,
)

h1, h2, h3, h4, h5, _ = st.columns([1, 1, 1, 1, 1, 1])
with h1:
    st.link_button("⌥ GitHub", GITHUB_URL)
with h2:
    st.link_button("⌘ LinkedIn", LINKEDIN_URL)
with h3:
    st.link_button("✦ Instagram", INSTAGRAM_URL)
with h4:
    st.link_button(f"✉ Email", f"mailto:{EMAIL}")
with h5:
    if _resume_bytes:
        st.download_button(
            label="⤓ Resume",
            data=_resume_bytes,
            file_name="Aryan_Pattani_resume.pdf",
            mime="application/pdf",
        )

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# SKILLS (pulled from tech-stack badges on his GitHub profile README)
# ══════════════════════════════════════════════════════════════════════════════
section_header("Technical Skills")
skill_row("Languages",         ["Python", "C", "C++", "Java", "Dart", "Kotlin", "R", "Bash", "SQL", "HTML5", "CSS3"])
skill_row("Frameworks",        ["Streamlit", "Flask", "Django", "FastAPI", "Flutter", "Node.js", "TailwindCSS"])
skill_row("Tools & Platforms", ["Git / GitHub", "Firebase", "PostgreSQL", "MySQL", "SQLite", "MongoDB", "Render", "Notion", "Arduino"])
st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# PROJECTS (descriptions verified against live GitHub repo list)
# ══════════════════════════════════════════════════════════════════════════════
section_header("Projects")

projects = [
    ("AI PPT Generator",
     "A Python-based application that leverages image generation APIs and structured "
     "document parsing to automatically assemble formatted PowerPoint presentations "
     "from text descriptions.",
     ["Python", "APIs", "Automation"],
     f"{GITHUB_URL}/ai-ppt-generator"),
    ("Customer Churn Action System",
     "A diagnostic analysis project focused on cleaning and modeling business datasets "
     "to predict customer attrition, using exploratory data analysis to surface retention insights.",
     ["Python", "Jupyter Notebook", "Pandas", "Data Analysis"],
     f"{GITHUB_URL}/customer-churn-action-system"),
    ("Task Management",
     "A task management application built in Python.",
     ["Python", "Backend"],
     f"{GITHUB_URL}/Task_Management"),
    ("Trading Bot",
     "An automated trading bot built in Python for analyzing market data and "
     "executing strategy-driven decisions.",
     ["Python", "Finance", "Automation"],
     f"{GITHUB_URL}/trading_bot"),
    ("AQI Analysis",
     "An analysis of Air Quality Index (AQI) reports across several Indian states.",
     ["Python", "Jupyter Notebook", "Pandas"],
     f"{GITHUB_URL}/aqi_analysis")
]

col_a, col_b, col_c = st.columns(3)
cols = [col_a, col_b, col_c]
for i, (title, desc, tags, gh) in enumerate(projects):
    with cols[i % 3]:
        project_card(title, desc, tags, gh)

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# EDUCATION — placeholder (couldn't verify via LinkedIn, which blocks scraping)
# ══════════════════════════════════════════════════════════════════════════════
section_header("Education")

e1_left, e1_right = st.columns([1, 4])
with e1_left:
    st.metric("CGPA", "7.76")
with e1_right:
    st.subheader("Diploma in Information Communication Technology")
    st.write("**Marwadi University** · Rajkot, Gujarat")
    st.caption("June 2024 - March 2027")

st.write("")
st.divider()

section_header("Certifications & Activites")
cert_cols, club_cols = st.columns(2)

with cert_cols:
    for cert in ["FOSSEE Arduino Day 2026 (College Edition)", "Data Science Essentials with Python"]:
        st.write(f"• {cert}")
with club_cols:
    st.write("• Cloud Computing & DevOps Club")
    st.write("• CP Club")
    st.write("• 10X Club")

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"<p style='text-align:center;font-size:11px;color:#1e3a5a;"
    f"font-family:{mono_fn},monospace;letter-spacing:1px;padding:24px 0;'>"
    "⌥ &nbsp;Aryan Pattani · 2026 &nbsp;·&nbsp; Built with Python &amp; Streamlit &nbsp;⌘"
    "</p>",
    unsafe_allow_html=True,
)