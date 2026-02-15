from datetime import date
from typing import Any

from rest_framework import serializers
from .models import Instructor, Course


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name', 'email', 'experience']
        
        
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Email повинен містити '@'")
        return value
    
    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Досвід не може бути від'ємним")
        return value
        
    def validate(self, attrs):
        return super().validate(attrs)
        
class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        
        
    def validate_start_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Дата старту курсу не може бути в минулому")
        return value

    
    def validate_students_count(self, value):
        if value < 5:
            raise serializers.ValidationError("На курсі має бути мінімум 5 студентів")
        return value

     
    def validate(self, attrs):
        title = attrs.get('title', '')
        if len(title) < 5:
            raise serializers.ValidationError("Назва курсу має бути мінімум 5 символів")
        return attrs
        
    def create(self, validated_data: dict[str, Any]) -> Course:
        instructor_data = validated_data.pop('instructor')
        instructor, _ = Instructor.objects.get_or_create(**instructor_data)
        course = Course.objects.create(instructor=instructor, **validated_data)
        return course
    
    def update(self, instance: Course, validated_data: dict[str, Any]) -> Course:
        instructor_data = validated_data.pop('instructor', None)
        if instructor_data:
            instructor, _ = Instructor.objects.get_or_create(**instructor_data)
            instance.instructor = instructor
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
        

        
        




