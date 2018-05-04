from django.db import models


# Create your models here.
class CrossfitCenter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=True, default=None)
    address = models.TextField(null=True, default=None)
    PhoneNum = models.CharField(max_length=13, null=True, default=None)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.name


class CrossfitMember(models.Model):
    id = models.AutoField(primary_key=True)
    center_id = models.ForeignKey(CrossfitCenter, on_delete=models.CASCADE, null=True, default=None)
    password = models.CharField(max_length=20, null=False, default="1111")
    name = models.CharField(max_length=20, null=True, default=None)
    PhoneNum = models.CharField(max_length=13, null=True, default=None)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.name


class WorkoutRecord(models.Model):
    id = models.AutoField(primary_key=True)
    MemberId = models.ForeignKey(CrossfitMember, on_delete=models.CASCADE, null=True, default=None)
    workoutName = models.CharField(max_length=20, null=True, default=None)
    recordTime = models.TimeField(null=True, default=None)
    recordedDate = models.DateTimeField(null=True, default=None)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.workoutName
