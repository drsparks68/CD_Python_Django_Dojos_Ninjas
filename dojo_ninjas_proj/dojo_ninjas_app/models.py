from django.db import models

class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

    def __repr__(self):
        return f"<Dojo Name: {self.name} ({self.id})>"

class ninjas(models.Model):
    dojo_id = models.ForeignKey(dojos, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return f"<Ninja name: {self.first_name} ({self.dojo_id})>"
