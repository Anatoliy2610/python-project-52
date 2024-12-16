from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import User


class TestTasks(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='T1',
            last_name='M1',
            username='TM1',
        )
        self.user = User.objects.get(id=1)
        Statuses.objects.create(status_name='status1')

        Tasks.objects.create(
            task_name='task1',
            description='d1',
            status_id=1,
            author_id=1,
            executor_id=1,
        )
        Tasks.objects.create(
            task_name='task2',
            description='d2',
            status_id=1,
            author_id=1,
            executor_id=1,
        )

    def test_task_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('tasks'))
        self.assertTrue(len(response.context['tasks1']), 2)

    def test_task_create(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                template_name='actions/create_or_update.html')

        response = self.client.post(reverse('create_task'), {
            'task_name': 'task3',
            'description': 'd3',
            'status': 1,
            'author': 1,
            'executor': 1})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks'))

        response = self.client.get(reverse('tasks'))
        self.assertTrue(len(response.context['tasks1']), 3)

    def test_task_update(self):
        self.client.force_login(self.user)
        task = Tasks.objects.get(id=1)

        response = self.client.post(
            reverse('task_update', kwargs={'task_id': task.id}),
            {
                'task_name': 'task111',
                'description': 'd111',
                'status': 1,
                'author': 1,
                'executor': 1,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks'))
        task.refresh_from_db()
        self.assertEqual([
            task.task_name,
            task.description],
            ['task111', 'd111'])

    def test_task_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('task_delete',
                                    kwargs={'task_id': 2}))
        self.assertRedirects(response, reverse('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tasks.objects.count(), 1)
        self.assertEqual(Tasks.objects.get(pk=1).task_name, 'task1')
