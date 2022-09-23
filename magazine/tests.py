from django.test import TestCase, Client


class TestHomepage(TestCase):
    def test_open_homepage_should_be_success(self): # expected success
        c = Client()
        response = c.get("http://127.0.0.1:8000/magazine/")
        assert response.status_code == 200
#
    def test_post_homepage_should_return_405(self): # expected fail
        c = Client()
        response = c.post("http://127.0.0.1:8000/")
        assert response.status_code == 404, f"{response.status_code} should be 405"
#
#
class TestProductCreate(TestCase):
    def test_should_allow_only_post(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/magazine/")
        assert response.status_code == 200
        response = c.put("http://127.0.0.1:8000/magazine/")
        assert response.status_code == 401
        response = c.delete("http://127.0.0.1:8000/magazine/")
        assert response.status_code == 401
        response = c.patch("http://127.0.0.1:8000/magazine/")
        assert response.status_code == 401
#
    def test_should_create_product(self):
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/magazine/",
            data={
                "title": "test product 1",
                "price": 1200
            }
        )
        assert response.status_code == 401
#
    def test_too_long_name_should_fail(self):
        c = Client()
        text = "a" * 300
        response = c.post(
            "http://127.0.0.1:8000/magazine/",
            data={
                "title": text,
                "price": 1200
            }
        )
        assert response.status_code == 401
