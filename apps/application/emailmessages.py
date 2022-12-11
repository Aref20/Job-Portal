from mimetypes import init


class Emessage:


    def __init__(self,firstname,lastname,job,date,hour):
        self.firstname = firstname
        self.lastname = lastname
        self.job = job
        self.date = date
        self.hour = hour
        

    def welcomemessage(self):

        return """ 
        <!DOCTYPE html>
<html lang="ar" >
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <div dir="rtl" style="width: 100%;text-align: right;">
            عزيزي / عزيزتي ( """+self.firstname+"""   """ + self.lastname+""") <br>
            تـحـيــة طيبـة وبـعـد،<br>
            نشكـر حضرتكم لتقـديم طلب توظيف فـي شركة منير سختيان<br>
            و نود إعلام حضرتكم  أنه قد تم إستلام طلبكم من قبلنا و أنه قيد الفرز و التدقيق, و سوف نقوم بموافاتكم بمدى إمكانية إدراج  الطلب في قاعدة البيانات الخاصة بشركتنا من خلال البريد الإلكتروني و ذلك خلال فترة  ثلاثة أسابيع  من تاريخه. 
    </div>

  </body>
</html>
            """  

            
    def firstinterview(self):
        return """
        <!DOCTYPE html>
        <html lang="ar" >
          <head>
            <meta charset="utf-8">
            <title></title>
          </head>
          <body>

            <div dir="rtl" style="width: 100%;text-align: right;">
                    عزيزي/ عزيزتي (""" + self.lastname+""" """ +self.firstname+""") <br>
                    تـحـيــة طيبـة وبـعـد،<br>
                    نشكر لكم إهتمامكم بتقديم طلب توظيف لدى شركة "منير سختيان" حيث تسعى الشركة  دائما لتشجيع وضم أفضل  الكوادر المؤهلة لفريقها المتميز  و ذلك بطريقة علمية و مهنية , و من أجل إتاحة الفرص المتساوية للجميع و حيث أن المقابلة الشخصية تعتبر الخطوة الأولى في هذه المسيرة  ، يسرنا دعوتكم لمقابلة شخصية مبدئية مع  اللجنة المختصة لدينا وذلك للنظر في مدى توافق  وظيفة  """ + self.job+""" مع ما لديكم من مؤهلات علمية و عملية و ذلك في تاريخ  """+self.date+"""و ذلك في الساعة  """+self.hour+"""<br>
                    ملاحظة : يرجى من حضرتكم احضار صور عن الشهادات العلمية وشهادات الخبرة ان وجدت .
            </div>

          </body>
        </html>
                """

    def rejectinterview(self):
        return """
        <!DOCTYPE html>
        <html lang="ar" >
          <head>
            <meta charset="utf-8">
            <title></title>
          </head>
          <body>

            <div dir="rtl" style="width: 100%;text-align: right;">
                    عزيزي/ عزيزتي (""" + self.lastname+""" """ +self.firstname+""") <br>
                    تـحـيــة طيبـة وبـعـد،<br>
                    نشكر لكم حضوركم للمقابلة الشخصية التي تمت مع حضرتكم  لدينا اذ اننا نقدر حماسكم واهتمامكم للعمل مع فريقنا المتميز , و نتقدم بالإعتذار من حضرتكم بخصوص الوظيفة التي قد تم مقابلتكم بخصوصها حيث أننا نأسف لعدم استطاعتنا توظيفكم في هذه الفترة و نتمى لكم التوفيق مستقبلاً, حيث قد يتم  إعادة  الإتصال بحضرتكم للحضور لمقابلة ثانية خلال فترة الطلب المحددة في حالة توفر وظائف تتناسب مع ما لديكم من مؤهلات علمية و عملية .
            </div>

          </body>
        </html>
                """


    def secoundInterview(self):
        return """
        <!DOCTYPE html>
        <html lang="ar" >
          <head>
            <meta charset="utf-8">
            <title></title>
          </head>
          <body>

            <div dir="rtl" style="width: 100%;text-align: right;">
                    عزيزي/ عزيزتي (""" + self.lastname+""" """ +self.firstname+""") <br>
                    تـحـيــة طيبـة وبـعـد،<br>
                    نشكـر لكـم اهتمـامكـم بشركة منير سختيان  و رغبتكـم فـي الانضمـام لفريق عملنا المتميز .<br>
                    لقـد أبديتـم حسن المـعرفـة والـخـبـرة فـي المقابلة المبدئية وعليه يسعدنا حضوركم لإجراء  <br>
                    مقابلة ثانية , حتى يتسنى لنا اتخاذ القرار بشأن وظيفة """ +self.job+""" وذلك في يوم """ +self.date+""" الـساعـة """ +self.hour+""" .فـي مقـر الشركة <br>
            </div>

          </body>
        </html>
                """


        
