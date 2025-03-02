import speech_recognition as sr
from precise_runner import PreciseEngine, PreciseRunner

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_sphinx(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("PocketSphinx could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from PocketSphinx; {e}")

def detected_callback():
    print("Wake word detected!")
    recognize_speech()

if __name__ == "__main__":
    # Path to your Mycroft Precise model
    model_path = "path_to_your_model/hey_mycroft.pb"

    # Initialize the Precise engine
    engine = PreciseEngine('precise-engine', model_path)
    runner = PreciseRunner(engine, on_activation=detected_callback)

    print("Listening for wake word... Press Ctrl+C to exit")
    runner.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        runner.stop()
