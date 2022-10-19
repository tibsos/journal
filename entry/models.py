from django.db import models as m

class Entry(m.Model):
    title = m.CharField(max_length=100,blank=True,null=True)
    
    dreams=m.TextField(max_length=9999,blank=True,null=True)

    meals=m.TextField(max_length=9999,blank=True,null=True)
    
    conversations=m.TextField(max_length=9999,blank=True,null=True)

    sex=m.TextField(max_length=9999,blank=True,null=True)

    ssilo4ka_progress=m.TextField(max_length=9999,blank=True,null=True)

    went_well=m.TextField(max_length=9999,blank=True,null=True)
    could_be_better=m.TextField(max_length=9999,blank=True,null=True)
    ultimate_questions=m.TextField(max_length=9999,blank=True,null=True)


    wake_up_time=m.TimeField()
    bed_time=m.TimeField()
    woke_up=m.PositiveSmallIntegerField()

    created_at=m.DateTimeField(auto_now_add=True)
    updated_at=m.DateTimeField(auto_now=True)