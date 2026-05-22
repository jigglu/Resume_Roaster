# 🔥 Resume Roaster

Upload your resume and get brutally honest feedback from a ruthless AI recruiter.

## Live App
[Click here to roast your resume](https://resumeroaster-dxke4dhr4wpb434tausgzt.streamlit.app/)

## What it does
- Upload any PDF resume
- AI tears it apart — weak action verbs, vague bullet points, missing metrics
- Tells you exactly what to fix

## ✨ Features

* **Brutally Honest AI:** Powered by Groq and LangChain, the AI is specifically prompted to roast weak action verbs, lack of metrics, and corporate jargon.
* **PDF Processing:** Seamlessly uploads and extracts text from your PDF resumes using `PyPDFLoader`.
* **Smart Validation:** Automatically detects and rejects PDFs that contain no readable text (e.g., image-only PDFs).
* **Anti-Spam / Rate Limiting:** Built-in IP caching ensures that users can only roast one resume per IP address, protecting your free Groq API limits from abuse.
* **Lightning Fast:** Utilizes Groq's LPU inference engine for near-instant roasts.

  
## Run locally
```bash
pip install -r requirements.txt
python main.py roast your_resume.pdf
```

## Built with
- Python, LangChain, Groq, Streamlit
