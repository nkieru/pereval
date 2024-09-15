
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Users, Coords, Level, Added, Images
from .serializers import AddedSerializer, ImagesSerializer



class AddedApiTestCase(APITestCase):
    def setUp(self):
        self.added_1 = Added.objects.create(beautyTitle='BTitle_1', title='Title_1', other_titles='OTitle_1',
                                       connect='C_1',
                                       user=Users.objects.create(email='test_1@example.com',
                                                                 phone='11111111111',
                                                                 fam='Fam_1',
                                                                 name='Name_1',
                                                                 otc='Otc_1'),
                                       coord=Coords.objects.create(latitude=11.01, longitude=11.01, height=1111),
                                       level=Level.objects.create(winter='1А', summer='1А', autumn='1А', spring='1А'),
                                       activities_types='01', status='N')
        self.image_1 = Images.objects.create(add=self.added_1, title_img='image_1',
                                        data='https://cdn.culture.ru/images/5517e3f2-4fdf-50c8-a025-23bec1a658b4')

        self.added_2 = Added.objects.create(beautyTitle='BTitle_2', title='Title_2', other_titles='OTitle_2',
                                            connect='C_2',
                                            user=Users.objects.create(email='test_2@example.com',
                                                                      phone='22222222222',
                                                                      fam='Fam_2',
                                                                      name='Name_2',
                                                                      otc='Otc_2'),
                                            coord=Coords.objects.create(latitude=22.02, longitude=22.02, height=2222),
                                            level=Level.objects.create(winter='2А', summer='2А', autumn='2А',
                                                                       spring='2А'),
                                            activities_types='02', status='N')
        self.image_2 = Images.objects.create(add=self.added_2, title_img='image_2',
                                             data='https://cdn.culture.ru/images/abc3a521-56e4-502e-b0aa-3591f2885fa7')


    def test_get_list(self):
        url = reverse('added-list')
        response = self.client.get(url)
        serializer_data = AddedSerializer([self.added_1, self.added_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_get_images(self):
        url = reverse('images-list')
        response = self.client.get(url)
        serializer_data = ImagesSerializer([self.image_1, self.image_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('added-detail', args=(self.added_1.id,))
        response = self.client.get(url)
        serializer_data = AddedSerializer(self.added_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_email_added(self):
        url = reverse('user__email', args=(self.added_1.user.email,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddedSerializerTestCase(TestCase):
    def setUp(self):
        self.added_1 = Added.objects.create(beautyTitle='BTitle_1', title='Title_1', other_titles='OTitle_1',
                                            connect='C_1',
                                            user=Users.objects.create(email='test_1@example.com',
                                                                      phone='11111111111',
                                                                      fam='Fam_1',
                                                                      name='Name_1',
                                                                      otc='Otc_1'),
                                           coord=Coords.objects.create(latitude=11.01, longitude=11.01, height=1111),
                                           level=Level.objects.create(winter='1А', summer='1А', autumn='1А', spring='1А'),
                                           activities_types='01', status='N')
        self.image_1 = Images.objects.create(add=self.added_1, title_img='image_1',
                                            data='https://cdn.culture.ru/images/5517e3f2-4fdf-50c8-a025-23bec1a658b4')

        self.added_2 = Added.objects.create(beautyTitle='BTitle_2', title='Title_2', other_titles='OTitle_2',
                                            connect='C_2',
                                            user=Users.objects.create(email='test_2@example.com',
                                                                      phone='22222222222',
                                                                      fam='Fam_2',
                                                                      name='Name_2',
                                                                      otc='Otc_2'),
                                            coord=Coords.objects.create(latitude=22.02, longitude=22.02, height=2222),
                                            level=Level.objects.create(winter='2А', summer='2А', autumn='2А',
                                                                       spring='2А'),
                                            activities_types='02', status='N')
        self.image_2 = Images.objects.create(add=self.added_2, title_img='image_2',
                                             data='https://cdn.culture.ru/images/abc3a521-56e4-502e-b0aa-3591f2885fa7')

    def test_serializer_expected_data(self):
        serializer_data = AddedSerializer([self.added_1, self.added_2], many=True).data
        expected_data = [
            {
            'id': self.added_1.id,
            'beautyTitle': 'BTitle_1',
            'title': 'Title_1',
            'other_titles': 'OTitle_1',
            'connect': 'C_1',
            'add_time': self.added_1.add_time.strftime('%Y-%m-%d %H:%M:%S'),
            'user': {
                'email': 'test_1@example.com',
                'phone': '11111111111',
                'fam': 'Fam_1',
                'name': 'Name_1',
                'otc': 'Otc_1',
            },
            'coord': {
                'latitude': 11.01,
                'longitude': 11.01,
                'height': 1111
            },
            'level': {'winter': '1А',
                      'summer': '1А',
                      'autumn': '1А',
                      'spring': '1А'
                      },
            'activities_types': '01',
            'status': 'N',
            'images': [
                {
                'title_img': 'image_1',
                'data': 'https://cdn.culture.ru/images/5517e3f2-4fdf-50c8-a025-23bec1a658b4'
                }
            ]
            },
            {
                'id': self.added_2.id,
                'beautyTitle': 'BTitle_2',
                'title': 'Title_2',
                'other_titles': 'OTitle_2',
                'connect': 'C_2',
                'add_time': self.added_1.add_time.strftime('%Y-%m-%d %H:%M:%S'),
                'user': {
                    'email': 'test_2@example.com',
                    'phone': '22222222222',
                    'fam': 'Fam_2',
                    'name': 'Name_2',
                    'otc': 'Otc_2',
                },
                'coord': {
                    'latitude': 22.02,
                    'longitude': 22.02,
                    'height': 2222
                },
                'level': {'winter': '2А',
                          'summer': '2А',
                          'autumn': '2А',
                          'spring': '2А'
                          },
                'activities_types': '02',
                'status': 'N',
                'images': [
                    {
                        'title_img': 'image_2',
                        'data': 'https://cdn.culture.ru/images/abc3a521-56e4-502e-b0aa-3591f2885fa7'
                    }
                ]
            }
        ]
        self.assertEqual(serializer_data, expected_data)
