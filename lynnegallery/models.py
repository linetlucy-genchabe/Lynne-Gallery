from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class Location(models.Model):
    location_name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self):
            return self.location_name


    def save_location(self):
        self.save()

            
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self):
        return self.category_name


    def save_category(self):
        self.save()
class Pictures(models.Model):
    name = models.CharField(max_length =50)
    description = models.CharField(max_length=500)
    picture_image = models.ImageField(upload_to = 'gallery/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(category__icontains=search_term)
        return search_result

    @classmethod
    def get_pictures_by_id(cls,incoming_id):
        pictures_result = cls.objects.get(id=incoming_id)
        return pictures_result

    def save_pictures(self):
        self.save()
    def delete_pictures(self):
        self.delete()

    

    @classmethod
    def update_pictures(cls,current_value,new_value):
        fetched_object = Pictures.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def filter_by_location(cls,location):
        filtered_result = cls.objects.filter(location__icontains=location)
        return filtered_result




   
