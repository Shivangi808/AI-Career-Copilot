import streamlit as st
import pdfplumber

from helpers import (
    extract_skills,
    find_missing_skills,
    learning_recommendations
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Career Copilot",
    layout="wide"
)

# ---------------- COLORS ----------------

BG = "#E8D8C4"
CARD = "#F5EFE6"
WINE = "#6D2932"
DARK_WINE = "#561C24"
BEIGE = "#C7B7A3"
TEXT = "#3D2A2A"

# ---------------- CSS ----------------

st.markdown(f"""
<style>

/* PAGE */

.stApp {{
    background:{BG};
    color:{TEXT};
}}

header {{
    visibility:hidden;
}}

[data-testid="stToolbar"] {{
    display:none;
}}

.block-container {{
    padding-top:4rem;
    padding-left:4rem;
    padding-right:4rem;
}}

/* HERO */

.hero-title {{
    font-size:82px;
    font-weight:700;
    color:{WINE};
    line-height:1;
    margin-bottom:18px;
}}

.hero-sub {{
    font-size:24px;
    color:{WINE};
    margin-bottom:50px;
}}

/* TITLES */

.section-title {{
    color:{WINE};
    font-size:34px;
    font-weight:700;
    margin-bottom:18px;
}}

hr {{
    border:0.5px solid {BEIGE};
    margin:42px 0;
}}

/* SKILLS */

.skill-row {{
    display:flex;
    flex-wrap:wrap;
    gap:12px;
    margin-top:10px;
}}

.skill-pill {{
    background:{WINE};
    color:{CARD};
    padding:10px 20px;
    border-radius:999px;
    font-size:14px;
    font-weight:500;
    display:inline-block;
}}

/* FILE UPLOADER */

[data-testid="stFileUploader"] {{
    background:{CARD} !important;
    border:1.5px solid {BEIGE} !important;
    border-radius:34px !important;
    padding:22px !important;
}}

[data-testid="stFileUploader"] > div {{
    background:transparent !important;
}}

[data-testid="stFileUploader"] section {{
    background:{CARD} !important;
    border:2px dashed {BEIGE} !important;
    border-radius:28px !important;
    padding:30px !important;
}}

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] label {{
    color:{WINE} !important;
}}

[data-testid="stFileUploader"] button {{
    background:{WINE} !important;
    border:none !important;
    border-radius:999px !important;
    padding:10px 24px !important;
    font-weight:600 !important;
}}

[data-testid="stFileUploader"] button:hover {{
    background:{DARK_WINE} !important;
}}

[data-testid="stFileUploader"] button * {{
    color:white !important;
}}

/* TEXT AREA */

[data-testid="stTextArea"] {{
    background:{CARD} !important;
    border:1.5px solid {BEIGE} !important;
    border-radius:34px !important;
    padding:22px !important;
}}

[data-testid="stTextArea"] > div {{
    background:{CARD} !important;
    border:2px dashed {BEIGE} !important;
    border-radius:28px !important;
}}

[data-testid="stTextArea"] label {{
    color:{WINE} !important;
    font-weight:600 !important;
}}

[data-testid="stTextArea"] textarea {{
    background:{CARD} !important;
    color:{TEXT} !important;
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
    font-size:17px !important;
    padding:22px !important;
    min-height:180px !important;
    caret-color:{WINE} !important;
}}

[data-testid="stTextArea"] textarea::placeholder {{
    color:#8B7B70 !important;
}}

/* METRIC */

[data-testid="stMetric"] {{
    background:{CARD} !important;
    border:1px solid {BEIGE} !important;
    border-radius:24px !important;
    padding:20px !important;
}}

/* Metric label */

[data-testid="stMetricLabel"] {{
    color:{WINE} !important;
    font-weight:600 !important;
    font-size:16px !important;
}}

/* Metric value */

[data-testid="stMetricValue"] {{
    color:{WINE} !important;
    font-size:42px !important;
    font-weight:700 !important;
}}

/* PROGRESS BAR TRACK */

.stProgress > div > div {{
    background:#D7C7B5 !important;
    border-radius:999px !important;
}}

/* PROGRESS BAR FILL */

.stProgress > div > div > div {{
    background:{WINE} !important;
    border-radius:999px !important;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown(
    f"""
    <div class='hero-title'>AI Career Copilot</div>
    <div class='hero-sub'>
    Understand your strengths, identify skill gaps, and design your next step.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- INPUTS ----------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=220,
    placeholder="Paste internship or job description here..."
)

# ---------------- ANALYSIS ----------------

if uploaded_file and job_description:

    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                resume_text += text

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    missing_skills = find_missing_skills(
        resume_skills,
        jd_skills
    )

    recommendations = learning_recommendations(
        missing_skills
    )

    # MATCH SCORE

    if len(jd_skills) > 0:
        match_score = (
            len(set(resume_skills) & set(jd_skills))
            / len(jd_skills)
        ) * 100
    else:
        match_score = 0

    st.markdown("<hr>", unsafe_allow_html=True)

    # SKILLS

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            "<div class='section-title'>Resume Skills</div>",
            unsafe_allow_html=True
        )

        pills = "".join(
            [f"<span class='skill-pill'>{s}</span>"
             for s in resume_skills]
        )

        st.markdown(
            f"<div class='skill-row'>{pills}</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            "<div class='section-title'>Job Description Skills</div>",
            unsafe_allow_html=True
        )

        pills = "".join(
            [f"<span class='skill-pill'>{s}</span>"
             for s in jd_skills]
        )

        st.markdown(
            f"<div class='skill-row'>{pills}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<hr>", unsafe_allow_html=True)

    # MATCH SCORE

    st.markdown(
        "<div class='section-title'>Match Score</div>",
        unsafe_allow_html=True
    )

    st.metric(
        "Compatibility",
        f"{match_score:.1f}%"
    )

    st.progress(match_score / 100)

    st.markdown("<hr>", unsafe_allow_html=True)

    # MISSING + RECOMMENDATIONS

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(
            "<div class='section-title'>Missing Skills</div>",
            unsafe_allow_html=True
        )

        if missing_skills:

            pills = "".join(
                [f"<span class='skill-pill'>{s}</span>"
                 for s in missing_skills]
            )

            st.markdown(
                f"<div class='skill-row'>{pills}</div>",
                unsafe_allow_html=True
            )

        else:
            st.success("Perfect match found.")

    with col4:

        st.markdown(
            "<div class='section-title'>Learning Recommendations</div>",
            unsafe_allow_html=True
        )

        if recommendations:

            for skill, rec in recommendations.items():

                st.markdown(
                    f"""
                    <div style="
                        background:{CARD};
                        border:1px solid {BEIGE};
                        border-radius:20px;
                        padding:16px;
                        margin-bottom:12px;
                    ">
                        <b style="color:{WINE}">
                        {skill.title()}
                        </b><br>
                        {rec}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown("<hr>", unsafe_allow_html=True)

                with st.expander("View Resume Text"):
                    st.write(resume_text)

                with st.expander("View Job Description"):
                    st.write(job_description)
        