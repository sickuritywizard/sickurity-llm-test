import subprocess

def execute_something(request):
    ip = request.POST.get("ip")
    subprocess.run("ping "+ ip)