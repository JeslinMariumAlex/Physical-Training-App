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
        return self.trainer_name
    
