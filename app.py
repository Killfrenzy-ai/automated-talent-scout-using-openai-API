import streamlit as st
from dotenv import load_dotenv
import os
from utils import generate_questions
from prompts import greeting_message, exit_keywords

# Load environment variables
load_dotenv()

# Streamlit config
st.set_page_config(page_title="TalentScout AI Assistant", page_icon="🤖")
st.title("🤖 TalentScout AI Hiring Assistant")

# Session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "info_collected" not in st.session_state:
    st.session_state.info_collected = False

if "tech_stack" not in st.session_state:
    st.session_state.tech_stack = ""

# Check for exit keywords
def is_exit(text):
    return any(word in text.lower() for word in exit_keywords)

# Greeting
if not st.session_state.conversation:
    st.session_state.conversation.append(("bot", greeting_message))

# Display conversation
for sender, msg in st.session_state.conversation:
    if sender == "bot":
        st.markdown(f"**🤖 TalentScout:** {msg}")
    else:
        st.markdown(f"**🧑 You:** {msg}")

# Input box
user_input = st.text_input("Your response", key="user_input")

if st.button("Send") and user_input:
    st.session_state.conversation.append(("user", user_input))

    if is_exit(user_input):
        st.session_state.conversation.append(("bot", "Thank you! We'll be in touch soon. 👋"))
        st.rerun()

    elif not st.session_state.info_collected:
        st.session_state.info_collected = True
        st.session_state.conversation.append(("bot", "Great! Now, please list your tech stack (languages, frameworks, tools):"))

    elif st.session_state.tech_stack == "":
        st.session_state.tech_stack = user_input

        try:
            questions = generate_questions(st.session_state.tech_stack)

            if questions and len(questions) > 0:
                bot_response = "Here are some technical questions based on your tech stack:\n\n"
                bot_response += "\n".join([f"🔹 {q}" for q in questions])
            else:
                bot_response = "⚠️ I couldn't generate questions. Please try a more detailed tech stack."

        except Exception as e:
            bot_response = f"⚠️ Error generating questions: {e}"

        st.session_state.conversation.append(("bot", bot_response))
        st.session_state.conversation.append(("bot", "That's all for now. Thank you for sharing your information!"))

    else:
        st.session_state.conversation.append(("bot", "Thanks for your input."))

    st.rerun()
