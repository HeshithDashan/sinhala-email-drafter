import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Simple Email Drafter", layout="centered")
st.title("📧 Sinhala to English Email Helper")
st.caption("No AI Keys Required | Free & Simple 🚀")

def translate_text(text):
    try:
        translator = GoogleTranslator(source='sinhala', target='english')
        return translator.translate(text)
    except:
        return text

email_type = st.selectbox(
    "ඔබට අවශ්‍ය ඊමේල් වර්ගය තෝරන්න:",
    ["General (සාමාන්‍ය)", "Leave Request (නිවාඩු ඉල්ලීම)", "Sick Leave (අසනීප නිවාඩු)", "Meeting Request (රැස්වීමක් ඉල්ලීම)"]
)

user_input = st.text_area("විස්තරය සිංහලෙන් ලියන්න:", height=300, placeholder="ඔබේ විස්තරය මෙතන ලියන්න...")

if st.button("Draft Email 📝"):
    if user_input:
        english_reason = translate_text(user_input)
        
        if email_type == "Leave Request (නිවාඩු ඉල්ලීම)":
            full_email = f"""Subject: Request for Casual Leave

Dear Manager,

I am writing to request leave.

Reason:
{english_reason}

I ensure that my pending tasks will be managed before I leave.

Best regards,
[Your Name]"""
            
        elif email_type == "Sick Leave (අසනීප නිවාඩු)":
            full_email = f"""Subject: Sick Leave Application

Dear Manager,

I am writing to inform you that I am unable to attend work today due to illness.

Details:
{english_reason}

I will be available on email for any urgent matters.

Best regards,
[Your Name]"""
            
        elif email_type == "Meeting Request (රැස්වීමක් ඉල්ලීම)":
            full_email = f"""Subject: Meeting Request

Dear Team,

I would like to request a meeting to discuss the following matter:

{english_reason}

Please let me know a convenient time for you.

Best regards,
[Your Name]"""
            
        else:
            full_email = f"""Subject: Update Regarding [Topic]

Dear [Name],

{english_reason}

Best regards,
[Your Name]"""
        
        st.success("Email Draft Ready! ✅")
        st.code(full_email, language='text')
        
    else:
        st.warning("කරුණාකර විස්තරයක් ඇතුලත් කරන්න.")

st.markdown("---")
st.markdown("Made with ❤️ by Heshith_D")