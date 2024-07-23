import factory
from django.core.management.base import BaseCommand, CommandError
from user.tests.factories import TeacherFactory, StudentFactory
from user.models import Teacher, Student


class Command(BaseCommand):
    help = 'Create a specified number of Teacher and Student objects using factory-boy'

    def add_arguments(self, parser):
        parser.add_argument('--teacher', type=int, help='Number of Teacher objects to create')
        parser.add_argument('--student', type=int, help='Number of Student objects to create')

    def generate_data_by_provider(self, provider):
        factory.Faker(provider).evaluate(None, None, {"locale": None})

    def handle(self, *args, **options):
        num_teachers = options['teacher']
        num_students = options['student']
        teachers = []
        if num_teachers is not None:
            if num_teachers < 0:
                raise CommandError('Number of teachers must be a positive integer.')
            teachers = TeacherFactory.create_batch(num_teachers)
            self.stdout.write(self.style.SUCCESS(f'Successfully created {num_teachers} Teacher objects.'))
        print(teachers)
        for teacher in teachers:
            if num_students is not None:
                if num_students < 0:
                    raise CommandError('Number of students must be a positive integer.')
                students = StudentFactory.create_batch(num_students, teachers=teacher)
                self.stdout.write(self.style.SUCCESS(f'Successfully created {num_students} Student objects.'))
