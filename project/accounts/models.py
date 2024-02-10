from django.db import models
from django.contrib.auth.models import User          #django user that already exists contained 5 fields knowns
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete =models.CASCADE) #دلوقت هنعمل علاقة عشان نربط المعلومات المضافة مع اللي موجوده ف الداتابيز ف اليوزر 
                                                        #بيحتاج برامتر بتاع الكاسكيد 
                                                        #عشان اليوزر ده هيبقا له بروفايل ولو مسحت اليوزر امسح البروفايل بتاعه 
                                                        #كدا انا عملت علاقة بين اليوزر والبروفايل بتاعه                                                    
    phone_number = models.CharField(max_length = 15 ,null = True , blank = True)
    address = models.CharField(max_length = 50 ,null = True , blank = True)
    #image / age/ job
    
    #next step go to cmd and makemigrations
    #python manage.py makemigrations
    #python manage.py migrate
    
    #next go to admin.py to make the admin panel view the model you just created 
    
    
    def __str__(self) :
        return str(self.user)  #thisfunction to make the any user created in profile apprear as profile admin instead of profile object1 
    
    
    #محتاجين نهندل الجزء بتاع لما تكريت يوزر روح كريت بروفايل
    #ففيه ارتباط في الحدثين 
    #والارتباط ده ف الكودينج اسمه signal
    #بمعنى اول ما تكريت يوزر ابعتلي سيجنال عشان اكريت بروفايل
    #next function related to signals 
    #سيكونس ماشي ازاي ؟
    # signup(create user)>signal>call function>create profile(user)
    
@receiver(post_save, sender=User)   
def create_user_profile(sender,instance,created,**kwargs):                 #sender > اللي هيرسلي الاشاره اللي لما دا يتنفذ دا هيتنفذ بعده علطول
                                                                           #instance >ودي الحاجة اللي لسه متكريتة لسه معمولها انشاء 
                                                                           #created >دا boolean field هل انت اتكريتت ولا لا
                                                                           #kwargs >ودي خاصة بالمعلومات الاضافية اللي هتتبعت لليوزر اللي اتكريت دا عشان اعرف استقبلها عادي
                                                                           #الفانكشن دي بتقبل 3 برامتر بس 
                                                                           #افرض انت بعت اكتر هيحصل ايرور 
                                                                           #عشان كدا ال kwargs دا معمول
                                                                           #بمعنى لو بعت 10 برامتر ع سبيل المثال 
                                                                           #اول 3 برامتر هيتباصوا لاول تلاتة ف الفانكشن 
                                                                           #والباقي هتضيفهم عادي
    if created:
        Profile.objects.create(
            user = instance
        )                                                                       
        



















'''
جانجو بيعطيلك كل ده جاهز 
username
password 
email
firstname
lasname
ولو حبيت احط معلومات زياده بعمل extend لليوزر دجانجو واضيف عليه بقا
مثلا هستخدم طريقة من الاربع طرق دي
proxy models
ono_to_one field
extend abstract base user
extend abstract user


one_to_one_field 
user (already exists in django (5 fields above)) + profile 
بمعنى ان كل يوزر هيكون له الفيلد بتاع دجانجو وكمان البروفايل الخاص بيه 
فهوجد ريليشن او علاقة بين اليوزر والبروفايل دا وهتكون >> one_to_one

عندي ف الداتا بيز جدول اسمه يوزر فيه اليوزر والباس والفرست واللاست نيم والايميل 
طب لو عايز ازود معلومات لليوزر دا ؟
هكريت جدول جديد اسمه profile واحط فيه المعلومات الزيادة اللي عايزه احطها 
واربط الاتنين ببعض بريليشن one_to_one

'''
