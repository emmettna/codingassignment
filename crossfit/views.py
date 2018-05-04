from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from crossfit.models import *


def add_dummy(request):
    center = CrossfitCenter(name="GoodFit", address="Seoul", PhoneNum="1234")
    center.save()
    mem = CrossfitMember(name="Jane", center_id=CrossfitCenter.objects.get(id=center), password="1234",
                         PhoneNum="010-000-0000")
    mem.save()
    mem2 = CrossfitMember(name="Phill", center_id=CrossfitCenter.objects.get(id=center), password="1234",
                          PhoneNum="010-000-0000")
    mem2.save()
    first_rec = WorkoutRecord(MemberId=CrossfitMember.objects.get(id=mem), workoutName="sprint", recordTime="00:20:20",
                              recordedDate=timezone.now())
    first_rec.save()
    second_rec = WorkoutRecord(MemberId=CrossfitMember.objects.get(id=mem), workoutName="sprint", recordTime="00:20:20",
                               recordedDate=timezone.now())
    second_rec.save()
    third_rec = WorkoutRecord(MemberId=CrossfitMember.objects.get(id=mem), workoutName="sprint", recordTime="00:30:20",
                              recordedDate=timezone.now())
    third_rec.save()
    forth_rec = WorkoutRecord(MemberId=CrossfitMember.objects.get(id=mem2), workoutName="sprint", recordTime="00:20:20",
                              recordedDate=timezone.now())
    forth_rec.save()
    return JsonResponse({"response": "Successfully Added"})


def get_ranks(request):
    """
    1. Takes workout_name as a param
    2. Retrieves data from DB order by recordTime with distinct values only
    3. keeps recordTime(time type) and rank on temp in order to hand the same record as the same rank
    :param request: WorkoutName
    :return: {rank, recordTime, MemberID, CenterName}
    """
    workout_name = "sprint"     # TODO Dummy Data
    # Distinct on fiend is not supported on MySQL nor sqLite
    ranks = WorkoutRecord.objects.filter(workoutName=workout_name).\
        order_by('recordTime').values_list('recordTime',
                                           'MemberId_id',
                                           'MemberId_id__center_id__name').distinct()

    res = []
    cur = timezone.datetime
    rank = int()
    for i, d in enumerate(ranks):
        recordTime = d[0]
        memberId = d[1]
        centerName = d[2]
        if recordTime != cur:
            cur = d[0]
            rank = i
        res.append({"rank": rank + 1,
                    "recordTime": recordTime,
                    "MemberId": memberId,
                    "CenterName": centerName})
    return JsonResponse({"response": res})
