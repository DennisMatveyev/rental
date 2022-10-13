from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=100)


class Reservation(models.Model):
    rental = models.ForeignKey(
        Rental,
        related_name='reservations',
        on_delete=models.CASCADE
    )
    checkin = models.DateField(db_index=True)
    checkout = models.DateField(db_index=True)


class ReservationsView(models.Model):
    id = models.IntegerField(primary_key=True)
    checkin = models.DateField()
    checkout = models.DateField()
    prev_reservation_id = models.IntegerField()
    rental_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rental_app_reservationsview'
