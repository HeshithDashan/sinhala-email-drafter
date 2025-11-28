import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Professional Email Drafter", layout="centered")
st.title("📧 Sinhala to Professional English Email")
st.caption("Professional Templates | Free & Simple 🚀")

# Sidebar එකේ නම් ටික ඉල්ලමු
with st.sidebar:
    st.header("📝 ඊමේල් විස්තර")
    sender_name = st.text_input("ඔබේ නම (Your Name):", "Heshith")
    recipient_name = st.text_input("යවන්නේ කාටද (Receiver Name):", "Manager")
    st.info("මෙහි දෙන නම් ඊමේල් එකට ස්වයංක්‍රීයව එකතු වේ.")

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

user_input = st.text_area("විස්තරය සිංහලෙන් ලියන්න:", height=200, placeholder="ඔබේ විස්තරය මෙතන ලියන්න...")

if st.button("Draft Email 📝"):
    if user_input:
        english_reason = translate_text(user_input)
        
        # නම් නැත්නම් පොදු නම් පාවිච්චි කිරීම
        r_name = recipient_name if recipient_name else "Manager"
        s_name = sender_name if sender_name else "[Your Name]"

        if email_type == "Leave Request (නිවාඩු ඉල්ලීම)":
            full_email = f"""Subject: Formal Request for Leave

Dear {r_name},

I am writing to formally request leave from work.

Reason for leave:
{english_reason}

I have taken necessary steps to ensure that my current responsibilities are covered during my absence. I apologize for any inconvenience this may cause.

Best regards,
{s_name}"""
            
        elif email_type == "Sick Leave (අසනීප නිවාඩු)":
            full_email = f"""Subject: Notification of Absence - Sick Leave

Dear {r_name},

Please accept this email as notification that I am unable to attend work today due to health reasons.

Details:
{english_reason}

I plan to rest today to ensure a speedy recovery and hope to resume my duties as soon as possible. I will remain available via email for any urgent matters.

Best regards,
{s_name}"""

        elif email_type == "Work From Home (නිවසේ සිට වැඩ කිරීමට)":
            full_email = f"""Subject: Request to Work from Home

Dear {r_name},

I am writing to request permission to work from home today.

Reason:
{english_reason}

I assure you that I have full access to all necessary tools and internet connectivity to perform my duties effectively.

Thank you for considering my request.

Best regards,
{s_name}"""
            
        elif email_type == "Meeting Request (රැස්වීමක් ඉල්ලීම)":
            full_email = f"""Subject: Request for Meeting - Regarding Important Matter

Dear {r_name},

I am writing to request a meeting to discuss a matter of importance.

Agenda / Context:
{english_reason}

I would appreciate it if we could schedule this at your earliest convenience. Please let me know a time slot that works best for you.

Best regards,
{s_name}"""
        
        elif email_type == "Resignation (රැකියාවෙන් ඉවත් වීම)":
            full_email = f"""Subject: Formal Resignation Letter

Dear {r_name},

Please accept this letter as formal notification that I am resigning from my position.

Reason (Optional):
{english_reason}

I want to thank you for the opportunity to work with this company. I will do my best to ensure a smooth handover of my responsibilities before I leave.

Best regards,
{s_name}"""
            
        elif email_type == "Thank You Note (ස්තුති කිරීම)":
            full_email = f"""Subject: Thank You

Dear {r_name},

I am writing this note to express my sincere gratitude.

Message:
{english_reason}

Thank you once again for your support.

Best regards,
{s_name}"""
            
        else:
            full_email = f"""Subject: Update Regarding Work Matter

Dear {r_name},

I am writing to bring the following to your attention.

Details:
{english_reason}

Thank you for your time and consideration.

Best regards,
{s_name}"""
        
        st.success("Professional Email Draft Ready! ✅")
        st.code(full_email, language='text')
        
    else:
        st.warning("කරුණාකර විස්තරයක් ඇතුලත් කරන්න.")

st.markdown("---")
st.markdown("Made with ❤️ by Heshith_D")