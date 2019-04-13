from django.http import HttpResponse
from django.shortcuts import render  #use to pass html file path in http respose
import operator

def homepage(request):
	#return HttpResponse("<h1>This is homepage<h1>")
	#return render(request,'home.html')
	return render(request,'home.html',{ 'name':'Hi, i am Ravi Yadav' }) #we can also pass dictionary

#def contact(request):
	#return HttpResponse("<h1>Contact Us</h1>")

def count(request):
	data = request.GET['fulltextarea']
	data_list = data.split()
	length= len(data_list)
	#print(data)

	dictionary={}

	for word in data_list:
		if word in dictionary:
			#increase by 1
			dictionary[word] += 1

		else:
			#add to dictionary and set 1
			dictionary[word] = 1

	sorted_list = sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True)

	return render(request,'count.html',{'fulltext':data,'length':length,'data_dictionary':sorted_list})

def aboutme(request):
	return render(request,'about.html')