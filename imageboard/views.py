from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from imageboard.models import Board, Post


def index(request):
    boards = Board.objects.order_by('address')
    return render(request, 'index.html', {'boards': boards})


def board(request, board_address):
    board = Board.objects.get(address=board_address)
    context = {
      'board': board,
      'op_posts': board.get_op_posts(),
    }
    return render(request, 'board.html', context)


def thread(request, board_address, thread_id):
    board = Board.objects.get(address=board_address)
    op_post = Post.objects.get(id=thread_id, board=board, op_ref=None)
    posts = Post.objects.filter(board=board, op_ref=op_post)

    context = {
      'board': board,
      'op_post': op_post,
      'posts': posts
    }
    return render(request, 'thread.html', context)


def add_post(request, board_address):
    # Находим тред, в котором пользователь пытается оставить пост
    try:
        board = Board.objects.get(address=board_address)
        thread_id = int(request.POST['parent'])
        op_post = Post.objects.get(id=thread_id, board=board, op_ref=None)
    except:
        raise Http404('Статья не найдена')

    new_post = Post()
    new_post.board = board
    new_post.op_ref = op_post
    new_post.body = request.POST['text']
    new_post.subject = request.POST['subject']
    new_post.save()

    kwargs = {'board_address': board_address, 'thread_id': request.POST['parent']}
    url = reverse('thread', kwargs=kwargs)
    return HttpResponseRedirect(url)
