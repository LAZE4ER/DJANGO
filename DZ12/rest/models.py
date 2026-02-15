from django.db import models




class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    years_of_experience = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    
    
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    students = models.ManyToManyField(
        Student,
        related_name="courses",
        blank=True
    )

    def __str__(self):
        return self.title