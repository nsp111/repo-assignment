from django.db import models

Category=[
    ('OOP','OOP'),
    ('Programming','Programming'),
    ('Business','Business'),
    ('Comics','Comics'),
    ('Self Development','Self Development'),
    ('Accounting','Accounting'),
    ('Math','Math'),
    ('Physics','Physics'),
    ('Magasine','Magasine'),
    ('Software Engineering','Software Engineering')
    
]
Fine_Category=[
    ('Book Lost','Book Lost'),
    ('Late Submission','Late Submission'),
    ('Book Damage','Book Damage')
]

class Books(models.Model):
    title=models.CharField(max_length=100, null=False, blank=False)
    ISBN=models.CharField(max_length=50, primary_key=True, null=False, blank=False)
    category=models.CharField(choices=Category, max_length=50)
    desciption=models.TextField()
    publisheDate=models.DateField()
    author=models.CharField(null=False,blank=False ,max_length=50)
    borrowed=models.BooleanField(default=False)
    borowDate=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class feedback(models.Model):
    feedback=models.TextField()
    book=models.ForeignKey(Books, verbose_name=("Bookfeedback"), on_delete=models.CASCADE)
    def __str__(self):
        return self.feedback

class Fine(models.Model):
    category=models.CharField(choices=Fine_Category, max_length=50, default='Book Lost')
    book=models.OneToOneField(Books, verbose_name=("bookFine"), on_delete=models.CASCADE)
    dueDate=models.DateField(auto_now_add=True)
    fine=models.IntegerField(default=0)
    def __str__(self):
        return self.category

