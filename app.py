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

user_input = st.text_area("විස්තරය සිංහලෙන් ලියන්න:", height=100, placeholder="උදා: මට හෙට එන්න වෙන්නේ නෑ...")

if st.button("Draft Email 📝"):
    if user_input:
        english_reason = translate_text(user_input)
        
        email_body = ""
        subject = ""
        
        if email_type == "Leave Request (නිවාඩු ඉල්ලීම)":
            subject = "Subject: Request for Casual Leave"
            email_body = f"""
            Dear Manager,

            I am writing to request leave. 
            Reason: {english_reason}

            I ensure that my pending tasks will be managed before I leave.

            Best regards,
            [Your Name]
            """
            
        elif email_type == "Sick Leave (අසනීප නිවාඩු)":
            subject = "Subject: Sick Leave Application"
            email_body = f"""
            Dear Manager,

            I am writing to inform you that I am unable to attend work today due to illness.
            Details: {english_reason}

            I will be available on email for any urgent matters.

            Best regards,
            [Your Name]
            """
            
        elif email_type == "Meeting Request (රැස්වීමක් ඉල්ලීම)":
            subject = "Subject: Meeting Request"
            email_body = f"""
            Dear Team,

            I would like to request a meeting to discuss the following:
            {english_reason}

            Please let me know a convenient time for you.

            Best regards,
            [Your Name]
            """
            
        else:
            subject = "Subject: Update Regarding [Topic]"
            email_body = f"""
            Dear [Name],

            {english_reason}

            Best regards,
            [Your Name]
            """
        
        st.success("Email Draft Ready! ✅")
        st.text(subject)
        st.code(email_body, language='text')
        
    else:
        st.warning("කරුණාකර විස්තරයක් ඇතුලත් කරන්න.")

st.markdown("---")
st.markdown("Made with ❤️ by Heshith_D")