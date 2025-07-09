
# YouTube Audio Summarizer with Gemini AI
#### Video Demo:  [<URL HERE>](https://youtu.be/UZkcMZjIE90)
#### Description:
This Python project allows you to download the audio from any public YouTube video and automatically generate a summarized version of its content using Google's Gemini AI API. The summary is neatly formatted in Markdown, making it ideal for documentation, study materials, or quick reviews of video content such as lectures, podcasts, interviews, and tutorials.

It simplifies the workflow of extracting value from long-form spoken content by converting it into well-structured, readable summaries that can be stored, shared, or published. Whether you're a student, content creator, researcher, or professional, this tool can help save time and make large volumes of content easier to digest.

---

### How It Works

The script performs the following steps in order:

1. **Prompt for Video URL**
   The script prompts the user to enter a YouTube video URL through the terminal. This ensures dynamic input from the user at runtime, rather than hardcoding URLs.

2. **Video Download and Audio Extraction**
   It uses the `pytubefix` library to access the video metadata and extract the audio-only stream. This version minimizes bandwidth usage by avoiding full video download. The audio file is saved locally in a specified directory.

3. **Connect to Google Gemini AI**
   The saved audio file is uploaded to Google's Gemini API using the `google-generativeai` SDK. This is a multimodal API capable of handling audio inputs for content generation.

4. **Summary Generation**
   A predefined prompt written in Portuguese is sent to the model along with the uploaded audio file. The prompt asks for a Markdown-formatted summary of the content. The Gemini model (`gemini-1.5-flash`) interprets the spoken content and creates a clean, readable text output.

5. **Save Summary File**
   The generated summary is saved as a `.md` file inside a designated directory. The file is named using a cleaned-up version of the original video title (special characters are removed to avoid filesystem issues).

---

### Features

- 🎧 Downloads audio from any valid YouTube URL using a simple CLI interface.
- 🧠 Leverages Gemini’s fast and accurate language models for summarization.
- 📝 Outputs summaries in Markdown format, perfect for integration with blogs, wikis, and note-taking apps.
- 💬 Supports prompt customization in natural language (currently set to Portuguese).
- 📂 Saves both raw audio and summaries locally for later access or analysis.
- ✅ Basic error handling for invalid URLs and unavailable videos.
- 🧹 Automatically cleans punctuation from filenames to ensure cross-platform compatibility.

---

### Technologies Used

- **Python 3**
  The core programming language for the script.

- **[pytubefix](https://pypi.org/project/pytubefix/)**
  A maintained fork of `pytube`, which provides a simple API for downloading YouTube video and audio streams. Ideal for building automation tools.

- **[google-generativeai](https://pypi.org/project/google-generativeai/)**
  Google's official SDK for interacting with Gemini models. It provides an easy interface for file uploads, content generation, and model configuration.

- **Google Gemini 1.5 Flash**
  A fast and efficient large language model optimized for real-time applications like summarization, translation, and content generation. It supports multimodal input including audio.

- **Standard Python Libraries**
  Libraries such as `string`, `sys`, and `os` are used for string manipulation, error handling, and file operations.

---

### Installation and Setup

1. **Install Dependencies**

Use `pip` to install the required Python packages:

```bash
pip install pytubefix google-generativeai
```

2. **Set Your Gemini API Key**

To access Google Gemini, you’ll need an API key:

- Go to [Google AI Studio](https://makersuite.google.com/app).
- Create or log into your account.
- Navigate to the **API Access** section and generate an API key.

In the Python script, locate the following line and replace `"YOUR_API_KEY_HERE"` with your actual key, and `"YOUR_PATH_HERE"` make the same to your PATH.

3. **Run the Script**

After configuration, run the script:

```bash
python main.py
```

You will be prompted to enter a YouTube video URL. The script will:

- Download the audio in `.mp4` or `.webm` format.
- Upload the audio to the Gemini API.
- Request a Markdown-formatted summary.
- Save the summary to a `.md` file.

---

### Output

After successful execution, you’ll find:

- **Audio File:** Saved in your configured `downloads_python/` directory.
- **Summary File:** Saved in `resumes/` as `resume_<video_title>.md`

For example:

```text
resume_TheFutureOfAIandWork.md
```

You can open this file with any Markdown editor, or push it directly to your own documentation repo.

---

### Limitations

- The script currently works with **public** YouTube videos only.
- The Gemini API has file size and quota limitations depending on your plan.
- Poor audio quality or strong accents may reduce summarization accuracy.
- The script uses **absolute Windows paths** — you’ll need to modify them for macOS/Linux.
- Currently, there is no user interface. All interactions are done via the terminal.
- Summaries are only as good as the audio content provided.

---

### Future Improvements

- 🔄 Make paths cross-platform with `os.path.join()` and environment variables.
- 🌐 Add automatic language detection and translation options.
- 🧠 Integrate Whisper for full transcription alongside Gemini summaries.
- 💻 Create a Streamlit-based UI for non-technical users.
- ⚙️ Add CLI arguments to control output paths, prompt language, and verbosity.
- 🔁 Add retry mechanisms for unstable network connections or failed uploads.

---

### License

This project is released under the MIT License. You are free to use, modify, and distribute the software with attribution.

---

### Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Bug reports, feature requests, and ideas for improvement are highly appreciated.

---

### Acknowledgments

- Thanks to the developers of `pytubefix` for making YouTube access easy.
- Credit to Google for providing powerful AI tools like Gemini.
- Inspired by the need to simplify learning and content curation workflows.

---

