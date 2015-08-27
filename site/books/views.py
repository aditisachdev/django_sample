from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import *
from django.views.decorators.csrf import csrf_protect
import json
import datetime
from django.http import Http404

# Create your views here.
@login_required
def index(request):
	books = Book.objects.all()
	o = ' '.join([bk.title for bk in books])
	template = loader.get_template('books/index.html')
	context = RequestContext(request, {'books':books})
	return render(request,'books/index.html',context)

@login_required
def detail(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
		reviews = book.review_set.all()
	except Book.DoesNotExist:
		raise Http404("Book with id %s does not exist" % book_id)
	
	d = RequestContext(request, {'book':book})
	return render(request, 'books/detail.html', d)

@login_required
def add_review(request):
	curr_user = request.user
	review = request.POST['comment']
	book_id = request.POST['book_id']
	u = User.objects.get(pk=curr_user.id)

	try:
		book = Book.objects.get(pk=book_id)
	except Book.DoesNotExist:
		return HttpResponse(json.dumps({'msg':'Invalid Request'}))

	rev = Review(book=book, text=review, user=u)
	try:
		rev.save()
	except e:
		return HttpResponse(json.dumps({'msg':'Request failed. Please try again later.'}))
		
	return render(request, 'books/detail.html', RequestContext(request,{'book_id':book_id, 'user':u}))

@login_required
def add_book(request):
	curr_user = request.user
	title = request.POST['book_name']
	author = request.POST['author_name']
	publisher = request.POST['pub_name']
	description = request.POST['desc']
	genre = request.POST['genre']
	pub_date = request.POST['pub_date']
	ISBN = request.POST['isbn']
	edition = request.POST['edition']

	if pub_date != '':
		pub_date=datetime.datetime.strptime(pub_date.replace('/',''), "%m%d%Y").date()
	else:
		pub_date = None
	try:
		book = Book(title=title, author=author, publisher=publisher, description=description, genre=genre, pub_date=pub_date, 
					ISBN=ISBN, edition=edition)
		book.save()
	except e:
		return HttpResponse(json.dumps({'msg':'Request failed. Please try again later.'}))

	return HttpResponse(json.dumps({'msg':'Success'}))	
