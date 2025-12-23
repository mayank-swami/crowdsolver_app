from django.db import models


class signup(models.Model):
    name = models.CharField(max_length=100)
    email_flatno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# class raiseproblem(models.Model):
#     title = models.ForeignKey.CharField(max_length=200)
#     description = models.ForeignKey.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

class raiseproblem(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(signup, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class givesuggestion(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(signup, on_delete=models.CASCADE)
    approval = models.IntegerField(default=0)
    reject = models.IntegerField(default=0)
    # approved = models.BooleanField(default=False)
    def __str__(self):
        return self.content[:50]
    

    
class voting(models.Model):
    memberdata = models.ForeignKey(signup, on_delete=models.CASCADE)
    suggestiondata = models.ForeignKey(givesuggestion, on_delete=models.CASCADE)
    is_approval = models.BooleanField(default=False)
    class Meta:
        unique_together = ('memberdata', 'suggestiondata')

# class solution(models.Model):
#     suggestion = models.ForeignKey(givesuggestion, on_delete=models.CASCADE)
#     approval_count = models.IntegerField(default=0)
#     reject_count = models.IntegerField(default=0)        
class solution(models.Model):
    suggestion = models.ForeignKey(givesuggestion, on_delete=models.CASCADE)
    approval_count = models.IntegerField(default=0)
    reject_count = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)


    

    

