from django.db import models

class Experience(models.Model):
    CATEGORY_CHOICES = [
        ('ORGANIZATION', 'Organization'),
        ('ACADEMIC', 'Academic'),
        ('INTERNSHIP', 'Internship'),
    ]
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, default='')
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ORGANIZATION')
    is_ongoing = models.BooleanField(default=False)
    image_url = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return f"{self.title} - {self.organization}"

class Education(models.Model):
    institution = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    start_period = models.CharField(max_length=50)
    end_period = models.CharField(max_length=50, default='Present')
    logo_url = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return f"{self.institution} - {self.faculty}"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    play_url = models.URLField()

    def __str__(self):
        return self.title

class ArtItem(models.Model):
    CATEGORY_CHOICES = [
        ('characters', 'Characters'),
        ('backgrounds', 'Backgrounds'),
        ('icons', 'Vector Icons'),
        ('tilemaps', 'Tilemaps'),
        ('spritesheets', 'Spritesheets'),
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} ({self.category})"