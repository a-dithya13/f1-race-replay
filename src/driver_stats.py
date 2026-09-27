"""
Driver Statistics Module
Create this file as: src/driver_stats.py

Fetches and caches driver information from OpenF1 API
Combines with manual career stats database
"""

import requests
from typing import Dict, Optional
from src.driver_stats_data import get_driver_stats

# Cache for driver info to avoid repeated API calls
_driver_cache = {}
_session_drivers = {}

def fetch_drivers_from_session(session_key: int) -> Dict:
    """
    Fetch all drivers from a specific OpenF1 session
    
    Args:
        session_key: OpenF1 session key
        
    Returns:
        dict: Dictionary mapping driver codes to driver info
    """
    global _session_drivers
    
    # Return cached if already fetched
    if session_key in _session_drivers:
        return _session_drivers[session_key]
    
    url = "https://api.openf1.org/v1/drivers"
    params = {"session_key": session_key}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        drivers = response.json()
        
        # Convert to dict with driver code as key
        drivers_dict = {}
        for driver in drivers:
            code = driver.get('name_acronym', '')
            if code:
                drivers_dict[code] = driver
        
        _session_drivers[session_key] = drivers_dict
        return drivers_dict
        
    except Exception as e:
        print(f"Error fetching drivers from OpenF1: {e}")
        return {}

def get_complete_driver_info(driver_code: str, session_key: Optional[int] = None) -> Optional[Dict]:
    """
    Get complete driver information combining OpenF1 and career stats
    
    Args:
        driver_code: 3-letter driver code (e.g., 'VER', 'HAM')
        session_key: Optional OpenF1 session key for current data
        
    Returns:
        dict: Complete driver information or None if not found
    """
    driver_code = driver_code.upper()
    
    # Check cache first
    cache_key = f"{driver_code}_{session_key}"
    if cache_key in _driver_cache:
        return _driver_cache[cache_key]
    
    # Get career stats from our database
    career_stats = get_driver_stats(driver_code)
    
    if not career_stats:
        return None
    
    # Start with career stats
    complete_info = {
        "driver_code": driver_code,
        "nickname": career_stats.get("nickname", ""),
        "championships": career_stats.get("championships", 0),
        "career_wins": career_stats.get("career_wins", 0),
        "pole_positions": career_stats.get("pole_positions", 0),
        "podiums": career_stats.get("podiums", 0),
        "notable_achievements": career_stats.get("notable_achievements", []),
        # Defaults from OpenF1 (will be overwritten if available)
        "full_name": "",
        "driver_number": 0,
        "team_name": "",
        "team_colour": "FFFFFF",
        "country_code": "",
        "headshot_url": ""
    }
    
    # Try to get current session data from OpenF1
    if session_key:
        session_drivers = fetch_drivers_from_session(session_key)
        openf1_data = session_drivers.get(driver_code)
        
        if openf1_data:
            complete_info.update({
                "full_name": openf1_data.get("full_name", ""),
                "driver_number": openf1_data.get("driver_number", 0),
                "team_name": openf1_data.get("team_name", ""),
                "team_colour": openf1_data.get("team_colour", "FFFFFF"),
                "country_code": openf1_data.get("country_code", ""),
                "headshot_url": openf1_data.get("headshot_url", "")
            })
    
    # Cache the result
    _driver_cache[cache_key] = complete_info
    return complete_info

def get_driver_track_record(driver_code: str, track_name: str) -> Dict:
    """
    Get driver's best results at a specific track
    This would require historical data - placeholder for future implementation
    
    Args:
        driver_code: 3-letter driver code
        track_name: Name of the circuit
        
    Returns:
        dict: Track-specific stats (currently placeholder)
    """
    # TODO: Implement with historical race data
    # For now, return placeholder
    return {
        "best_finish": "TBD",
        "poles_at_track": 0,
        "wins_at_track": 0,
        "note": "Historical track data coming soon!"
    }

def clear_cache():
    """Clear the driver info cache"""
    global _driver_cache, _session_drivers
    _driver_cache = {}
    _session_drivers = {}

# Example usage and testing
if __name__ == "__main__":
    print("Testing driver_stats module...")
    
    # Test without session key (career stats only)
    print("\n1. Testing career stats (no session key):")
    info = get_complete_driver_info("VER")
    if info:
        print(f"   {info['driver_code']}: {info['nickname']}")
        print(f"   Championships: {info['championships']}")
        print(f"   Wins: {info['career_wins']}")
    
    # Test with session key (full data)
    print("\n2. Testing with OpenF1 session key:")
    session_key = 9472  # 2024 Bahrain race
    info = get_complete_driver_info("VER", session_key)
    if info:
        print(f"   Full Name: {info['full_name']}")
        print(f"   Team: {info['team_name']}")
        print(f"   Number: #{info['driver_number']}")
        print(f"   Championships: {info['championships']}")
    
    print("\n✅ Module test complete!")