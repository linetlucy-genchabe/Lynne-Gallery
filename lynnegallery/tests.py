from django.test import TestCase
from .models import Pictures,Location,Category
# Create your tests here.
class lynnegallery_TestCases(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='fashion')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'africa')
        self.new_location.save_location()
        self.new_pic = Pictures(id=1,name='girls fashion', description='this is a dress',picture_image='media/gallery/dress.jpg',pic_category=self.new_category,pic_location=self.new_location)
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Pictures.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_pic,Pictures))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_pic.save_pictures()
        all_objects = Pictures.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_pic.save_pictures()
        filtered_object = Pictures.objects.filter(name='girls fashion')
        Pictures.delete_pictures(filtered_object)
        all_objects = Pictures.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_pic.save_pictures()
        all_objects = Pictures.retrieve_all()
        self.assertEqual(all_objects.name,'girls fashion')


    def test_update_single_object_property(self):
        self.new_pic.save_pictures()
        filtered_object =Pictures.update_pictures('girls fashion','dress')
        fetched = Pictures.objects.get(name='dress')
        self.assertEqual(fetched.name,'dress')
    def test_get_pictures_by_id(self):
        self.new_pic.save_pictures()
        fetched_pic = Pictures.get_pictures_by_id(1)
        self.assertEqual(fetched_pic.id,1)
    def test_search_by_category(self):
        self.new_pic.save_pictures()        
        fetch_specific = Category.objects.get(category_name='girls fashion')
        self.assertTrue(fetch_specific.category_name=='girls fashion')
    def test_filter_by_location(self):
        self.new_pic.save_pictures()        
        fetch_specific = Location.objects.get(location_name='africa')
        self.assertTrue(fetch_specific.location_name=='africa')