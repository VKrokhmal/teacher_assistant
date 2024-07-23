import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from user.models import Teacher, Student


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
    payment_info = factory.Faker('text', max_nb_chars=500)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def teachers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for teacher in extracted:
                self.teachers.add(teacher)
