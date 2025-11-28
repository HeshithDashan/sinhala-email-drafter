import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Professional Email Drafter", layout="centered")
st.title("📧 Sinhala to Professional English Email")
st.caption("Professional Templates | Free & Simple 🚀")

def translate_text(text):
    try:
        translator = GoogleTranslator(source='sinhala', target='english')
        return translator.translate(text)
    except:
        return text

email_type = st.selectbox(
    "ඔබට අවශ්‍ය ඊමේල් වර්ගය තෝරන්න:",
    ["General (සාමාන්‍ය)", "Leave Request (නිවාඩු ඉල්ලීම)", "Sick Leave (අසනීප නිවාඩු)", "Meeting Request (රැස්වීමක් ඉල්ලීම)", "Work From Home (නිවසේ සිට වැඩ කිරීමට)"]
)

user_input = st.text_area("විස්තරය සිංහලෙන් ලියන්න:", height=300, placeholder="ඔබේ විස්තරය මෙතන ලියන්න...")

if st.button("Draft Email 📝"):
    if user_input:
        english_reason = translate_text(user_input)
        
        if email_type == "Leave Request (නිවාඩු ඉල්ලීම)":
            full_email = f"""Subject: Formal Request for Leave

Dear Manager,

I am writing to formally request leave from work.

Reason for leave:
{english_reason}

I have taken necessary steps to ensure that my current responsibilities are covered during my absence. I apologize for any inconvenience this may cause and appreciate your understanding.

Best regards,
[Your Name]"""
            
        elif email_type == "Sick Leave (අසනීප නිවාඩු)":
            full_email = f"""Subject: Notification of Absence - Sick Leave

Dear Manager,

Please accept this email as notification that I am unable to attend work today due to health reasons.

Details:
{english_reason}

I plan to rest today to ensure a speedy recovery and hope to resume my duties as soon as possible. I will remain available via email for any urgent matters.

Best regards,
[Your Name]"""

        elif email_type == "Work From Home (නිවසේ සිට වැඩ කිරීමට)":
            full_email = f"""Subject: Request to Work from Home

Dear Manager,

I am writing to request permission to work from home today.

Reason:
{english_reason}

I assure you that I have full access to all necessary tools and internet connectivity to perform my duties effectively without any disruption.

Thank you for considering my request.

Best regards,
[Your Name]"""
            
        elif email_type == "Meeting Request (රැස්වීමක් ඉල්ලීම)":
            full_email = f"""Subject: Request for Meeting - Regarding Important Matter

Dear Team,

I am writing to request a meeting to discuss a matter of importance.

Agenda / Context:
{english_reason}

I would appreciate it if we could schedule this at your earliest convenience. Please let me know a time slot that works best for you.

Best regards,
[Your Name]"""
            
        else:
            full_email = f"""Subject: Update Regarding Work Matter

Dear [Name],

I am writing to bring the following to your attention.

Details:
{english_reason}

Thank you for your time and consideration regarding this matter.

Best regards,
[Your Name]"""
        
        st.success("Professional Email Draft Ready! ✅")
        st.code(full_email, language='text')
        
    else:
        st.warning("කරුණාකර විස්තරයක් ඇතුලත් කරන්න.")

st.markdown("---")
st.markdown("Made with ❤️ by Heshith_D")