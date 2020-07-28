from django.test import TestCase,Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name = 'the5fire',
            sex = 1,
            email='nobody@the5fire.com',
            profession='程序员',
            qq='3333',
            phone='222222',
        )
    
    def test_creat_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='33333',
            phone='55555',
        )
        self.assertEqual(student.sex_show,'男','性别字段内容跟展示不一致！')
        
    def test_creat_and_get_sex_display(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='33333',
            phone='55555',
        )
        self.assertEqual(student.get_sex_display(),'男','性别字段内容跟展示不一致！')
        self.assertEqual(student.get_sex_display(),'男','性别字段内容跟展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='liyang',
            sex=1,
            email='liyang@dd.com',
            profession='程序员',
            qq='8888',
            phone='99999',
        )
        name='the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,
                         '应该只存在一个名称为{}的记录'.format(name))
    
    def test_get_index(self):
        #测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200,'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data=dict(
            name='test_for_post',
            sex=1,
            email='test_for_post@dd.com',
            profession='程序员',
            qq='8883338',
            phone='99333999',
            status='1',
        )
        response=client.post('/',data)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response=client.get('/')
        self.assertTrue(b'8883338' in response.content,
                        'response context must contain `test_for_post`')
        


# Create your tests here.
