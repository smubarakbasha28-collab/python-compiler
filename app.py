import streamlit as st
import io
import contextlib
import traceback
import multiprocessing
import time
from streamlit_ace import st_ace

st.set_page_config(page_title="Python Online Compiler", layout="wide")

# ----------------------------
# CENTERED TITLE
# ----------------------------
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0px;'>
        🧠 Python Online Compiler
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; color: gray; margin-top: 0px; margin-bottom: 20px;'>
        Secure browser-based Python IDE
    </p>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# STREAMLIT FONT + ACE OVERRIDE
# ----------------------------
st.markdown(
    """
    <style>
    /* Streamlit default font */
    html, body, [class*="css"] {
        font-family: "Source Sans Pro", sans-serif;
    }

    /* Ace Editor styling */
    .ace_editor, .ace_text-input, .ace_content {
        font-family: "Source Sans Pro", sans-serif !important;
        font-size: 20px !important;
        line-height: 1.6 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# THEME (system-based)
# ----------------------------
theme = st.get_option("theme.base")

if theme == "dark":
    ace_theme = "monokai"
else:
    ace_theme = "github"

# ----------------------------
# SESSION STATE
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# SAFE EXECUTION FUNCTION
# ----------------------------
def run_code(code, q):
    stdout = io.StringIO()
    stderr = io.StringIO()

    safe_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
        }
    }

    try:
        compiled = compile(code, "user_code", "exec")

        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exec(compiled, safe_globals)

        q.put((stdout.getvalue(), stderr.getvalue(), None))

    except Exception:
        q.put(("", "Error", traceback.format_exc()))

# ----------------------------
# LAYOUT
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Editor")

    # ----------------------------
    # ACE EDITOR
    # ----------------------------
    code = st_ace(
        placeholder="Write Python code here...",
        language="python",
        theme=ace_theme,
        height=500,
        keybinding="vscode",
        font_size=22,
        tab_size=4,
        show_gutter=True,
        show_print_margin=False,
        wrap=False,
        auto_update=True
    )

    col_run, col_download = st.columns(2)

    with col_run:
        run = st.button("▶ Run Code", use_container_width=True)

    with col_download:
        st.download_button(
            "⬇ Download .py",
            data=code or "",
            file_name="script.py",
            mime="text/plain",
            use_container_width=True
        )

    # ----------------------------
    # RUN CODE
    # ----------------------------
    if run:
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=run_code, args=(code, q))
        p.start()
        p.join(3)

        if p.is_alive():
            p.terminate()
            st.error("⛔ Timeout: Code took too long")
        else:
            out, err, trace = q.get()

            st.session_state.history.append({
                "code": code,
                "output": out,
                "error": err,
                "trace": trace,
                "time": time.strftime("%H:%M:%S")
            })

            st.success("Execution complete")

# ----------------------------
# OUTPUT PANEL
# ----------------------------
with col2:
    st.subheader("📟 Output")

    if st.session_state.history:
        last = st.session_state.history[-1]

        if last["output"]:
            st.markdown("### Output")
            st.code(last["output"])

        if last["error"]:
            st.markdown("### Error")
            st.code(last["error"])

        if last["trace"]:
            st.markdown("### Traceback")
            st.code(last["trace"])

# ----------------------------
# SIDEBAR HISTORY
# ----------------------------
st.sidebar.title("📜 History")

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared")

for item in reversed(st.session_state.history[-10:]):
    with st.sidebar.expander(f"{item['time']}"):
        st.code(item["code"])
        if item["output"]:
            st.text(item["output"])

st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; color: gray; font-size: 13px;'>
        ⚠ For interview and learning purposes only — not intended for production use
    </p>
    """,
    unsafe_allow_html=True
)
=======
import streamlit as st
import io
import contextlib
import traceback
import multiprocessing
import time
from streamlit_ace import st_ace

st.set_page_config(page_title="Python Online Compiler", layout="wide")

# ----------------------------
# CENTERED TITLE
# ----------------------------
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0px;'>
        🧠 Python Online Compiler
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; color: gray; margin-top: 0px; margin-bottom: 20px;'>
        Secure browser-based Python IDE
    </p>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# STREAMLIT FONT + ACE OVERRIDE
# ----------------------------
st.markdown(
    """
    <style>
    /* Streamlit default font */
    html, body, [class*="css"] {
        font-family: "Source Sans Pro", sans-serif;
    }

    /* Ace Editor styling */
    .ace_editor, .ace_text-input, .ace_content {
        font-family: "Source Sans Pro", sans-serif !important;
        font-size: 20px !important;
        line-height: 1.6 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# THEME (system-based)
# ----------------------------
theme = st.get_option("theme.base")

if theme == "dark":
    ace_theme = "monokai"
else:
    ace_theme = "github"

# ----------------------------
# SESSION STATE
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# SAFE EXECUTION FUNCTION
# ----------------------------
def run_code(code, q):
    stdout = io.StringIO()
    stderr = io.StringIO()

    safe_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
        }
    }

    try:
        compiled = compile(code, "user_code", "exec")

        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exec(compiled, safe_globals)

        q.put((stdout.getvalue(), stderr.getvalue(), None))

    except Exception:
        q.put(("", "Error", traceback.format_exc()))

# ----------------------------
# LAYOUT
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Editor")

    # ----------------------------
    # ACE EDITOR
    # ----------------------------
    code = st_ace(
        placeholder="Write Python code here...",
        language="python",
        theme=ace_theme,
        height=500,
        keybinding="vscode",
        font_size=22,
        tab_size=4,
        show_gutter=True,
        show_print_margin=False,
        wrap=False,
        auto_update=True
    )

    col_run, col_download = st.columns(2)

    with col_run:
        run = st.button("▶ Run Code", use_container_width=True)

    with col_download:
        st.download_button(
            "⬇ Download .py",
            data=code or "",
            file_name="script.py",
            mime="text/plain",
            use_container_width=True
        )

    # ----------------------------
    # RUN CODE
    # ----------------------------
    if run:
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=run_code, args=(code, q))
        p.start()
        p.join(3)

        if p.is_alive():
            p.terminate()
            st.error("⛔ Timeout: Code took too long")
        else:
            out, err, trace = q.get()

            st.session_state.history.append({
                "code": code,
                "output": out,
                "error": err,
                "trace": trace,
                "time": time.strftime("%H:%M:%S")
            })

            st.success("Execution complete")

# ----------------------------
# OUTPUT PANEL
# ----------------------------
with col2:
    st.subheader("📟 Output")

    if st.session_state.history:
        last = st.session_state.history[-1]

        if last["output"]:
            st.markdown("### Output")
            st.code(last["output"])

        if last["error"]:
            st.markdown("### Error")
            st.code(last["error"])

        if last["trace"]:
            st.markdown("### Traceback")
            st.code(last["trace"])

# ----------------------------
# SIDEBAR HISTORY
# ----------------------------
st.sidebar.title("📜 History")

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared")

for item in reversed(st.session_state.history[-10:]):
    with st.sidebar.expander(f"{item['time']}"):
        st.code(item["code"])
        if item["output"]:
            st.text(item["output"])

st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; color: gray; font-size: 13px;'>
        ⚠ For interview and learning purposes only — not intended for production use
    </p>
    """,
    unsafe_allow_html=True
)
