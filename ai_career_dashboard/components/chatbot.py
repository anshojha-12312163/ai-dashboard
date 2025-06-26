print("chatbot.py loaded")
import streamlit as st
import openai

# Set your real OpenAI key
api_key = "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"
client = openai.OpenAI(api_key=api_key)

def run():
    st.subheader("💬 Career Chat Assistant")
    st.markdown("Ask anything about careers, skills, courses, or study strategies.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with st.form("chat_form"):
        user_input = st.text_input("🔍 Ask your question")
        submit = st.form_submit_button("Send")

        if submit and user_input:
            with st.spinner("Thinking..."):
                st.session_state.chat_history.append(("You", user_input))

                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a friendly and helpful career guidance assistant."},
                            {"role": "user", "content": user_input}
                        ]
                    )
                    reply = response.choices[0].message.content
                    st.session_state.chat_history.append(("Bot", reply))

                except Exception as e:
                    st.error(f"Error: {e}")
                    st.session_state.chat_history.append(("Bot", "Sorry, I couldn't process that right now."))

    # Display chat history
    for sender, msg in reversed(st.session_state.chat_history):
        if sender == "You":
            st.markdown(f"🧑‍🎓 You:** {msg}")
        else:
            st.markdown(f"🤖 Bot:** {msg}")