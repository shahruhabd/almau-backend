from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import TodoListSerializer, TodoSerializer


@api_view(['GET'])
def get_todo_lists(request):
    todo_lists = TodoList.objects.all()
    serializer = TodoListSerializer(todo_lists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_todo_list(request):
    serializer = TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_todo_list(request, id):
    try:
        todo_list = TodoList.objects.get(id=id)
    except TodoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoListSerializer(todo_list)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_todo_list(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
    except TodoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoListSerializer(todo_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo_list(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
    except TodoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todo_list.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_todo_list_todos(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
    except TodoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todos = Todo.objects.filter(todo_list=todo_list)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_todo_list_todo(request, pk):
    try:
        todo_list = TodoList.objects.get(pk=pk)
    except TodoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(todo_list=todo_list)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(['PUT'])
def update_todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todo_lists.html', {'todo_lists': todo_lists})


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {'todo_list': todo_list}
    return render(request, 'todo_list_detail.html', context)



