import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 130)

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def responder(texto_usuario):
    texto_usuario = texto_usuario.lower()
    if "hey" in texto_usuario or "hi" in texto_usuario:
        return "Hi, how are you?"
    elif "how are you" in texto_usuario:
        return "I'm great, thank you!"
    elif "what's your name" in texto_usuario or "what is your name" in texto_usuario:
        return "I'm your voice assistant."
    elif "thank you" in texto_usuario:
        return "You're welcome."
    elif "goodbye" in texto_usuario or "bye" in texto_usuario:
        return "Goodbye!"
    else:
        return "I didn't understand that."

def escuchar_y_responder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language='en-US')
        print(f" You said: {texto}")

        respuesta = responder(texto)  # Esta línea siempre dentro del try
        print(f" Response: {respuesta}")
        hablar(respuesta)

        if "goodbye" in texto.lower() or "bye" in texto.lower():
            return False

    except sr.UnknownValueError:
        print(" I couldn't understand you.")
    except sr.RequestError:
        print(" There was a connection issue.")
    except Exception as e:
        print(f" Unexpected error: {e}")

    return True

# Bucle principal
while True:
    continuar = escuchar_y_responder()
    if not continuar:
        break
