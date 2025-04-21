import streamlit as st
from transformers import pipeline
import PyPDF2
import io

# Page configuration
st.set_page_config(page_title="PDF Resume Analyzer", page_icon="📄")

st.title("📄 AI PDF Resume Analyzer")
st.write("Upload your resume (PDF) and match it against a job description using GenAI.")

# PDF upload
uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type="pdf")

# Job description input
job_desc = st.text_area("💼 Paste Job Description Here", height=250)

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

generator = load_model()

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text() + "\n"
    return extracted_text

# Analyze button
if st.button("🔍 Analyze Resume"):
    if uploaded_file and job_desc:
        with st.spinner("Reading PDF and Analyzing..."):
            pdf_text = extract_text_from_pdf(uploaded_file)

            prompt = (
                f"Compare the resume and job description. "
                f"Suggest 3 improvements to better match the job.\n\n"
                f"Resume:\n{pdf_text}\n\nJob Description:\n{job_desc}"
            )

            result = generator(prompt, max_length=300, clean_up_tokenization_spaces=True)[0]["generated_text"]

            st.success("✅ Suggestions Ready!")
            st.markdown("### 💡 Suggestions:")
            st.write(result)
    else:
        st.warning("⚠️ Please upload a resume and enter a job description.")

