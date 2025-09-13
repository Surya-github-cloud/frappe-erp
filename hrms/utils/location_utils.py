cd.import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    
    Args:
        lat1, lon1: Latitude and longitude of first point
        lat2, lon2: Latitude and longitude of second point
    
    Returns:
        Distance in meters
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in meters
    r = 6371000
    
    return c * r

def verify_site_visit_location(captured_location, expected_location, max_distance_meters=100):
    """
    Verify if the captured location is within acceptable distance from expected location
    
    Args:
        captured_location: String in format "lat,lng"
        expected_location: String in format "lat,lng"
        max_distance_meters: Maximum allowed distance in meters
    
    Returns:
        tuple: (is_valid, distance_meters, error_message)
    """
    try:
        if not captured_location or not expected_location:
            return False, 0, "Location coordinates missing"
        
        # Parse coordinates
        captured_lat, captured_lng = map(float, captured_location.split(','))
        expected_lat, expected_lng = map(float, expected_location.split(','))
        
        # Calculate distance
        distance = calculate_distance(captured_lat, captured_lng, expected_lat, expected_lng)
        
        # Check if within acceptable range
        if distance <= max_distance_meters:
            return True, distance, f"Location verified - {distance:.2f}m from expected"
        else:
            return False, distance, f"Location too far - {distance:.2f}m from expected (max: {max_distance_meters}m)"
            
    except ValueError as e:
        return False, 0, f"Invalid location format: {str(e)}"
    except Exception as e:
        return False, 0, f"Error verifying location: {str(e)}"
