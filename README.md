# Audio/Video Transcription App

This project creates a web application for transcribing audio and video files using OpenAI's Whisper API. It is built with Streamlit, allowing users to upload files and receive transcriptions.

## Project Aim

The aim of this project is to provide an easy-to-use interface for transcribing various audio and video file formats. It splits larger audio files into chunks to manage size constraints and delivers the transcription in both on-screen and downloadable text formats.

## Installation

1. **Clone the Repository**

   ```bash
   git clone [repository URL]
   cd [repository directory]
   ```

2. **Install Dependencies**

   This project requires Python 3. Ensure it is installed on your system. Then install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` should include `streamlit`, `python-dotenv`, `requests`, `pydub`, and any other necessary packages.

3. **Set Up Environment Variables**

   You need to set up the Whisper API key. Create a `.env` file in the project root and add the following line:

   ```plaintext
   WHISPER_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

1. **Start the Streamlit App**

   Run the following command in the terminal:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of the main Python file, if different.

2. **Using the App**

   - The app will open in your default web browser.
   - Upload an audio or video file (.wav, .mp3, .mp4, .avi, .mkv, .flv, .m4a).
   - The app processes the file and displays the transcription on the screen.
   - You can download the transcription as a text file.

## Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change or add.

## License

[MIT](https://choosealicense.com/licenses/mit/)


