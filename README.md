# blueberry

## API ENDPOINTS

APIs

/GET get_parking_lot_details/<parking_lot_id>
Parking Lot Details

/POST create_parking_lot
Create A parking lot with capacity for each type of vehicle
Request Params:
{
    "name",
    "address",
    "pincode",
    "operating_company"
}


/POST create_rate_card
Request Params
{
    "parking_lot_id"
    "vehicle_type",
    "hourly_cost"
}

Success
/POST park_vehicle  
Request Params
{
    "vehicle_id"
    "vehicle_type"
    "pricing_type"
}

Failure Behaviour
/POST park_vehicle
{
    "vehicle_id"
    "vehicle_type"
    "pricing_type"
}


/GET get_parked_vehicle_details?vehicle_id
# Return the amount due for the duration that vehicle is parked


/GET get_parked_vehicle_history
see complete parking history across all lots
