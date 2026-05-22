import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import tempfile

st.set_page_config(page_title="Resume Roaster 🔥", page_icon="🔥")
st.title("🔥 Resume Roaster")
st.subheader("Upload your resume. Prepare to cry.")

uploaded_file = st.file_uploader("Drop your resume here", type="pdf")

if uploaded_file:
    if st.button("Roast me 💀"):
        with st.spinner("Heating up the roaster..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
            resume_text = "\n".join([doc.page_content for doc in docs])

            if not resume_text.strip():
                st.error("This PDF has no readable text. Is it just a giant image?")
                st.stop()

            llm = ChatGroq(
                model="llama-3.1-8b-instant",
                api_key=st.secrets["GROQ_API_KEY"]
            )

            prompt = PromptTemplate.from_template(
                "You are the most ruthless, cynical, and brutally honest tech recruiter on Earth. "
                "You have zero patience for fluff, buzzwords, and vague accomplishments. "
                "Tear this resume apart. Highlight weak action verbs, vague bullet points, "
                "lack of hard metrics, and anything trash-worthy. "
                "Be sarcastic and brutal but technically valid so they know what to fix.\n\n"
                "Resume:\n<resume>\n{resume_text}\n</resume>\n\nRoast:"
            )

            chain = prompt | llm | StrOutputParser()
            response = chain.invoke({"resume_text": resume_text})

        st.markdown("---")
        st.subheader("💀 The Roast")
        st.write(response)
