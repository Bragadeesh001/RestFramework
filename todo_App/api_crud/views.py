from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.shortcuts import render, get_object_or_404

from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return render(request,'list.html', {'tas':serializer.data})

# @api_view(['GET','POST'])
# def taskDetail(request):
# 	pk=None
# 	if request.method=='POST':
# 		pk = request.POST.get('option', None)
# 		print(pk)
# 	if pk is not None:
# 		task = get_object_or_404(Task, id=pk)
# 		tasks = Task.objects.get(id=pk)
# 		serializer = TaskSerializer(tasks, many=False)
# 	else:
# 		tasks = Task.objects.all()
# 		serializer = TaskSerializer(tasks, many=True)
# 	print(pk)
# 	return render(request,'list.html', {'det':serializer.data, 'pk': pk})

@api_view(['GET', 'POST'])
def taskDetail(request):
    if request.method == 'POST':
        selected_option = request.POST.get('option', None)
        if selected_option is not None:
            task = get_object_or_404(Task, id=selected_option)
            serializer = TaskSerializer(task)
            return render(request, 'list.html', {'task_detail': Task.objects.all(), 'pk': selected_option, 'task_detail': task})
        else:
            return Response({"error": "No option selected."}, status=400)
    else:
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return render(request, 'list.html', {'task_detail': serializer.data})

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

@api_view(['GET', 'POST'])
def taskUpdate(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Update the task with new data
        task.title = title
        task.description = description
        task.save()

    return render(request, 'list.html', {'det': Task.objects.all(), 'pk': None})


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



######### Front end  ###########

# @api_view(['GET'])
# def product_list(request):
#     products = Task.objects.all()
#     serializer = TaskSerializer(Task, many=True)
#     return Response(serializer.data)



def home(request):
    return render(request, 'list.html')  # Render the list.html template


