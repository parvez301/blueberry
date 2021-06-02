from django.conf.urls import include, url
from parking_lot.views import ParkingLot, VehicleHistory, ParkVehicle, ParkingLotRateCard

urlpatterns = [
    url(r"^create_parking_lot/", ParkingLot.as_view()),
     url(r"^create_parking_lot_rate_card/", ParkingLot.as_view()),
    url(r"^get_vehicle_history/", VehicleHistory.as_view()),
    url(r"^park_vehicle/", ParkVehicle.as_view())
]