import ollama

def iniciar_chat(usuario):
    # Rol del chatbot
    historial = [{
        'role': 'system',
        'content': 'Eres un robot social, das respuestas cortas y siempre buscas mantener la conversación haciendo preguntas para interactuar'
    }]

    ultima_respuesta = ""  # Variable para almacenar la última respuesta del bot

    historial.append({'role': 'user', 'content': usuario})

    # Limitar historial
    historial = historial[:1] + historial[-20:]

    # Llama al modelo
    respuesta = ollama.chat(model='llama3:8b', messages=historial)

    ultima_respuesta = respuesta['message']['content'].strip()
    print(f"Bot: {ultima_respuesta}")

    historial.append({'role': 'assistant', 'content': ultima_respuesta})

    

if __name__ == "__main__":
    while True:
        usuario = input("Tú: ")

        # Verificar si quiere salir antes de llamar a iniciar_chat
        if usuario.lower() in ["salir", "exit", "adios", "chao"]:
            print("Bot: ¡Hasta luego!")
            break

        iniciar_chat(usuario)
