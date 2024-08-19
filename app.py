import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable, TranscriptsDisabled

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Improved prompt for Google Generative AI
prompt = """

You are an expert YouTube video summarizer. Your task is to create a well-structured and engaging summary of the video transcript provided. Please follow these guidelines for the summary:

1. Main Heading: Start with a clear and concise heading that reflects the main topic or theme of the video.

2. Subheadings: Break down the summary into key sections or topics discussed in the video. Each subheading should represent a major point or segment of the video content.

3. Bullet Points:
   - Use simple bullet points for each item.
   - Each bullet point should be on a new line.
   - Ensure the points are clear, concise, and effectively convey the essence of the discussion.

4. Details and Clarity: For each point, provide enough detail to convey the essence of the discussion. Avoid overly technical jargon and use simple language. The goal is to make the summary easily understandable and engaging for a broad audience.

5. Conciseness: Keep the entire summary concise and within 1000 words. Focus on the most important information and avoid unnecessary details.

Make sure the summary is easy to read and enjoyable, with clear and structured points that capture the essence of the video content. Here’s the transcript text to summarize:

[Insert Transcript Text Here]

Please format the summary as follows:

# Main Heading

### Subheading 1

- Bullet point 1  
- Bullet point 2  
- Bullet point 3  

### Subheading 2

- Bullet point 1  
- Bullet point 2  
- Bullet point 3  

### Subheading 3

- Bullet point 1  
- Bullet point 2  
- Bullet point 3  

Instructions for Bullet Points:
- Use simple bullet points (•) for each item.
- Place each bullet point on its own line.
- Ensure there is a newline after each bullet point to ensure proper spacing and readability.

Ensure that the summary is well-organized, with each section clearly delineated for easy reading and comprehension. The use of simple bullet points with proper newline formatting should help highlight the most important information effectively.


"""



# Function to extract transcript details
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except NoTranscriptFound:
        return "Transcript not found for this video."
    except VideoUnavailable:
        return "This video is unavailable."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to generate content using Google Generative AI
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit App UI
st.set_page_config(page_title="YouTube Summarizer", layout="wide")

# Custom CSS styling with Tailwind color palette
st.markdown("""
    <style>
    body {
        background-color: #f5efed; /* Isabelline for the overall background */
        color: #000000; /* Black text color for better readability */
    }
    .main {
        background-color: #ffffff; /* White for main content area */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #000000; /* Black text color for input field */
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #cccccc; /* Light gray border */
    }
    .stTextInput>label {
        color: #000000; /* Black color for input field label */
    }
    .stButton>button {
        background-color: #2292a4; /* Blue (Munsell) for buttons */
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1b7684; /* Darker Blue (Munsell) on hover */
    }
    .summary {
        font-size: 1em;
        line-height: 1.6;
        color: #000000; /* Black text color for summary */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #000000; /* Black color for headings */
    }
    .stMarkdown ul {
        list-style-type: disc;
        padding-left: 20px;
    }
    .stMarkdown ul li {
        margin-bottom: 0.5em;
    }
    .emoji {
        font-size: 1.2em;
        margin-right: 0.5em;
    }
    .stImage>img {
        max-width: 40%; /* Smaller image size */
        height: auto;
        border-radius: 5px;
        border: 2px solid #d96c06; /* Cocoa Brown border for the image */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for additional options
with st.sidebar:
    st.title("YouTube Summarizer")
    st.markdown("Convert YouTube videos into detailed summaries with ease.")

# Main content
st.title("YouTube Video Summary")

# Input field for YouTube link
youtube_link = st.text_input("YouTube Video Link")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to get detailed notes
if st.button("Generate Summary"):
    with st.spinner("Extracting transcript and generating summary..."):
        transcript_text = extract_transcript_details(youtube_link)

        if "error" in transcript_text.lower():
            st.error(transcript_text)
        else:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Summary:")
            # Display the summary with headings, subheadings, and emojis
            st.markdown(f'<div class="summary">{summary}</div>', unsafe_allow_html=True)
