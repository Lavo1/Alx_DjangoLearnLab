from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book, Author  # Author is assumed to exist

class BookAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create authors
        self.author_a = Author.objects.create(name='Author A')
        self.author_b = Author.objects.create(name='Author B')

        # Create books
        self.book1 = Book.objects.create(title='Book One', author=self.author_a, publication_year=2000)
        self.book2 = Book.objects.create(title='Book Two', author=self.author_b, publication_year=2010)

        self.list_url = reverse('book-list')    # From your BookViewSet
        self.detail_url = reverse('book-detail', args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "author": self.author_a.id, "publication_year": 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "New Book", "author": self.author_a.id, "publication_year": 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "New Book", "author": self.author_a.id, "publication_year": 2005}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {'author': self.author_a.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(all(book['author'] == self.author_a.id for book in response.data))

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Book Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Book Two' in book['title'] for book in response.data))

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
