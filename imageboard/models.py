from django.db import models


class Board(models.Model):
    address     = models.CharField(max_length=32, primary_key=True)
    title       = models.CharField(max_length=100)
    description = models.TextField(max_length=9000, blank=True, default='')

    def __str__(self):
        return f'/{self.address}/ - {self.title}'

    def start_thread(self, post):
        post.board = self
        post.save()

    def get_op_posts(self):
        posts = Post.objects.filter(board=self, op_ref=None)
        return posts


class Post(models.Model):
    id        = models.BigAutoField(primary_key=True)
    board     = models.ForeignKey(Board, on_delete=models.CASCADE)
    op_ref    = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    options   = models.CharField(max_length=100,  blank=True, default='')
    name      = models.CharField(max_length=50,   blank=True, default='')
    tripcodes = models.CharField(max_length=50,   blank=True, default='')
    subject   = models.CharField(max_length=100,  blank=True, default='')
    body      = models.TextField(max_length=9000, blank=True, default='')
    date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        op = ''
        if self.is_op_post():
            op = ' (op)'
        desc = f'/{self.board.address}/{self.id} "{self.body}"{op}'
        return desc

    def is_op_post(self):
        return self.op_post is None
