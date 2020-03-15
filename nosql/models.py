from djongo import models

# simple blog application
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedOn  = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title