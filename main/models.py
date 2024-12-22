from django.db import models

# Create your models here.

class Workout(models.Model):
    workout_name = models.CharField(max_length=100)
    workout_description = models.TextField()

    def __str__(self):
        return self.workout_name

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=100)
    trainer_spec = models.CharField(max_length=100)
    workout_name = models.ForeignKey(Workout, on_delete=models.CASCADE)
    trainer_image = models.ImageField(upload_to='trainer_images')

    def __str__(self):
        return self.trainer_name + ' - ' + self.trainer_spec

class Appointment(models.Model):
    person_name = models.CharField(max_length=100)
    person_phone = models.CharField(max_length=10)
    person_email = models.EmailField()
    trainer_name = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    booked_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.person_name
    
