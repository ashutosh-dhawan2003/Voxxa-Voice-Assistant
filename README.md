
# Voxxa Voice Assistant

Voxxa is a Python-based voice assistant designed to perform tasks such as web browsing, fetching information from Wikipedia, and sending emails, all through voice commands. It uses powerful libraries for text-to-speech and speech recognition to create a smooth and interactive experience.

## Features

- **Voice Recognition**: Uses SpeechRecognition to process spoken commands.
- **Text-to-Speech**: Converts text responses to spoken words using pyttsx3.
- **Web Browsing**: Automates web browsing tasks through voice commands.
- **Wikipedia Search**: Fetches information from Wikipedia based on voice queries.
- **Email Automation**: Sends emails through voice commands using smtplib.
- **Time-Based Greetings**: Greets the user based on the time of day (morning, afternoon, evening).

## Technologies Used

- **Python**: Primary programming language.
- **pyttsx3**: For converting text to speech.
- **SpeechRecognition**: For recognizing and processing voice input.
- **Wikipedia API**: Fetches information from Wikipedia.
- **Webbrowser**: Opens and interacts with web browsers via voice commands.
- **smtplib**: Sends emails through voice input.
- **Datetime**: To manage time-based greetings.

## Requirements

To run the Voxxa Voice Assistant, you need the following dependencies installed:

```bash
pip install pyttsx3 SpeechRecognition wikipedia smtplib
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/ashutosh-dhawan2003/voxxa-voice-assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd voxxa-voice-assistant
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the project:

   ```bash
   python voxxa.py
   ```

5. Voxxa will greet you and be ready for voice commands. Start speaking, and the assistant will listen for tasks like browsing the web, searching Wikipedia, or sending emails.

## Usage

### Available Commands:

- **"Open Google"**: Opens Google in your default browser.
- **"Search Wikipedia for [topic]"**: Fetches a summary from Wikipedia about the specified topic.
- **"Send email"**: Automates the process of sending an email through voice commands.
- **"What time is it?"**: Tells the current time.
- **"Good morning/afternoon/evening"**: Greets based on the time of day.

### Example Interaction:

- **User**: "Open Google"
- **Voxxa**: "Opening Google..."

- **User**: "Search Wikipedia for Python programming"
- **Voxxa**: "According to Wikipedia, Python is a high-level, interpreted programming language..."

## Customization

You can extend Voxxa by adding new voice commands and functionalities. Modify the `take()` function to include more options and integrate other APIs or custom scripts.

## Contributing

If you'd like to contribute to Voxxa, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to modify.
