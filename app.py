import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

st.set_page_config(page_title="Professional Email Drafter", page_icon="✉️", layout="centered")

st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .success-box {
        padding: 15px;
        background-color: #e8f5e9;
        color: #2e7d32;
        border-radius: 10px;
        border: 1px solid #c8e6c9;
        margin-bottom: 20px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

if 'generated_email' not in st.session_state:
    st.session_state.generated_email = ""
if 'generated_subject' not in st.session_state:
    st.session_state.generated_subject = ""

with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("---")
    sender_name = st.text_input("👤 Your Name:", "Heshith")
    recipient_name = st.text_input("🧑‍💼 Receiver Name:", "Manager")
    
    st.markdown("---")
    if st.button("🗑️ Clear All"):
        st.session_state.generated_email = ""
        st.session_state.generated_subject = ""
        st.rerun()

st.markdown('<div class="main-title">📧 Professional Email Drafter</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Sinhala to English | Professional Templates | Editable</div>', unsafe_allow_html=True)

def translate_text(text):
    try:
        translator = GoogleTranslator(source='sinhala', target='english')
        return translator.translate(text)
    except:
        return text

email_type = st.selectbox(
    "📌 Select Email Type:",
    [
        "General (සාමාන්‍ය)", 
        "Leave Request (නිවාඩු ඉල්ලීම)", 
        "Sick Leave (අසනීප නිවාඩු)", 
        "Work From Home (නිවසේ සිට වැඩ කිරීමට)",
        "Meeting Request (රැස්වීමක් ඉල්ලීම)",
        "Resignation (රැකියාවෙන් ඉවත් වීම)", 
        "Thank You Note (ස්තුති කිරීම)"
    ]
)

user_input = st.text_area("✍️ Describe in Sinhala:", height=150, placeholder="Example: මට හෙට එන්න වෙන්නේ නෑ...")

if st.button("✨ Draft Email Now", type="primary"):
    if user_input:
        with st.spinner("Writing email..."):
            english_reason = translate_text(user_input)
            
            r_name = recipient_name if recipient_name else "Manager"
            s_name = sender_name if sender_name else "[Your Name]"
            
            if email_type == "Leave Request (නිවාඩු ඉල්ලීම)":
                st.session_state.generated_subject = "Formal Request for Leave"
                st.session_state.generated_email = f"Dear {r_name},\n\nI am writing to formally request leave from work.\n\nReason for leave:\n{english_reason}\n\nI have taken necessary steps to ensure that my current responsibilities are covered during my absence. I apologize for any inconvenience this may cause.\n\nBest regards,\n{s_name}"
            
            elif email_type == "Sick Leave (අසනීප නිවාඩු)":
                st.session_state.generated_subject = "Notification of Absence - Sick Leave"
                st.session_state.generated_email = f"Dear {r_name},\n\nPlease accept this email as notification that I am unable to attend work today due to health reasons.\n\nDetails:\n{english_reason}\n\nI plan to rest today to ensure a speedy recovery and hope to resume my duties as soon as possible. I will remain available via email for any urgent matters.\n\nBest regards,\n{s_name}"

            elif email_type == "Work From Home (නිවසේ සිට වැඩ කිරීමට)":
                st.session_state.generated_subject = "Request to Work from Home"
                st.session_state.generated_email = f"Dear {r_name},\n\nI am writing to request permission to work from home today.\n\nReason:\n{english_reason}\n\nI assure you that I have full access to all necessary tools and internet connectivity to perform my duties effectively.\n\nThank you for considering my request.\n\nBest regards,\n{s_name}"
                
            elif email_type == "Meeting Request (රැස්වීමක් ඉල්ලීම)":
                st.session_state.generated_subject = "Request for Meeting - Regarding Important Matter"
                st.session_state.generated_email = f"Dear {r_name},\n\nI am writing to request a meeting to discuss a matter of importance.\n\nAgenda / Context:\n{english_reason}\n\nI would appreciate it if we could schedule this at your earliest convenience. Please let me know a time slot that works best for you.\n\nBest regards,\n{s_name}"
            
            elif email_type == "Resignation (රැකියාවෙන් ඉවත් වීම)":
                st.session_state.generated_subject = "Formal Resignation Letter"
                st.session_state.generated_email = f"Dear {r_name},\n\nPlease accept this letter as formal notification that I am resigning from my position.\n\nReason (Optional):\n{english_reason}\n\nI want to thank you for the opportunity to work with this company. I will do my best to ensure a smooth handover of my responsibilities before I leave.\n\nBest regards,\n{s_name}"
                
            elif email_type == "Thank You Note (ස්තුති කිරීම)":
                st.session_state.generated_subject = "Thank You"
                st.session_state.generated_email = f"Dear {r_name},\n\nI am writing this note to express my sincere gratitude.\n\nMessage:\n{english_reason}\n\nThank you once again for your support.\n\nBest regards,\n{s_name}"
                
            else:
                st.session_state.generated_subject = "Update Regarding Work Matter"
                st.session_state.generated_email = f"Dear {r_name},\n\nI am writing to bring the following to your attention.\n\nDetails:\n{english_reason}\n\nThank you for your time and consideration.\n\nBest regards,\n{s_name}"

if st.session_state.generated_email:
    st.markdown('<div class="success-box">✅ Draft Generated Successfully! You can edit it below.</div>', unsafe_allow_html=True)
    
    final_subject = st.text_input("📝 Subject Line:", value=st.session_state.generated_subject)
    
    final_body = st.text_area("📄 Email Body (Editable):", value=st.session_state.generated_email, height=350)
    
    full_final_text = f"Subject: {final_subject}\n\n{final_body}"
    
    # මෙන්න මෙතන විතරයි මාරු කලේ. (Rocket -> Tools)
    st.markdown("### 🛠️ Actions")
    
    col1, col2 = st.columns(2)
    
    safe_subject = urllib.parse.quote(final_subject)
    safe_body = urllib.parse.quote(final_body)
    mailto_link = f"mailto:?subject={safe_subject}&body={safe_body}"

    with col1:
        st.markdown(f'''
            <a href="{mailto_link}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #4CAF50; color: white; padding: 15px; text-align: center; border-radius: 8px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    📤 Open in Email App
                </div>
            </a>
            ''', unsafe_allow_html=True)
        
    with col2:
        st.download_button(
            label="💾 Download Text File",
            data=full_final_text,
            file_name="email_draft.txt",
            mime="text/plain"
        )

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Made with ❤️ by Heshith_D</div>", unsafe_allow_html=True)