import os,subprocess
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse





# Create your views here.
def index_view(request):

    with os.scandir('python-files/') as entries:
        list_file = [entry.name for entry in entries]

    context = {'list_files': list_file,

               }
    return render(request, 'index.html', context)


def run_file_view(request):
    if request.method == 'GET' and request.is_ajax():
        clicked_file = request.GET['file']
        path = os.path.join("python-files", clicked_file)
        out_file = clicked_file.replace(".py",".txt")
        shell_run = f"python {path}"
        xd = subprocess.Popen(shell_run.split(" "), stderr=subprocess.STDOUT,shell=True,stdout=subprocess.PIPE)
        output= ""
        while True:
            line = xd.stdout.readline().decode('utf-8')
            if not line:
                break
            print(line)
            output += line
        print("--------------")
        print(output)
        data = { "output_file": output}
        return JsonResponse(data)
    return HttpResponse("ok")
