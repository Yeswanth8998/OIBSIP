import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()


def say(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()


def main():
    say("Hello, I am your voice assistant. How can I help you?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print("You said: " + command)

            if "hello" in command.lower():
                say("Hello! How can I help you?")

            elif "what is the time" in command.lower() or "tell me the time" in command.lower():
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                say(f"The time is {current_time}")

            elif "what is the date" in command.lower() or "tell me the date" in command.lower():
                current_date = datetime.date.today().strftime("%B %d, %Y")
                say(f"Today's date is {current_date}")

            elif "search for" in command.lower():
                query = command.lower().replace("search for", "")
                query = query.strip()
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open(search_url)
                say(f"Searching the web for {query}")

            elif "exit" in command.lower() or "goodbye" in command.lower():
                say("Bye! Have a nice day.")
                break

            else:
                say("I'm sorry, I don't understand what you said. Please say it again.")

        except sr.UnknownValueError:
            say("I don't understand what you said. Please say it again.")
        except sr.RequestError as e:
            say(f"Error {e}")


if __name__ == "__main__":
    main()
