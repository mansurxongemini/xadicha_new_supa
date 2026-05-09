from django.db import models
from django.core.validators import FileExtensionValidator


# Model for the biography page
class Biography(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='biography/')

    class Meta:
        verbose_name = "Biografiya"
        verbose_name_plural = "Biografiyalar"

    def __str__(self):
        return self.title

# Model for the books/library page
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='books/covers/')
    pdf_file = models.FileField(upload_to='books/pdfs/')

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.title

# Model for the video gallery
class VideoResource(models.Model):
    title = models.CharField(max_length=255)
    embed_code = models.TextField(verbose_name="Embed Kod", help_text="YouTube videoning to'liq embed kodini shu yerga tashlang (<iframe>...</iframe>)")
    description = models.TextField(blank=True, null=True, verbose_name="Qisqacha izoh", help_text="Video haqida qisqacha ma'lumot (tahminan 10-15 so'z)")

    class Meta:
        verbose_name = "Video Resurs"
        verbose_name_plural = "Video Resurslar"

    def __str__(self):
        return self.title

# Model for scientific articles
class ScientificArticle(models.Model):
    title = models.CharField(max_length=255)
    publication_source = models.CharField(max_length=255, verbose_name="Nashr manbasi")
    published_date = models.DateField(verbose_name="Nashr sanasi")
    file = models.FileField(
        upload_to='scientific_articles/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['pdf'])],
        help_text="PDF faylni yuklang"
    )

    class Meta:
        verbose_name = "Ilmiy maqola"
        verbose_name_plural = "Ilmiy maqolalar"
        ordering = ['-published_date']

    def __str__(self) -> str:
        return self.title

# Model for news and blog posts
class NewsBlog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_blog/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Yangiliklar va Blog"
        verbose_name_plural = "Yangiliklar va Bloglar"
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

class ProjectAuthor(models.Model):
    full_name = models.CharField(max_length=255)
    student_info = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='author/', blank=True, null=True)

    class Meta:
        verbose_name = "Loyiha Muallifi"
        verbose_name_plural = "Loyiha Mualliflari"

    def __str__(self):
        return self.full_name
