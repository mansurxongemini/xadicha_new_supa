from django.test import TestCase, Client
from django.urls import reverse
from .models import Book, VideoResource

class CoreSystemTest(TestCase):
    def setUp(self):
        # Setup runs before every test
        self.client = Client()
        
        # Create a dummy book
        self.book = Book.objects.create(
            title="Test Book Unique Title",
            description="This is a test description for the book.",
            # We can skip file uploads for basic logic testing
        )

    def test_homepage_loads_and_shows_book(self):
        """Test that the homepage loads (200 OK) and displays the book title."""
        response = self.client.get(reverse('home'))
        
        # Check if page loads successfully
        self.assertEqual(response.status_code, 200)
        
        # Check if our book title is present in the HTML
        self.assertContains(response, "Test Book Unique Title")

    def test_video_resource_creation(self):
        """Test that VideoResource can be created with embed code."""
        
        embed_code = '<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen></iframe>'
        video = VideoResource.objects.create(title="Test Video", embed_code=embed_code)
        self.assertEqual(video.embed_code, embed_code)

        print("\nAll automated tests passed successfully!")