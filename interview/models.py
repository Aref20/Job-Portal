from email.mime import application
from django.db import models
from application.models import *
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Interview(models.Model):
    interview_application = models.OneToOneField(Application, on_delete=models.SET_NULL, null=True,verbose_name='طلب التوظيف')
    post_date = models.DateField(auto_now_add=True,verbose_name='تاريخ ألإنشاء')
    commitment = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='ألإلتزام بموعد المقابلة')
    MSG_knowledge = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='المعرفة السابقة عن الشركة')
    MSG_comp_knowledge = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='المعرفة السابقة عن قطاع الشركة')
    self_exp_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='المهارات اللفظية بالتعبير عن نفسه')
    body_exp_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='مهارات التعبير والتواصل بلغة الجسد')
    behaviour = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='السلوك أثناء الرد على ألأسئلة')
    listening_skills = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='مهارة ألإستماع للجنة المقابلة')
    asked_q_level = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='مستوى ألأسئلة المطروحة من المرشح')
    eng_lang_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='اللغة الانجليزية')
    computer_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12,verbose_name='مهارات الحاسوب')

    working_experience = models.TextField(max_length=3000,blank=True,verbose_name='الخبرة العملية')
    management_leading_cap = models.TextField(max_length=3000,blank=True,verbose_name='القدرات القيادية أو الادارية')
    tech_cap = models.TextField(max_length=3000,blank=True,verbose_name='القدرات الفنية')
    personality = models.TextField(max_length=3000,blank=True,verbose_name='الشخصية والمظهر العام')
    prev_work_leave = models.TextField(max_length=3000,blank=True,verbose_name='سبب ترك أخر عمل')
    achievements = models.TextField(max_length=3000,blank=True,verbose_name='أهم ألإنجازات برأي المرشح')
    pros = models.TextField(max_length=3000,blank=True,verbose_name='أبرز ألإيجابيات')
    cons = models.TextField(max_length=3000,blank=True,verbose_name='أبرز السلبيات')
    expected_salary = models.IntegerField(max_length=100,default=0,verbose_name='الراتب المتوقع')
    work_time = models.DateTimeField(default=datetime.now,verbose_name='أقرب وقت للإلتحاق بالعمل')
    note = models.TextField(max_length=3000,blank=True,verbose_name='ملاحظات عامة')
    hiring_Recommendation = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='التوصية بالتعين')


      
    def __str__(self):
        return self.interview_application.Name

    class Meta:
        verbose_name = _('المقابلات')
        verbose_name_plural = _('المقابلات')



