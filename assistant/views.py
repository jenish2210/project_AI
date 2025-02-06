from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
from django.shortcuts import render
from .utils.speech_to_text import recognize_speech
from .utils.text_to_speech import speak_text
from .utils.task_manager import add_task, list_tasks, clear_tasks
from .utils.emergency_alert import send_emergency_alert

def home(request):
    return render(request, "assistant/index.html")

def add_task_view(request):
    if request.method == "POST":
        task = request.POST.get("task", "").strip()
        if task:
            response = add_task(task)
            speak_text(response)
            return JsonResponse({"message": response})
    return JsonResponse({"message": "No task provided."})

def list_tasks_view(request):
    tasks = list_tasks()
    return JsonResponse({"tasks": tasks})

def emergency_alert_view(request):
    send_emergency_alert()
    speak_text("Emergency alert sent.")
    return JsonResponse({"message": "Emergency alert sent!"})
