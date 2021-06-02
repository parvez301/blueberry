import enum
from django.db import models

from parking_lot.lib import ChoiceIntEnum


class RowInfo(models.Model):
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        s = ''
        for k, v in self.__dict__.items():
            s += ('%s: %s\n' % (k, v))
        return s

    def to_dict(self):
        return self.__dict__

    class Meta:
        abstract = True

class ParkingLotOwner(RowInfo):
    """
    Parking lot owner model
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        s = ''
        for k, v in self.__dict__.items():
            s += ('%s: %s\n' % (k, v))
        return s

    def to_dict(self):
        return self.__dict__

    class Meta:
        db_table = 'parking_lot_owner'
        app_label = 'api'

class ParkingLot(RowInfo):
    """
    Parking Lot Model
    """
    name = models.CharField(max_length=255, unique=True)
    pincode = models.IntegerField(max_length=6)
    address = models.CharField(max_length=255)
    operating_company = models.ForeignKey(ParkingLotOwner, on_delete=models.CASCADE)

    def __unicode__(self):
        s = ''
        for k, v in self.__dict__.items():
            s += ('%s: %s\n' % (k, v))
        return s

    def to_dict(self):
        return self.__dict__

    class Meta:
        db_table = 'parked_lot'
        app_label = 'api'

@enum.unique
class VehicleType(ChoiceIntEnum):
    undefined = 0
    motorbike = 1
    car = 2


@enum.unique
class ParkedVehicleStatus(ChoiceIntEnum):
    undefined = 0
    parked = 1
    waiting = 2
    banned = 3


class ParkingLotRateCard(RowInfo):
    """
    Parking lot Rate card model
    """
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    vehicle_type = models.IntegerField(choices=VehicleType.choices(), default=0)
    hourly_price = models.IntegerField()

    class Meta:
        db_table = 'parking_lot_rate_card'
        app_label = 'api'


class ParkingLotSpots(RowInfo):
    """
    Parking Lot Spots
    """
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    vehicle_type = models.IntegerField(choices=VehicleType.choices(), default=0)
    number_of_spots = models.IntegerField()

    class Meta:
        db_table = 'parking_lot_spots'
        app_label = 'api'

class ParkedVehicleDetails(RowInfo):
    """
    Parked Vehicle Details
    """
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    parked_vehice_id = models.CharField(max_length=255)
    vehicle_type = models.IntegerField(choices=VehicleType.choices(), default=0)
    status = models.IntegerField(choices=ParkedVehicleStatus.choices(), default=1)

    class Meta:
        db_table = 'parked_vehicle_details'
        app_label = 'api'
