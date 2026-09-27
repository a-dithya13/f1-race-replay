"""
Test script to explore OpenF1 API and fetch driver information
Save this as: test_openf1_api.py in your project root
"""

import requests
import json

def get_2024_race_session():
    """Get a race session from 2024 with actual data"""
    print("=" * 60)
    print("Finding a 2024 Race Session")
    print("=" * 60)
    
    url = "https://api.openf1.org/v1/sessions"
    params = {
        "year": 2024,
        "session_name": "Race"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        sessions = response.json()
        
        if sessions:
            # Get the first race
            session = sessions[0]
            print(f"\n✅ Found: {session['location']} - {session['session_name']}")
            print(f"   Session Key: {session['session_key']}")
            return session['session_key']
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None

def test_openf1_drivers(session_key):
    """Fetch F1 drivers from a specific session"""
    print("\n" + "=" * 60)
    print("Testing OpenF1 API - Driver Information")
    print("=" * 60)
    
    url = "https://api.openf1.org/v1/drivers"
    params = {
        "session_key": session_key
    }
    
    try:
        print(f"\n📡 Fetching driver data for session {session_key}...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        drivers = response.json()
        
        print(f"✅ Found {len(drivers)} drivers\n")
        
        # Display ALL drivers
        for i, driver in enumerate(drivers):
            print(f"\n🏎️  Driver {i+1}:")
            print(f"   Full Name: {driver.get('full_name', 'N/A')}")
            print(f"   Number: #{driver.get('driver_number', 'N/A')}")
            print(f"   Team: {driver.get('team_name', 'N/A')}")
            print(f"   Country: {driver.get('country_code', 'N/A')}")
            
        print("\n" + "=" * 60)
        print("💡 Full data for first driver:")
        print("=" * 60)
        if drivers:
            print(json.dumps(drivers[0], indent=2))
            
        return drivers
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return None

def test_ergast_api():
    """Test Ergast API for career statistics"""
    print("\n" + "=" * 60)
    print("Testing Ergast API - Career Statistics")
    print("=" * 60)
    
    # Get Max Verstappen's career stats
    driver_id = "max_verstappen"
    
    print(f"\n📡 Fetching career stats for {driver_id}...")
    
    # Get championship wins
    url = f"http://ergast.com/api/f1/drivers/{driver_id}/driverStandings/1.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        standings = data['MRData']['StandingsTable']['StandingsLists']
        championships = len(standings)
        
        print(f"\n🏆 Championships: {championships}")
        
        for standing in standings:
            year = standing['season']
            print(f"   - {year}")
        
        # Get total wins
        url_wins = f"http://ergast.com/api/f1/drivers/{driver_id}/results/1.json?limit=1000"
        response = requests.get(url_wins, timeout=10)
        data = response.json()
        
        total_wins = int(data['MRData']['total'])
        print(f"\n🥇 Career Wins: {total_wins}")
        
        # Get some recent wins
        races = data['MRData']['RaceTable']['Races'][:5]
        print(f"\n   Recent wins:")
        for race in races:
            print(f"   - {race['season']} {race['raceName']}")
        
        return {
            'championships': championships,
            'wins': total_wins
        }
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None

def get_driver_ergast_stats(driver_code):
    """Get specific driver stats from Ergast - reusable function"""
    print(f"\n🔍 Fetching stats for driver code: {driver_code}")
    
    # Convert common codes to Ergast format
    code_mapping = {
        'VER': 'max_verstappen',
        'HAM': 'hamilton',
        'LEC': 'leclerc',
        'NOR': 'norris',
        'SAI': 'sainz',
        'PER': 'perez',
        'RUS': 'russell',
        'ALO': 'alonso',
        'PIA': 'piastri',
        'GAS': 'gasly'
    }
    
    ergast_id = code_mapping.get(driver_code, driver_code.lower())
    
    try:
        # Championships
        url = f"http://ergast.com/api/f1/drivers/{ergast_id}/driverStandings/1.json"
        response = requests.get(url, timeout=10)
        data = response.json()
        championships = len(data['MRData']['StandingsTable']['StandingsLists'])
        
        # Wins
        url_wins = f"http://ergast.com/api/f1/drivers/{ergast_id}/results/1.json?limit=1000"
        response = requests.get(url_wins, timeout=10)
        data = response.json()
        wins = int(data['MRData']['total'])
        
        # Poles
        url_poles = f"http://ergast.com/api/f1/drivers/{ergast_id}/qualifying/1.json?limit=1000"
        response = requests.get(url_poles, timeout=10)
        data = response.json()
        poles = int(data['MRData']['total'])
        
        print(f"   🏆 Championships: {championships}")
        print(f"   🥇 Wins: {wins}")
        print(f"   ⚡ Pole Positions: {poles}")
        
        return {
            'championships': championships,
            'wins': wins,
            'poles': poles
        }
        
    except Exception as e:
        print(f"   ❌ Could not fetch stats: {e}")
        return None

if __name__ == "__main__":
    print("\n🏎️  F1 RACE REPLAY - OpenF1 + Ergast API Test 🏎️\n")
    
    # Get a real race session
    session_key = get_2024_race_session()
    
    if session_key:
        # Test OpenF1 for driver info
        drivers = test_openf1_drivers(session_key)
        
        # Test Ergast for career stats
        test_ergast_api()
        
        # Test getting stats for multiple drivers
        if drivers:
            print("\n" + "=" * 60)
            print("Testing Stats for Current Drivers")
            print("=" * 60)
            
            # Test a few drivers
            test_codes = ['VER', 'HAM', 'LEC']
            for code in test_codes:
                get_driver_ergast_stats(code)
    
    print("\n" + "=" * 60)
    print("✨ Test Complete!")
    print("=" * 60)
    print("\n📊 Summary:")
    print("   ✅ OpenF1 API: Provides current driver info (name, number, team)")
    print("   ✅ Ergast API: Provides career stats (championships, wins, poles)")
    print("   💡 We'll combine both APIs for your feature!")
    print("\n🎯 Next Step: Create the driver stats module")