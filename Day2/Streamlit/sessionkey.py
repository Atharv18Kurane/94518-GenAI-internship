import streamlit as st

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Settings")
    options = ["Upper", "Lower", "Toggle"]
    case = st.selectbox("Select Case", options)
    count = st.slider("Max Messages", min_value=2, max_value=10, value=6, step=1)

    st.subheader("Current Config")
    st.json({"mode": case, "count": count})

# Clear chat history
if st.button("Clear History"):
    st.session_state.messages = []

st.title("My Chatbot")

# Chat input
msg = st.chat_input("Say Anything")

if msg:
    outmsg = msg
    if case == "Upper":
        outmsg = msg.upper()
    elif case == "Lower":
        outmsg = msg.lower()
    elif case == "Toggle":
        outmsg = msg.swapcase()

    # Store messages
    st.session_state.messages.append(msg)
    st.session_state.messages.append(outmsg)

    # Limit message history
    st.session_state.messages = st.session_state.messages[-count * 2:]

# Display chat
for idx, message in enumerate(st.session_state.messages):
    role = "human" if idx % 2 == 0 else "ai"
    with st.chat_message(role):
        st.write(message)
