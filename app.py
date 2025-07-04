import gradio as gr
from transformers import pipeline
import os
# Load the classifier
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Define the prediction function
def detect_scam(text):
    labels = ["scam", "not scam"]
    result = classifier(text, labels)
    # Return nicely formatted string
    label = result["labels"][0]
    score = result["scores"][0]
    return f"Prediction: {label} (confidence: {score:.2f})"

# Build Gradio interface
demo = gr.Interface(
    fn=detect_scam,
    inputs=gr.Textbox(lines=4, placeholder="Paste the message here..."),
    outputs="text",
    title="Scam Detector",
    description="Classifies text as scam or not scam using zero-shot classification."
)

# Launch



port = int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0", server_port=port)
