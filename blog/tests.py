# from django.test import TestCase, Client
# from bs4 import BeautifulSoup
# from .models import Post
# from django.utils import timezone
# from django.contrib.auth.models import User
#
#
#
# def create_post(title, content, author):
#     blog_post = Post.objects.create(
#         title=title,
#         content=content,
#         created=timezone.now(),
#         author=author,
#     )
#     return blog_post
#
#
# class TestModel(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.author_000 = User.objects.create(username='smith', password='nopassword')
#
#
#
# class TestView(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.author_000 = User.objects.create_user(username='smith', password='nopassword')
#         self.user_obama = User.objects.create_user(username='obama', password='nopassword')
#
#
#
#     def test_post_list_no_post(self):
#         response = self.client.get('/blog/')
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         title = soup.title
#
#         self.assertIn(title.text, 'Blog')
#
#
#         self.assertEqual(Post.objects.count(), 0)
#         self.assertIn('아직 게시물이 없습니다.', soup.body.text)
#
#
#     def test_post_list_with_post(self):
#         post_000 = create_post(
#             title='The first post',
#             content='Hello World. We are the world',
#             author=self.author_000,
#         )
#         post_000.save()
#
#         post_001 = create_post(
#             title='The second post',
#             content='Second Second Second',
#             author=self.author_000,
#         )
#
#         post_001.save()
#
#         self.assertGreater(Post.objects.count(), 0)
#
#         response = self.client.get('/blog/')
#         self.assertEqual(response.status_code, 200)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         body = soup.body
#         self.assertNotIn('아직 게시물이 없습니다', body.text)
#         self.assertIn(post_000.title, body.text)
#
#
#
#
#     def test_pageination(self):
#         # post가 적은 경우
#         for i in range(0, 3):
#             post = create_post(
#                 title='The post No, {}'.format(i),
#                 content='Content {}'.format(i),
#                 author=self.author_000,
#             )
#         response = self.client.get('/blog/')
#         self.assertEqual(response.status_code, 200)
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         self.assertNotIn('Older', soup.body.text)
#         self.assertNotIn('Newer', soup.body.text)
#
#         for i in range(3, 10):
#             post = create_post(
#                 title='The post No, {}'.format(i),
#                 content='Content {}'.format(i),
#                 author=self.author_000,
#             )
#         response = self.client.get('/blog/')
#         self.assertEqual(response.status_code, 200)
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         self.assertIn('Older', soup.body.text)
#         self.assertIn('Newer', soup.body.text)
#
#     def test_post_detail(self):
#         post_000 = create_post(
#             title='The first post',
#             content='Hello World. We are the world',
#             author=self.author_000,
#
#         )
#         post_000.save()
#
#         post_001 = create_post(
#             title='The second post',
#             content='Second Second Second',
#             author=self.author_000,
#
#         )
#
#         self.assertGreater(Post.objects.count(), 0)
#         post_000_url = post_000.get_absolute_url()
#         self.assertEqual(post_000_url, '/blog/{}/'.format(post_000.pk))
#
#         response = self.client.get(post_000_url)
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         title = soup.title
#
#         self.assertEqual(title.text, '{} - Blog'.format(post_000.title))
#
#         body = soup.body
#
#         main_div = body.find('div', id='main-div')
#         self.assertIn(post_000.title, main_div.text)
#         self.assertIn(post_000.author.username, main_div.text)
#
#         self.assertIn(post_000.content, main_div.text)
#
#
#         self.assertNotIn('EDIT', main_div.text)  # EDIT 버튼이 로그인하지 않은 경우 보이지 않는다
#
#         login_success = self.client.login(username='smith', password='nopassword')  # 로그인을 한 경우에는
#         response = self.client.get(post_000_url)
#         self.assertTrue(login_success)
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         main_div = soup.find('div', id='main-div')
#         self.assertEqual(post_000.author, self.author_000)  # post.author와 login 한 사용자가 동일하면
#         self.assertIn('EDIT', main_div.text)  # edit버튼이 있다.
#
#         # 다른 사람인 경우에는 없다.
#         login_success = self.client.login(username='obama', password='nopassword')  # 로그인을 한 경우에는
#         response = self.client.get(post_000_url)
#         self.assertTrue(login_success)
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         main_div = soup.find('div', id='main-div')
#         self.assertEqual(post_000.author, self.author_000)  # post.author와 login 한 사용자가 동일하면
#         self.assertNotIn('EDIT', main_div.text)  # edit버튼이 있다.
#
#
#
#
#
#     def test_post_list_no_category(self):
#
#
#         post_000 = create_post(
#             title='The first post',
#             content='Hello World. We are the world',
#             author=self.author_000,
#         )
#
#         post_001 = create_post(
#             title='The second post',
#             content='Second Second Second',
#             author=self.author_000,
#
#
#
#
#
#     def test_post_create(self):
#         response = self.client.get('/blog/create/')
#         self.assertNotEqual(response.status_code, 200)  # 사용자가 아니면 create화면이 나오지 않도록
#
#         self.client.login(username='smith', password='nopassword')
#         response = self.client.get('/blog/create/')
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         main_div = soup.find('div', id='main-div')
#
#     def test_post_update(self):
#         post_000 = create_post(
#             title='The first post',
#             content='Hello World. We are the world',
#             author=self.author_000,
#         )
#
#         self.assertEqual(post_000.get_update_url(), post_000.get_absolute_url() + 'update/')
#         response = self.client.get(post_000.get_update_url())
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         main_div = soup.find('div', id='main-div')
#
#         self.assertNotIn('created', main_div.text)
#         self.assertNotIn('Author', main_div.text)
