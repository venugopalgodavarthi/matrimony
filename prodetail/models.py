from django.db import models
from authe.models import registermodel
# Create your models here.
class details(models.Model):
    userid=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    surname=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    dob=models.DateField()
    time=models.TimeField()
    aob=models.CharField(max_length=50)
    rasilist=[['Aries','Aries'],['Taurus','Taurus'],['Gemini','Gemini'],['Cancer','Cancer'],['Leo','Leo'],['Virgo','Virgo'],['Libra','Libra'],['Scorpio','Scorpio']
    ,['Saggitarius','Saggitarius'],['Capricorn','Capricorn'],['Aquarius','Aquarius'],['Pisces','Pisces']
    ]
    rasi=models.CharField(max_length=20,choices=rasilist)
    nakshatra=models.CharField(max_length=15)
    padhalist=[['1','1'],['2','2'],['3','3'],['4','4']]
    padha=models.CharField(max_length=3,choices=padhalist)
    height=models.FloatField()
    color=models.CharField(max_length=20)
    img=models.ImageField(upload_to='profilepic/')

class education(models.Model):
    highedu=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    userid=models.ForeignKey(registermodel,on_delete=models.CASCADE)

class occupation(models.Model):
    job=models.CharField(max_length=30)
    salary=models.FloatField()
    company=models.CharField(max_length=50)
    userid=models.ForeignKey(registermodel,on_delete=models.CASCADE)

class family(models.Model):
    fname=models.CharField(max_length=50)
    focc=models.CharField(max_length=50)
    fphone=models.BigIntegerField()
    mname=models.CharField(max_length=50)
    mocc=models.CharField(max_length=50)

class siblings(models.Model):
    userid=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    sname=models.CharField(max_length=50)
    oname=models.CharField(max_length=50)
    st=[['Married','Married'],['UnMarried','UnMarried']]
    statusm=models.CharField(max_length=10,choices=st)
    

class address(models.Model):
    pdno=models.CharField(max_length=20)
    streetname=models.CharField(max_length=30)
    landmark=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    pincode=models.IntegerField()
    userid=models.ForeignKey(registermodel,on_delete=models.CASCADE)

class profilelink(models.Model):
    flink=models.CharField(max_length=30)
    llink=models.CharField(max_length=30)
    ylink=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    alphone=models.BigIntegerField()
    email=models.EmailField()
    userid=models.ForeignKey(registermodel,on_delete=models.CASCADE)