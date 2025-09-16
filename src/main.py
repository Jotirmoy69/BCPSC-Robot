# main.py
from utils import is_bangla, conversation_memory
from speech_io import listen, speak
from ai_conversation import load_model, get_local_response
from hardware import move_forward, move_backward, turn_left, turn_right, cleanup
from vision import person_detection  # auto-starts thread
from ai_apis import call_external_apis

# Load models
vectorizer_en, model_en = load_model("../models/conversation_model_en.joblib")
vectorizer_bn, model_bn = load_model("../models/conversation_model_bn.joblib")

def detect_action(text):
    text_lower = text.lower()
    if any(word in text_lower for word in ["forward", "go"]):
        return move_forward
    if any(word in text_lower for word in ["back", "backward"]):
        return move_backward
    if "left" in text_lower:
        return turn_left
    if "right" in text_lower:
        return turn_right
    if any(word in text for word in ["সামনে", "গো", "আগুন"]):
        return move_forward
    if any(word in text for word in ["পিছনে", "ব্যাক"]):
        return move_backward
    if "বামে" in text:
        return turn_left
    if "ডানে" in text:
        return turn_right
    return None

def main():
    speak("Hello! I am Blue, your bilingual robot assistant.")
    try:
        while True:
            query = listen()
            if not query:
                continue

            action = detect_action(query)
            if action:
                action()
                response = "Action executed."
                conversation_memory.append({"user": query, "bot": response})
                speak(response)
                continue

            lang = "bn" if is_bangla(query) else "en"
            if lang == "en":
                response = get_local_response(query, vectorizer_en, model_en)
            else:
                response = get_local_response(query, vectorizer_bn, model_bn)

            if not response:
                response = call_external_apis(query, lang)

            if not response:
                response = "I am not sure about that." if lang=="en" else "আমি এটা বুঝতে পারিনি।"

            conversation_memory.append({"user": query, "bot": response})
            speak(response)
    except KeyboardInterrupt:
        speak("Shutting down...")
    finally:
        cleanup()

if __name__ == "__main__":
    main()
