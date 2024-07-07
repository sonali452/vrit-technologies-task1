from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_children(self):
        return self.children.all()

    def get_parent(self):
        return self.parent
