from django.db import models
from django.core import validators

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()
    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)
    __str__ = __repr__

class Account(models.Model):
    account = models.ForeignKey(User, related_name='accounts', on_delete=models.CASCADE)
    def __repr__(self):
        return "{}: {}".format(self.pk, self.account)
    __str__ = __repr__

class Entry(models.Model):
    STATUS_TBD = "tbd"
    STATUS_DONE = "done"
    STATUS_SET = (
        (STATUS_TBD, "To Be Determined"),
        (STATUS_DONE, "Done"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    score = models.IntegerField(default=3, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(5)])
    comment = models.TextField(default="Please add some comment")
    status = models.CharField(choices=STATUS_SET, default=STATUS_TBD, max_length=128)
    reporter = models.ForeignKey(Account, related_name='entries', on_delete=models.CASCADE)