league_id = 0 # Fill in your league ID

# Fill this in if your league is private
swid = '' # cookie data here
espn_s2 = '' # cookie data here

nhl_team_info = {
    "1": {
        "full_name": "New Jersey Devils",
        "abbr": "NJD",
        "location": "New Jersey",
        "short_name": "Devils",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "2": {
        "full_name": "New York Islanders",
        "abbr": "NYI",
        "location": "New York",
        "short_name": "Islanders",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "3": {
        "full_name": "New York Rangers",
        "abbr": "NYR",
        "location": "New York",
        "short_name": "Rangers",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "4": {
        "full_name": "Philadelphia Flyers",
        "abbr": "PHI",
        "location": "Philadelphia",
        "short_name": "Flyers",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "5": {
        "full_name": "Pittsburgh Penguins",
        "abbr": "PIT",
        "location": "Pittsburgh",
        "short_name": "Penguins",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "6": {
        "full_name": "Boston Bruins",
        "abbr": "BOS",
        "location": "Boston",
        "short_name": "Bruins",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "7": {
        "full_name": "Buffalo Sabres",
        "abbr": "BUF",
        "location": "Buffalo",
        "short_name": "Sabres",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "8": {
        "full_name": "Montréal Canadiens",
        "abbr": "MTL",
        "location": "Montréal",
        "short_name": "Canadiens",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "9": {
        "full_name": "Ottawa Senators",
        "abbr": "OTT",
        "location": "Ottawa",
        "short_name": "Senators",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "10": {
        "full_name": "Toronto Maple Leafs",
        "abbr": "TOR",
        "location": "Toronto",
        "short_name": "Maple Leafs",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "12": {
        "full_name": "Carolina Hurricanes",
        "abbr": "CAR",
        "location": "Carolina",
        "short_name": "Hurricanes",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "13": {
        "full_name": "Florida Panthers",
        "abbr": "FLA",
        "location": "Florida",
        "short_name": "Panthers",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "14": {
        "full_name": "Tampa Bay Lightning",
        "abbr": "TBL",
        "location": "Tampa Bay",
        "short_name": "Lightning",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "15": {
        "full_name": "Washington Capitals",
        "abbr": "WSH",
        "location": "Washington",
        "short_name": "Capitals",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "16": {
        "full_name": "Chicago Blackhawks",
        "abbr": "CHI",
        "location": "Chicago",
        "short_name": "Blackhawks",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "17": {
        "full_name": "Detroit Red Wings",
        "abbr": "DET",
        "location": "Detroit",
        "short_name": "Red Wings",
        "division": "Atlantic",
        "division_short": "ATL",
        "conference": "Eastern"
    },
    "18": {
        "full_name": "Nashville Predators",
        "abbr": "NSH",
        "location": "Nashville",
        "short_name": "Predators",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "19": {
        "full_name": "St. Louis Blues",
        "abbr": "STL",
        "location": "St. Louis",
        "short_name": "Blues",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "20": {
        "full_name": "Calgary Flames",
        "abbr": "CGY",
        "location": "Calgary",
        "short_name": "Flames",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "21": {
        "full_name": "Colorado Avalanche",
        "abbr": "COL",
        "location": "Colorado",
        "short_name": "Avalanche",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "22": {
        "full_name": "Edmonton Oilers",
        "abbr": "EDM",
        "location": "Edmonton",
        "short_name": "Oilers",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "23": {
        "full_name": "Vancouver Canucks",
        "abbr": "VAN",
        "location": "Vancouver",
        "short_name": "Canucks",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "24": {
        "full_name": "Anaheim Ducks",
        "abbr": "ANA",
        "location": "Anaheim",
        "short_name": "Ducks",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "25": {
        "full_name": "Dallas Stars",
        "abbr": "DAL",
        "location": "Dallas",
        "short_name": "Stars",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "26": {
        "full_name": "Los Angeles Kings",
        "abbr": "LAK",
        "location": "Los Angeles",
        "short_name": "Kings",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "28": {
        "full_name": "San Jose Sharks",
        "abbr": "SJS",
        "location": "San Jose",
        "short_name": "Sharks",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "29": {
        "full_name": "Columbus Blue Jackets",
        "abbr": "CBJ",
        "location": "Columbus",
        "short_name": "Blue Jackets",
        "division": "Metropolitan",
        "division_short": "Metro",
        "conference": "Eastern"
    },
    "30": {
        "full_name": "Minnesota Wild",
        "abbr": "MIN",
        "location": "Minnesota",
        "short_name": "Wild",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "52": {
        "full_name": "Winnipeg Jets",
        "abbr": "WPG",
        "location": "Winnipeg",
        "short_name": "Jets",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "53": {
        "full_name": "Arizona Coyotes",
        "abbr": "ARI",
        "location": "Arizona",
        "short_name": "Coyotes",
        "division": "Central",
        "division_short": "CEN",
        "conference": "Western"
    },
    "54": {
        "full_name": "Vegas Golden Knights",
        "abbr": "VGK",
        "location": "Vegas",
        "short_name": "Golden Knights",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    },
    "55": {
        "full_name": "Seattle Kraken",
        "abbr": "SEA",
        "location": "Seattle",
        "short_name": "Kraken",
        "division": "Pacific",
        "division_short": "PAC",
        "conference": "Western"
    }
}

''' # ! Code to pull NHL team stats
import requests, json

req = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
raw = req.json()["teams"]

team_list = {}

for team in raw:
    temp = {
        "full_name": team["name"],                          # Colorado Avalanche
        "abbr": team["abbreviation"],                       # COL
        "location": team["locationName"],                   # Colorado
        "short_name": team["teamName"],                     # Avalanche
        "division": team["division"]["name"],               # Central
        "division_short": team["division"]["nameShort"],    # CEN
        "conference": team["conference"]["name"]            # Western
    }

    team_list[team["id"]] = temp
    
with open ("./teams.json", "w") as f:
    json.dump(team_list, f)'''
