**🚀 Scam Detector**
This project is a simple web application that classifies text as scam or not scam using zero-shot classification with the facebook/bart-large-mnli model from Hugging Face Transformers.

**Built with:**

Python

Transformers

Gradio

**✨ Features**
✅ Paste any message (like an email or SMS)
✅ The model predicts whether it's scam or not scam
✅ Shows prediction confidence

**🛠️ Installation**
Clone the repository

Install dependencies

pip install -r requirements.txt
🧾 Requirements
Your requirements.txt should look like:
transformers
torch
gradio

**🚦 Usage**
Run the app:

python app.py


**📂 File Structure**

app.py             # Main Gradio app
requirements.txt   # Dependencies
README.md          # Project documentation

**✨ Example**
Input:
Congratulations! You have won $5000. Click here to claim your prize.
Output:
Prediction: scam (confidence: 0.98)

**Demo** 
Live app:https://huggingface.co/spaces/Abisha2005/scam-detector

**⚡ License**
MIT License.
