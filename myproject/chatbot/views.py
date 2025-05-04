from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

intents = ["emergency"]

@csrf_exempt  # Needed to test POSTs without CSRF token
def handle_intent(request, intent):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    message = data.get("message")
    if not message:
        return JsonResponse({"error": "Message is required"}, status=400)

    if intent == "emergency":
        return JsonResponse(emergency_intent(message), safe=False)
    else:
        return JsonResponse({"error": f"Intent '{intent}' not supported."}, status=404)


# --- Response Helpers ---

def text_response(text, enable_input=True):
    return {
        "sender": "ai",
        "text": text,
        "props": "enable_input" if enable_input else "disable_input"
    }

def buttons_response(text, actions, enable_input=False):
    return {
        "sender": "ai",
        "props": "disable_input" if not enable_input else "enable_input",
        "button_response": {
            "text": text,
            "actions": [{"id": action["id"], "title": action["title"]} for action in actions]
        }
    }

# --- Emergency Intent Logic ---

def emergency_intent(message):
    msg = message.lower()
    if msg in ["thanks", "thank you", "asante", "cool"]:
        return text_response("Wow, I'm glad to have helped you! Have a nice day")

    elif msg in ["hello", "hi", "habari"]:
        actions = [
            {"id": 1, "title": "Call Emergency Services"},
            {"id": 2, "title": "Need Urgent Medical Advice"},
            {"id": 3, "title": "Find Nearby Hospital"},
            {"id": 4, "title": "Locate Nearby Pharmacy"}
        ]
        return buttons_response("Hello, how can we help you?", actions)

    elif msg == "call emergency services":
        return text_response("Dialing emergency services. For Tanzania, dial 112.", enable_input=False)

    elif msg == "need urgent medical advice":
        actions = [
            {"id": 1, "title": "Speak with a Medical Officer"},
            {"id": 2, "title": "Get First Aid Advice"}
        ]
        return buttons_response("Would you like to speak with a medical officer or get first aid advice?", actions)

    elif msg == "find nearby hospital":
        return text_response(
            "Nearby hospitals:\n- Muhimbili National Hospital\n- Aga Khan Hospital\n- Regency Medical Center",
            enable_input=False
        )

    elif msg == "locate nearby pharmacy":
        return text_response(
            "Nearby pharmacies:\n- Shelys Pharmacy\n- Alpha Pharmacy\n- Duka la Dawa Muhimu",
            enable_input=False
        )

    else:
        return text_response("Sorry, we didn't understand your request. Please clarify.")

