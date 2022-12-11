# apis/serializers.py
from rest_framework import serializers
from apps.job.models import Job
from apps.userprofile.models import *

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'



class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class UserLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLanguage
        fields = '__all__'

class Computer_SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer_Skill
        fields = '__all__'

class Previous_CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Previous_Company
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class Previous_CoworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Previous_Coworker
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    Qualification = QualificationSerializer( many=True)
    UserLanguage = UserLanguageSerializer( many=True)
    Computer_Skill = Computer_SkillSerializer(many=True)
    Previous_Company = Previous_CompanySerializer( many=True)
    Training = TrainingSerializer( many=True)
    Previous_Coworker = Previous_CoworkerSerializer( many=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
        