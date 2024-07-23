from django.shortcuts import render

from .models import Todo
def home(request):
	result = Todo.objects.all()
	# # print(result[0].task) # type -> str
	# # # print(result[0].created_at)  This is my task to impress someone
	# for object in result:
	# 	print(object.task)  # data print 
	# 	# print(type(object.task))  # 3 bar str 


	return render(request, "home.html")


def todo(request):
	todos = Todo.objects.all()
	
	parameters = {
		"todos": todos,
		# "name": "This is Raghav"
		# "total_todo": len(todos) # another method their is no need to display and write we write simple in html file {{ todos.count }}
	}

	return render(request, "todo.html", parameters)




def add_todo(request):
	return render(request, "add_todo.html")

'''
Django models m hr class ek class k kuch methods mujhe phle m milue hue hn
jse ki ?

1. objects.all()

Todo.objects.all()

'''

# result = Todo.objects.all()
# print(result)  #on termianal <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>]>
# print(result[0].task)

'''
todo ek class h
Todo m m objects create ka pr rha hu
Todo m objects ko modify bhi kia ja skta hai

Todo ek Mutable data rkha ha?

Todo.objects.all() la return data type kya hogab

Most important:

Dictionary m key aur value kse likhte hai ye pta hona chaiye 

data = {
	key: value
}
'''
