"""Django models utilities"""

#Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model

    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created
        + modified (DateTime): Store the last datetime the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
        
        
class Student(CRideModel):
    """Student model."""
    name = models.CharField()
    
    class Meta(CRideModel.Meta):
        """Meta option."""
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'students'
        
    def __str__(self):
        """Return name."""
        return self.name
    
class Person(models.Model):
    """Person model."""
    name = models.CharField()
    
    
    class Meta:
        """Meta option."""
        db_table = 'person'
        verbose_name = 'person'
        verbose_name_plural = 'persons'
        
    def __str__(self):
        """Return name."""
        return self.name