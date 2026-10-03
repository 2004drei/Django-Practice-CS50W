from django.shortcuts import render

tasks = ["bla", "ble", "blu"]
# Create your views here.
def index(request):
  return render(request, "tasks/index.html", {
    "tasks" : tasks
  })