# 📄 AI PDF Resume Analyzer

Upload a PDF resume and instantly get AI-powered suggestions to improve it for a specific job description. Built using Streamlit and Hugging Face Transformers.

---

## 🚀 Features

- 📤 Upload your resume (PDF)
- 💼 Paste a job description
- 🤖 Get 3 AI-generated resume improvement suggestions
- ⚡ Uses Google's `flan-t5-small` model (fast & free)
- 🧠 Smart comparison between resume and job description

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- PyPDF2 (PDF reader)

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/pdf-resume-analyzer.git
cd pdf-resume-analyzer

# Optional: Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📌 Example Prompt

```
Compare the resume and job description.
Suggest 3 improvements to better match the job.

Resume:
[PDF Text Extracted]

Job Description:
[User input]
```

---

## 📸 Demo

![image](https://github.com/user-attachments/assets/8101ba27-fc0c-4b5b-8e9d-7f28968301e5)


---


## 👨‍💻 Author

Built with ❤️ by [Vishal Vastava](https://github.com/VishalVastava)
