# **🎥 YouTube Video Summarizer**

This repository contains a Python-based web application that extracts transcripts from YouTube videos and generates concise summaries using Google’s Generative AI. The project uses `streamlit` for the web interface, making it easy for users to interact with the tool.

---

## **🚀 Features**

- **Video Transcript Extraction**: Extracts transcripts from any YouTube video using the `youtube_transcript_api`.
- **AI-Powered Summarization**: Utilizes Google’s Generative AI to generate structured summaries, including headings, subheadings, and bullet points.
- **Streamlit Web Interface**: Provides a simple and user-friendly interface for inputting YouTube video links and receiving summaries.
- **Customization Options**: Allows users to tailor the summary format to their needs.

---

## **🎥 Video Demo**

[![Watch the video](https://img.youtube.com/vi/aY2jtJR813U/maxresdefault.jpg)](https://youtu.be/aY2jtJR813U)

Click on the image above to watch the demo.

---

## **🛠️ Installation**

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/DSabarish/yt-summariser.git
    cd yt-summariser
    ```

2. **Install Required Packages:**

    Ensure you have Python installed. Then, install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables:**

    Create a `.env` file in the root directory of the project and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY = "Your-Google-API-Key"
    ```

---

## **📋 Usage**

1. **Run the Streamlit App:**

    Start the web application using the following command:

    ```bash
    streamlit run app.py
    ```

2. **Input the YouTube Video Link:**

    Paste the YouTube video link into the input field and click "Generate Summary."

3. **View the Summary:**

    The application will extract the transcript, summarize it using Google’s Generative AI, and display the summary on the screen.

---

## **📁 Project Structure**

- **`app.py`**: Main application script that contains the Streamlit interface and functions to handle transcript extraction and summarization.
- **`requirements.txt`**: List of required Python packages.
