from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    status_choice=[ 
        ('C','COMPLETED'),
        ('P','PENDING')
    ]
    priority_choice=[
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣')

    ]
    title = models.CharField(max_length=101)
    status = models.CharField(max_length=2,choices=status_choice)
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    priority = models.CharField(max_length=10,choices=priority_choice)

