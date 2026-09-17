import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HackBridge — Enterprise Hackathon Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for Streamlit container
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #4F46E5;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 9999px;
        background-color: #EEF2FF;
        color: #4F46E5;
        margin-right: 0.5rem;
    }
    .card {
        padding: 1.25rem;
        border-radius: 0.75rem;
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }
    iframe {
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🎓 HackBridge")
    st.caption("Pilot Tenant: MITT Thandavapura | v2.0")
    st.markdown("---")
    nav_choice = st.radio(
        "Navigation",
        ["🚀 Live Application", "📋 Panel Presentation Guide", "📖 Complete Documentation", "🏛️ System Architecture"],
        index=0
    )
    st.markdown("---")
    st.markdown("#### 🔒 Security & Privacy")
    st.caption("✓ No credentials committed to git\n✓ Supabase RLS policies enforced\n✓ Multi-tenant isolated schemas")

base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, "static")
index_html_path = os.path.join(static_dir, "index.html")

if nav_choice == "🚀 Live Application":
    st.markdown('<div class="main-header">HackBridge Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Interactive Multi-Tenant Hackathon & Recruitment SaaS Platform</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown('<span class="badge">React 18</span><span class="badge">Vite</span><span class="badge">Tailwind CSS</span><span class="badge">Supabase</span><span class="badge">Phase 1-12 Live</span>', unsafe_allow_html=True)
    with col2:
        st.markdown("[🔗 Open Full-Screen App](/app/static/index.html)")
    with col3:
        st.caption("Status: All 4 Stakeholder Portals Active")

    st.markdown("---")

    # Render embedded application using Streamlit static serving
    if os.path.exists(index_html_path):
        # Embed via iframe pointing to the static app endpoint
        components.iframe(src="/app/static/index.html", height=820, scrolling=True)
    else:
        st.warning("Production build not detected in static/ directory. Please run `npm run build && python scripts/prepare_streamlit.py`.")

elif nav_choice == "📋 Panel Presentation Guide":
    st.markdown('<div class="main-header">Live Panel Presentation Script</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Guided walkthrough for academic evaluators & industry judges</div>', unsafe_allow_html=True)

    st.markdown("""
    ### 🎯 Demonstration Flow (MITT NIH 2026)

    #### 1. Student Portal (`/student`)
    - **My Team & Invite Code (`/student/team`)**:
      - Inspect **NeuralByte Innovations** and unique invite code `MITT-9X4K`.
      - Review 4 member profiles with skills and avatars.
    - **Problem Statements (`/student/problems`)**:
      - 5 industrial challenges sponsored by Bosch, Zerodha, Philips, Infosys, and AgriTech.
    - **Project Submissions & AI Score (`/student/submissions`)**:
      - Full project submission with GitHub repo, Loom video, slide deck, and architecture.
      - Automated **AI Pre-Screening Scorecard: 9.6 / 10**.
    - **Verified Talent Profile (`/student/portfolio`)**:
      - 9.4 CGPA, Grand Champion badge, interactive verified skills radar.
    - **Career Offers Desk (`/student/offers`)**:
      - Real recruiter outreach offers from Bosch (₹12-15 LPA CTC) and Zerodha (₹60k/mo).

    #### 2. Evaluator Desk (`/evaluator`)
    - **Assigned Submissions Queue (`/evaluator/assignments`)**:
      - Review status tracking: Completed, Pending, Recused.
    - **Rubric Scoring Workspace (`/evaluator/score`)**:
      - Double-blind masked dossier (left) and 4-criterion sliders (right).
      - Live weighted score computation, recommendation voting (`Advance`), and COI recusal.
      - **Review Entry Switcher** dropdown in the header to jump between all 4 assigned entries.

    #### 3. Company Portal (`/company`)
    - **Candidate Talent Pool (`/company/talent-pool`)**:
      - Filter candidates by skill tags (*Python, YOLOv8, eBPF*), CGPA, and awards.
      - 1-Click **Express Hiring Interest** modal to send job/internship offers.

    #### 4. Admin Console (`/admin`)
    - **AI Pre-Screening Console (`/admin/prescreening`)**: Automated heuristic triage and batch runner.
    - **Results & Judging Deliberation (`/admin/results`)**: Score aggregation and winner declaration.
    - **Institutional Audit Log (`/admin/audit`)**: Tamper-evident compliance trail.

    #### 5. Live Leaderboard (`/leaderboard`)
    - Championship podium display (🥇 1st: NeuralByte, 🥈 2nd: QuantEdge, 🥉 3rd: AgriSense).
    """)

elif nav_choice == "📖 Complete Documentation":
    st.markdown('<div class="main-header">System Documentation</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Complete technical specifications, ERD, and user manuals</div>', unsafe_allow_html=True)

    doc_path = os.path.join(base_dir, "DOCUMENTATION.md")
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            doc_content = f.read()
        st.markdown(doc_content)
    else:
        st.info("DOCUMENTATION.md not found in project root.")

elif nav_choice == "🏛️ System Architecture":
    st.markdown('<div class="main-header">Architecture & Multi-Tenancy</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">White-label multi-tenant design & database security</div>', unsafe_allow_html=True)

    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
        ### Multi-Tenant Isolation Model
        - **Registry:** `public.tenants` with slug, custom domain, and dynamic theme colors.
        - **Zero Trust:** Client can never supply or fabricate `tenant_id`. Resolution is strictly server-side.
        - **Row-Level Security (RLS):** All 14 tables enforce strict tenant checks via authenticated JWT claims.
        - **Protected Fields:** Trigger `enforce_profile_field_protection()` protects `role`, `tenant_id`, and `is_active` from client-side modification.
        """)
    with colB:
        st.markdown("""
        ### 7 Hierarchical RBAC Roles
        1. `super_admin`: Global multi-tenant system administrator.
        2. `college_admin`: Institutional tenant hackathon manager.
        3. `committee_member`: Academic review board member.
        4. `evaluator`: Industry judge with double-blind scoring permissions.
        5. `company_rep`: Corporate partner sponsoring challenges & scouting.
        6. `mentor`: Academic guide supporting student teams.
        7. `student`: Innovator building and submitting solutions.
        """)

    st.markdown("---")
    st.markdown("""
    ### Data Privacy & Security Checklist
    - ✅ **`.env` Ignored:** Real database connection strings and passwords are never tracked in Git.
    - ✅ **Publishable Anon Key:** Client communicates using standard publishable keys protected by PostgreSQL RLS.
    - ✅ **Double-Blind Anonymization:** Student team names and members are masked in the evaluator scoring API.
    - ✅ **Append-Only Audit Logs:** Tamper-evident logging for all scoring, approval, and hiring operations.
    """)
