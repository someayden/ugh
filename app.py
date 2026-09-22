import streamlit as st
import sys
import io
import requests

st.set_page_config(
    page_title="UNCLE BEEZ HUB // CORE",
    page_icon="💔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .reportview-container, .main {
        background: #090d16 !important;
    }
    h1, h2, h3, h4 {
        font-family: 'Courier New', Courier, monospace !important;
        color: #ff3366 !important;
        text-shadow: 0 0 10px rgba(255, 51, 102, 0.4);
    }
    .stButton>button {
        color: #ff3366 !important;
        background-color: #111726 !important;
        border: 1px solid #ff3366 !important;
    }
    .stButton>button:hover {
        background-color: #ff3366 !important;
        color: #090d16 !important;
        box-shadow: 0 0 15px rgba(255, 51, 102, 0.8);
    }
    div[data-baseweb="input"] {
        background-color: #111726 !important;
        border: 1px solid #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💔 UNCLE BEEZ HUB // SUBSYSTEM_V3")
st.caption("🥀 Network Core Status: OPERATIONAL // Terminal Interface Locked")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("💻 COMPILER // Execution Sandbox")
    
    # default user script
    default_code = """import requests
print("Initializing Hub Code Matrix...")
"""
    
    tab_code, tab_docs = st.tabs(["[Source Input]", "[System Docs]"])
    with tab_code:
        user_code = st.text_area("Input Stream:", value=default_code, height=220, label_visibility="collapsed")
    with tab_docs:
        st.markdown("Use this terminal interface to run raw scripts and process data variables.")

    if st.button("RUN ISOLATED CODE BLOCK", use_container_width=True):
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        try:
            exec(user_code)
            sys.stdout = old_stdout
            output = redirected_output.getvalue()
            st.success("Process terminated successfully.")
            st.code(output if output else "[Process exited with no return string]")
        except Exception as e:
            sys.stdout = old_stdout
            st.error("Process execution failure.")
            st.exception(e)

    st.markdown("---")
    
    st.subheader("🎵 AUDIO_STREAM // Global Feed")
    st.write("Stream public radio channels or direct digital audio tracks natively below.")
    
    station_options = {
        "Frequency Alpha (Lo-Fi / Instrumental)": "https://radiomast.io",
        "Frequency Beta (Electronic Mix)": "https://radiomast.io",
        "Custom Direct Stream Link": "CUSTOM"
    }
    
    selected_label = st.selectbox("Select Station Frequency:", list(station_options.keys()))
    stream_url = station_options[selected_label]
    
    if stream_url == "CUSTOM":
        stream_url = st.text_input("Inject Direct Audio Stream URL (.mp3 / .ogg / Icecast stream):", value="")
        
    if stream_url:
        try:
            st.audio(stream_url, format="audio/mp3", loop=True)
            st.caption("Active stream pipeline connected. Press play above to monitor output. 😭")
        except Exception as audio_err:
            st.error(f"Pipeline connectivity drop: {audio_err}")

with col2:
    st.subheader("🤖 AI_COGNITION // Dialogue Array")
    
    with st.expander("🔑 Authentication Matrix Keys", expanded=False):
        api_key = st.text_input("Gemini Engine Key Token:", type="password")

    chat_container = st.container(height=450, border=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Inject logical query..."):
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        if not api_key:
            st.error("Authentication missing: Token validation failed. 🥀")
        else:
            with chat_container:
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    url = f"https://googleapis.com{api_key}"
                    headers = {'Content-Type': 'application/json'}
                    payload = {"contents": [{"parts": [{"text": prompt}]}]}
                    
                    try:
                        response = requests.post(url, json=payload, headers=headers)
                        if response.status_code == 200:
                            ai_response = response.json()['candidates']['content']['parts']['text']
                            message_placeholder.markdown(ai_response)
                            st.session_state.messages.append({"role": "assistant", "content": ai_response})
                        else:
                            st.error(f"Cognition node rejected package: {response.text} 🥀")
                    except Exception as e:
                        st.error(f"Pipeline sync error: {e}")
