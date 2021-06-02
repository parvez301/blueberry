from typing import Dict, Any
from parking_lot.exceptions import RequestFailureException

from parking_lot.models import *

def create_new_parking_lot(request_data: Dict[str, Any]) -> bool:
    """
    Create new parking lot
    """
    try:
        name = request_data.get("name")
        address = request_data.get("address")
        pincode = request_data.get("pincode")
        operating_company = request_data.get('oprating_company')

        if not all([name, address, pincode]):
            raise RequestFailureException('please provid valid Name, address and pincode')

        try:
            parking_lot = ParkingLot.objects.get(name=name)
        except ParkingLot.DoesNotExist:
            # Add conditional logic before creating owner
            parking_lot = ParkingLot(name=name)
        else:
            raise RequestFailureException(f"Parking lot for given name: {name} already exist")
        try:
            parking_lot_owner = ParkingLotOwner.objects.get(name=operating_company)
        except ParkingLotOwner.DoesNotExist:
            # Add conditional logic before creating owner
            parking_lot_owner = ParkingLotOwner(name=operating_company)
            parking_lot_owner.save()

        parking_lot.address = address
        parking_lot.pincode = pincode
        parking_lot.save()
        
    except Exception as err:
        raise RequestFailureException(str(err))
    else:
        return {
            'status': 'ok'
        }


def create_parking_lot_rate_card(request_data):
    """
    Create parking lot rate card
    """
    parking_lot_id = request_data.get('parking_lot_id')
    vehicle_type = request_data.get('vehicle_type')
    hourly_cost = request_data.get('hourly_cost')
    try:
        parking_lot = ParkingLot.objects.get(id=name)
    except ParkingLot.DoesNotExist:
        raise RequestFailureException(f"Parking lot for given id: {parking_lot_id} does not exist")
    else:
        try:
            rate_card = ParkingLotRateCard(parking_lot=parking_lot, vehicle_type=vehicle_type, hourly_cost=hourly_cost)
            rate_card.save()
        except Exception as err:
            raise RequestFailureException(str(err))
        else:
            {
                'status': "ok"
            }
    

def get_parked_vehicle_history(request_data):
    """
    Get Parked vehicle history
    """
    vehicle_data = ParkedVehicleStatus.objects.filter(request_data.get('vehicle_id')).values_list('vehicle_id', 'parking_lot__name', 'created_at', flat=True)

    return vehicle_data
    

def park_vehicle(request_data):
    """
    Park vehicle util
    """
    parking_lot_id = request_data.get('parking_lot_id')
    vehicle_id = request_data.get('vehicle_id')
    vehicle_type = request_data.get('vehicle_type')

    try:
        spot = ParkedVehicleDetails.objects.create(parking_lot_id=parking_lot_id, vehicle_id=vehicle_id)
    except Exception as err:
        raise RequestFailureException(str(err))
    else:
        return {
            "spot_id": spot.id
        }
