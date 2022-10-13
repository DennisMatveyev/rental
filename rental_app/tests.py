import datetime

from django.test import TestCase

from model_bakery import baker

from rental_app.models import ReservationsView


class ReservationsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rental_1 = baker.make('rental_app.Rental', name='Rental 1')
        cls.rental_2 = baker.make('rental_app.Rental', name='Rental 2')

        cls.reservation_1 = baker.make(
            'rental_app.Reservation',
            rental=cls.rental_1,
            checkin=datetime.date(2022, 1, 1),
            checkout=datetime.date(2022, 1, 10)
        )
        cls.reservation_2 = baker.make(
            'rental_app.Reservation',
            rental=cls.rental_1,
            checkin=datetime.date(2022, 1, 11),
            checkout=datetime.date(2022, 1, 20)
        )
        cls.reservation_3 = baker.make(
            'rental_app.Reservation',
            rental=cls.rental_1,
            checkin=datetime.date(2022, 1, 21),
            checkout=datetime.date(2022, 1, 30)
        )
        cls.reservation_4 = baker.make(
            'rental_app.Reservation',
            rental=cls.rental_2,
            checkin=datetime.date(2022, 1, 1),
            checkout=datetime.date(2022, 1, 10)
        )
        cls.reservation_5 = baker.make(
            'rental_app.Reservation',
            rental=cls.rental_2,
            checkin=datetime.date(2022, 1, 11),
            checkout=datetime.date(2022, 1, 15)
        )

    def test_reservations_view(self):
        prev_reservations_map = {
         self.reservation_1.id: None,
         self.reservation_2.id: self.reservation_1.id,
         self.reservation_3.id: self.reservation_2.id,
         self.reservation_4.id: None,
         self.reservation_5.id: self.reservation_4.id
        }

        for rec in ReservationsView.objects.values():
            self.assertEqual(prev_reservations_map[rec.get('id')], rec['prev_reservation_id'])
