from django.test import TestCase
from reviews.models import Publisher, Book, Contributor, Review

class TestPublisherModel(TestCase):
    def setUp(self):
        self.p = Publisher(name='Packt', website='www.packt.com', email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")


class TestBookModel(TestCase):
    def setUp(self):
        publisher = Publisher(name='Packt', website='www.packt.com', email='contact@packt.com')
        self.p = Book(title='Book_title', publication_date='2018-10-31', isbn='24141234324', publisher=publisher)

    def test_create_book(self):
        self.assertIsInstance(self.p, Book)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Book_title")


class TestContributorModel(TestCase):
    def setUp(self):
        self.p = Contributor(first_names='Clint', last_names='Bookcreator', email='contact@packt.com')

    def test_create_contributor(self):
        self.assertIsInstance(self.p, Contributor)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Clint")


class TestReviewModel(TestCase):
    def setUp(self):
        self.p = Review(content='Test_review', rating=5)

    def test_create_review(self):
        self.assertIsInstance(self.p, Review)
        