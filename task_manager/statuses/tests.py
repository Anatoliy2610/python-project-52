from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Statuses
from task_manager.users.models import User


class TestStatuses(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="T1",
            last_name="M1",
            username="TM1",
        )
        self.user = User.objects.get(id=1)
        Statuses.objects.create(name="status1")
        Statuses.objects.create(name="status2")
        Statuses.objects.create(name="status3")

    def test_status_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("statuses"))
        self.assertTrue(len(response.context["statuses"]), 3)

    def test_status_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("statuses_create"), {"name": "status4"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("statuses"))
        response = self.client.get(reverse("statuses"))
        self.assertTrue(len(response.context["statuses"]), 4)

    def test_status_update(self):
        self.client.force_login(self.user)
        status = Statuses.objects.get(pk=1)
        response = self.client.post(
            reverse("statuses_update", kwargs={"status_id": 1}),
            {"name": "status111"},
        )
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, "status111")

    def test_status_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("statuses_delete", kwargs={"status_id": 3})
        )
        self.assertRedirects(response, reverse("statuses"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Statuses.objects.count(), 2)
        self.assertEqual(Statuses.objects.get(pk=1).name, "status1")
        self.assertEqual(Statuses.objects.get(pk=2).name, "status2")
