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

	return render(request, 'home.html', {'data':api_urls})

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return render(request, "home.html",{"tasks":serializer.data})



@api_view(['GET', 'POST'])
def taskDetail(request):
	if request.method == 'GET':
		tasks = Task.objects.all()
		serializer = TaskSerializer(tasks, many=True)
		return render(request, 'home.html', {'detail':serializer.data})
	if request.method == 'POST':
		pk = request.data.get('pk')
		print(type(pk))
		tasks = Task.objects.get(id=pk)
		serializer = TaskSerializer(tasks, many=False)
		return render(request, 'home.html', {'id':tasks.id, 'title':tasks.title, 'status':tasks.completed, 'pk':pk })


@api_view(['POST', 'GET'])
def taskCreate(request):
	is_updat = True
	if request.method == 'POST':
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return render(request, 'home.html', {'crea':'Data creation successful', 'is_update': is_updat})
		else:
	         return render(request, 'home.html', {'crea':'Data creation unsuccessful', 'is_update': is_updat})
	if request.method == 'GET':
	     return render(request, 'home.html', {'is_update': is_updat})

@api_view(['POST',"GET"])
def taskUpdate(request):
	try:
		if request.method == 'POST':
			pk = request.data.get('pk')
			task = Task.objects.get(id=pk)
			serializer = TaskSerializer(instance=task, data=request.data)

			if serializer.is_valid():
				serializer.save()
				return render(request, 'home.html', {'updat':'Data Updation successful'})
			else:
				return render(request, 'home.html', {'updat':'Data Updation successful'})
		if request.method == 'GET':
			return render(request, 'home.html')
	except:
		return render(request, 'home.html',{'updat': 'Please check your entry'})



@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


