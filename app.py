import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

st.set_page_config(page_title="Professional Email Drafter", layout="centered")
st.title("📧 Sinhala to Professional English Email")
st.caption("Professional Templates | Editable Drafts ✏️")

if 'generated_email' not in st.session_state:
    st.session_state.generated_email = ""
if 'generated_subject' not in st.session_state:
    st.session_state.generated_subject = ""

with st.sidebar:
    st.header("📝 ඊමේල් විස්තර")
    sender_name = st.text_input("ඔබේ නම (Your Name):", "Heshith")
    recipient_name = st.text_input("යවන්නේ කාටද (Receiver Name):", "Manager")
    
    if st.button("Clear All 🔄"):
        st.session_state.generated_email = ""
        st.session_state.generated_subject = ""
        st.rerun()

def translate_text(text):
    try:
        translator = GoogleTranslator(source='sinhala', target='english')
        return translator.translate(text)
    except:
        return text

email_type = st.selectbox(
    "ඔබට අවශ්‍ය ඊමේල් වර්ගය තෝරන්න:",
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

user_input = st.text_area("විස්තරය සිංහලෙන් ලියන්න:", height=150, placeholder="උදා: මට හෙට එන්න වෙන්නේ නෑ...")

if st.button("Draft Email 📝", type="primary"):
    if user_input:
        english_reason = translate_text(user_input)
        
        r_name = recipient_name if recipient_name else "Manager"
        s_name = sender_name if sender_name else "[Your Name]"
        
        if email_type == "Leave Request (නිවාඩු ඉල්ලීම)":
            st.session_state.generated_subject = "Formal Request for Leave"
            st.session_state.generated_email = f"""Dear {r_name},

I am writing to formally request leave from work.

Reason for leave:
{english_reason}

I have taken necessary steps to ensure that my current responsibilities are covered during my absence. I apologize for any inconvenience this may cause.

Best regards,
{s_name}"""
            
        elif email_type == "Sick Leave (අසනීප නිවාඩු)":
            st.session_state.generated_subject = "Notification of Absence - Sick Leave"
            st.session_state.generated_email = f"""Dear {r_name},

Please accept this email as notification that I am unable to attend work today due to health reasons.

Details:
{english_reason}

I plan to rest today to ensure a speedy recovery and hope to resume my duties as soon as possible. I will remain available via email for any urgent matters.

Best regards,
{s_name}"""

        elif email_type == "Work From Home (නිවසේ සිට වැඩ කිරීමට)":
            st.session_state.generated_subject = "Request to Work from Home"
            st.session_state.generated_email = f"""Dear {r_name},

I am writing to request permission to work from home today.

Reason:
{english_reason}

I assure you that I have full access to all necessary tools and internet connectivity to perform my duties effectively.

Thank you for considering my request.

Best regards,
{s_name}"""
            
        elif email_type == "Meeting Request (රැස්වීමක් ඉල්ලීම)":
            st.session_state.generated_subject = "Request for Meeting - Regarding Important Matter"
            st.session_state.generated_email = f"""Dear {r_name},

I am writing to request a meeting to discuss a matter of importance.

Agenda / Context:
{english_reason}

I would appreciate it if we could schedule this at your earliest convenience. Please let me know a time slot that works best for you.

Best regards,
{s_name}"""
        
        elif email_type == "Resignation (රැකියාවෙන් ඉවත් වීම)":
            st.session_state.generated_subject = "Formal Resignation Letter"
            st.session_state.generated_email = f"""Dear {r_name},

Please accept this letter as formal notification that I am resigning from my position.

Reason (Optional):
{english_reason}

I want to thank you for the opportunity to work with this company. I will do my best to ensure a smooth handover of my responsibilities before I leave.

Best regards,
{s_name}"""
            
        elif email_type == "Thank You Note (ස්තුති කිරීම)":
            st.session_state.generated_subject = "Thank You"
            st.session_state.generated_email = f"""Dear {r_name},

I am writing this note to express my sincere gratitude.

Message:
{english_reason}

Thank you once again for your support.

Best regards,
{s_name}"""
            
        else:
            st.session_state.generated_subject = "Update Regarding Work Matter"
            st.session_state.generated_email = f"""Dear {r_name},

I am writing to bring the following to your attention.

Details:
{english_reason}

Thank you for your time and consideration.

Best regards,
{s_name}"""

if st.session_state.generated_email:
    st.success("Draft Generated! You can edit it below (ඔබට අවශ්‍ය නම් පහතින් වෙනස්කම් කරන්න):")
    
    final_subject = st.text_input("Subject Line:", value=st.session_state.generated_subject)
    
    final_body = st.text_area("Email Body (Editable):", value=st.session_state.generated_email, height=350)
    
    full_final_text = f"Subject: {final_subject}\n\n{final_body}"
    
    st.markdown("### 📨 Preview & Actions")
    
    col1, col2 = st.columns(2)
    
    safe_subject = urllib.parse.quote(final_subject)
    safe_body = urllib.parse.quote(final_body)
    mailto_link = f"mailto:?subject={safe_subject}&body={safe_body}"

    with col1:
        st.markdown(f'''
            <a href="{mailto_link}" target="_blank">
                <button style="width: 100%; background-color: #FF4B4B; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    🚀 Open in Email App
                </button>
            </a>
            ''', unsafe_allow_html=True)
        
    with col2:
        st.download_button(
            label="💾 Download Text File",
            data=full_final_text,
            file_name="email_draft.txt",
            mime="text/plain"
        )
    
    with st.expander("Click here to View/Copy Final Text"):
        st.code(full_final_text, language='text')

st.markdown("---")
st.markdown("Made with ❤️ by Heshith_D")