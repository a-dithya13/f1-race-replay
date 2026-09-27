"""
Driver Statistics Database
Create this file as: src/driver_stats_data.py

Contains career stats, nicknames, and achievements for F1 drivers
Data as of 2024 season
"""

# Career statistics for current F1 drivers
DRIVER_STATS = {
    # Red Bull Racing
    "VER": {
        "nickname": "Mad Max / Super Max",
        "championships": 3,
        "career_wins": 54,
        "pole_positions": 38,
        "podiums": 103,
        "notable_achievements": [
            "3x World Champion (2021, 2022, 2023)",
            "Most wins in a season (19 in 2023)",
            "Youngest points scorer (17 years)"
        ]
    },
    "PER": {
        "nickname": "Checo",
        "championships": 0,
        "career_wins": 6,
        "pole_positions": 3,
        "podiums": 36,
        "notable_achievements": [
            "Sakhir GP 2020 winner",
            "Multiple podiums with Red Bull",
            "Strong defensive driver"
        ]
    },
    
    # Mercedes
    "HAM": {
        "nickname": "The GOAT / #Blessed",
        "championships": 7,
        "career_wins": 103,
        "pole_positions": 104,
        "podiums": 197,
        "notable_achievements": [
            "7x World Champion (2008, 2014-2020)",
            "Most race wins in F1 history",
            "Most pole positions in F1 history",
            "First Black F1 World Champion"
        ]
    },
    "RUS": {
        "nickname": "George / Mr. Saturday",
        "championships": 0,
        "career_wins": 2,
        "pole_positions": 3,
        "podiums": 12,
        "notable_achievements": [
            "Brazil 2022 winner",
            "Qualified 2nd on Williams debut",
            "Strong qualifier"
        ]
    },
    
    # Ferrari
    "LEC": {
        "nickname": "Il Predestinato / Charlie",
        "championships": 0,
        "career_wins": 5,
        "pole_positions": 24,
        "podiums": 35,
        "notable_achievements": [
            "Multiple wins with Ferrari",
            "Monaco resident",
            "Exceptional qualifier"
        ]
    },
    "SAI": {
        "nickname": "Smooth Operator",
        "championships": 0,
        "career_wins": 3,
        "pole_positions": 5,
        "podiums": 23,
        "notable_achievements": [
            "Singapore 2023 winner",
            "Consistent points scorer",
            "Strong racecraft"
        ]
    },
    
    # McLaren
    "NOR": {
        "nickname": "Lando / Landinho",
        "championships": 0,
        "career_wins": 3,
        "pole_positions": 4,
        "podiums": 21,
        "notable_achievements": [
            "Youngest British F1 driver",
            "Multiple podiums",
            "Twitch streamer"
        ]
    },
    "PIA": {
        "nickname": "Oscar / The Iceman",
        "championships": 0,
        "career_wins": 2,
        "pole_positions": 0,
        "podiums": 9,
        "notable_achievements": [
            "F2 Champion 2021",
            "Sprint race winner 2023",
            "Impressive rookie season"
        ]
    },
    
    # Aston Martin
    "ALO": {
        "nickname": "El Nano / Magic Alonso",
        "championships": 2,
        "career_wins": 32,
        "pole_positions": 22,
        "podiums": 106,
        "notable_achievements": [
            "2x World Champion (2005, 2006)",
            "Youngest champion at the time",
            "Le Mans 24h winner",
            "Racing legend still competing"
        ]
    },
    "STR": {
        "nickname": "Lance / Lancey",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 1,
        "podiums": 3,
        "notable_achievements": [
            "Youngest podium finisher",
            "Pole position in Turkey 2020",
            "Son of team owner"
        ]
    },
    
    # Alpine
    "GAS": {
        "nickname": "Pierre / Gastly",
        "championships": 0,
        "career_wins": 1,
        "pole_positions": 0,
        "podiums": 4,
        "notable_achievements": [
            "Monza 2020 winner",
            "AlphaTauri's only win",
            "Strong midfield performer"
        ]
    },
    "OCO": {
        "nickname": "Esteban / Ocon",
        "championships": 0,
        "career_wins": 1,
        "pole_positions": 0,
        "podiums": 3,
        "notable_achievements": [
            "Hungary 2021 winner",
            "Mercedes junior driver",
            "Consistent points scorer"
        ]
    },
    
    # Williams
    "ALB": {
        "nickname": "Albon / Alex",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 2,
        "notable_achievements": [
            "Multiple podiums with Red Bull",
            "Comeback with Williams",
            "Strong racecraft"
        ]
    },
    "SAR": {
        "nickname": "Sargeant / Logan",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "F3 champion",
            "First American in F1 since 2015",
            "Development driver"
        ]
    },
    
    # RB (AlphaTauri)
    "TSU": {
        "nickname": "Yuki / Tsunami",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "Points on debut",
            "Japanese rising star",
            "Aggressive racer"
        ]
    },
    "RIC": {
        "nickname": "Honey Badger / Danny Ric",
        "championships": 0,
        "career_wins": 8,
        "pole_positions": 3,
        "podiums": 32,
        "notable_achievements": [
            "Multiple race winner",
            "Monaco specialist",
            "Fan favorite personality"
        ]
    },
    
    # Haas
    "MAG": {
        "nickname": "K-Mag / The Viking",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 1,
        "podiums": 1,
        "notable_achievements": [
            "Pole position on return 2022",
            "Aggressive defender",
            "Comeback story"
        ]
    },
    "HUL": {
        "nickname": "Hulk / Nico",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 1,
        "podiums": 0,
        "notable_achievements": [
            "Most races without a podium",
            "Le Mans 24h winner",
            "Consistent midfielder"
        ]
    },
    
    # Kick Sauber
    "BOT": {
        "nickname": "Valtteri / Porridge",
        "championships": 0,
        "career_wins": 10,
        "pole_positions": 20,
        "podiums": 67,
        "notable_achievements": [
            "Multiple wins with Mercedes",
            "Strong qualifier",
            "Team player extraordinaire"
        ]
    },
    "ZHO": {
        "nickname": "Zhou / Guanyu",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "First Chinese F1 driver",
            "F2 podium finisher",
            "Breaking barriers"
        ]
    },
    
    # 2024/2025 Rookies and Recent Additions
    "BEA": {
        "nickname": "Ollie / The Brit",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "F2 Champion 2023",
            "Ferrari Academy driver",
            "Haas F1 rookie 2024"
        ]
    },
    "ANT": {
        "nickname": "Antonelli / Kimi",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "Mercedes junior driver",
            "F2 competitor",
            "Highly rated prospect"
        ]
    },
    "LAW": {
        "nickname": "Lawson / Liam",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "Red Bull junior driver",
            "RB/AlphaTauri substitute",
            "Strong performances in limited chances"
        ]
    },
    "COL": {
        "nickname": "Colapinto / Franco",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "Williams F1 2024",
            "Argentine rising star",
            "F2 competitor"
        ]
    },
    "DOO": {
        "nickname": "Doohan / Jack",
        "championships": 0,
        "career_wins": 0,
        "pole_positions": 0,
        "podiums": 0,
        "notable_achievements": [
            "Alpine reserve driver",
            "Son of Mick Doohan",
            "F2 experience"
        ]
    },
}

def get_driver_stats(driver_code):
    """
    Get career statistics for a driver by their code
    
    Args:
        driver_code: 3-letter driver code (e.g., 'VER', 'HAM')
        
    Returns:
        dict: Driver statistics or None if not found
    """
    return DRIVER_STATS.get(driver_code.upper())

def get_all_drivers():
    """Get list of all driver codes"""
    return list(DRIVER_STATS.keys())