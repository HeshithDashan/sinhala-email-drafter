import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Sinhala Email Drafter", layout="centered")

def translate_and_draft(text):
    try:
        translator = GoogleTranslator(source='sinhala', target='english')
        english_text = translator.translate(text)
    except Exception as e:
        return f"Error: Translation failed. {e}"
    
    draft = f"""
    Subject: [Subject Here]

    Dear [Name],

    {english_text}

    Best regards,
    [Your Name]
    """
    return draft

st.title("📧 Sinhala to English Email Drafter")
st.write("සිංහලෙන් idea එක type කරන්න. අපි එක English Email එකක් කරමු.")

user_input = st.text_area("ඔබේ පණිවිඩය (සිංහලෙන්):", height=150, placeholder="උදා: මට හෙට එන්න වෙන්නේ නෑ. මගේ කාර් එක කැඩිලා.")

if st.button("Generate Email Draft"):
    if user_input:
        with st.spinner('Translating & Drafting...'):
            email_draft = translate_and_draft(user_input)
            
            st.success("Draft එක ලෑස්තියි! 👇")
            st.code(email_draft, language='text')
            st.caption("මේක Copy කරගෙන ඔයාගේ Email එකට දාගන්න.")
    else:
        st.warning("කරුණාකර යමක් type කරන්න.")

st.markdown("---")
st.markdown("Made with ❤️ by Heshith_D")