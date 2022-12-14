# CREATE STRICT DIFFERENTIATION BETWEEN FANTASY AND NHL TEAMS FOR VARIABLE/FUNCTION NAMES

import requests, json, time, os, pytz
import pprint as pp
from datetime import datetime
from dateutil import tz
from dataclasses import dataclass
import auth as xe

@dataclass
class FantasyTeam:
	# Team meta info
	id: int
	div: str
	abbr: str
	name: str

	# Team rank
	rank: int
	wins: int
	losses: int
	ties: int
	pts_for: int
	pts_against: int
	streak_len: int
	streak_type: str

	# Transactions
	acquisitions: int
	drops: int
	move_to_ir: int
	trades: int	

def main():
	# Get information on fantasy teams, including name, id, pts, etc.
	(f_team_info, f_meta_info) = get_league_info()

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')

		nhl_games = get_nhl_today()
		fantasy: dict[dict] = get_final_fantasy(f_team_info, f_meta_info) # type: ignore

		for f in fantasy["matchups"]: # type: ignore

			home = f["home"]
			away = f["away"]

			home_lo = f"{home['abbr']:5} {home['pts_week']:<5} (+{home['pts_today']:>5})"
			away_lo = f"{away['abbr']:5} {away['pts_week']:<5} (+{away['pts_today']:>5})"

			print(f"{away_lo} // {home_lo}")

		time.sleep(40)

def get_final_fantasy(fantasy_teams, meta):
	output = meta

	fantasy_matchup: dict = get_fantasy_today()
	matchups: list = []

	for entry in fantasy_matchup:
		if "rosterForCurrentScoringPeriod" in entry["home"]:
			home_id = entry["home"]["teamId"]
			home_pts_old = entry["home"]["totalPoints"]
			home_pts_live = entry["home"]["totalPointsLive"]

			home = next(filter(lambda x: x.id == home_id, fantasy_teams))

			away_id = entry["away"]["teamId"]
			away_pts_old = entry["away"]["totalPoints"]
			away_pts_live = entry["away"]["totalPointsLive"]

			away = next(filter(lambda x: x.id == away_id, fantasy_teams))

			this_matchup = {
				"home" : {
					"name": home.name,
					"abbr": home.abbr,
					"team_id": home.id,
					"division": home.div,
					"wins": home.wins,
					"losses": home.losses,
					"ties": home.ties,
					"rank": home.rank,
					"streak_len": home.streak_len,
					"streak_type": home.streak_type,
					"pts_up_to": home_pts_old,
					"pts_week": home_pts_live,
					"pts_today": f"{home_pts_live - home_pts_old:.1f}",
					"pts_for": f"{home.pts_for:.1f}",
					"pts_against": f"{home.pts_against:.1f}",
					"acquisitions": home.acquisitions,
					"drops": home.drops,
					"move_to_ir": home.move_to_ir,
					"trades": home.trades,
				},
				
				"away" : {
					"name": away.name,
					"abbr": away.abbr,
					"team_id": away.id,
					"division": away.div,
					"wins": away.wins,
					"losses": away.losses,
					"ties": away.ties,
					"rank": away.rank,
					"streak_len": away.streak_len,
					"streak_type": away.streak_type, 
					"pts_up_to": away_pts_old,
					"pts_week": away_pts_live,
					"pts_today": f"{away_pts_live - away_pts_old:.1f}",
					"pts_for": f"{away.pts_for:.1f}",
					"pts_against": f"{away.pts_against:.1f}",
					"acquisitions": away.acquisitions,
					"drops": away.drops,
					"move_to_ir": away.move_to_ir,
					"trades": away.trades,
				},
			}

			matchups.append(this_matchup)
		output["matchups"] = matchups

	return output


def get_nhl_today():
	url = "https://statsapi.web.nhl.com/api/v1/schedule?expand=schedule.linescore"
	games_req = requests.get(url)

	nhl_games_today = games_req.json()

	total_games = nhl_games_today["totalGames"]
	game_list = nhl_games_today["dates"][0]["games"]

	for game in game_list:
		status = game["status"]["detailedState"]
		time_utc = game["gameDate"]

		if game["status"]["abstractGameState"] == "Live":
			game_time = game["linescore"]["currentPeriodTimeRemaining"] 
			period = game["linescore"]["currentPeriodOrdinal"]

			if game_time == "END":
				temp = f"End {period}"
				game_status = f"{'Live':<12} {temp:>12}"
			else:
				game_status = f"{'Live':<12}{period} {game_time} Rem"

		elif game["status"]["abstractGameState"] == "FINAL":
			game_status = f"{'Final':<25}"

		else:
			d1 = datetime.strptime(time_utc,"%Y-%m-%dT%H:%M:%SZ")

			dt_utc = d1.replace(tzinfo=pytz.UTC)
			local_zone = tz.tzlocal()
			dt_local = dt_utc.astimezone(local_zone)
			game_time = dt_local.strftime("%I:%M %p")

			game_status = f"{status.upper():<14} @ {game_time}"
		
		home = game["teams"]["home"]["team"]["name"]
		home_id = game["teams"]["home"]["team"]["id"]
		home_abbr = xe.nhl_team_info[str(home_id)]["abbr"]
		home_pts = game["teams"]["home"]["score"]

		away = game["teams"]["away"]["team"]["name"]
		away_id = game["teams"]["away"]["team"]["id"]
		away_abbr = xe.nhl_team_info[str(away_id)]["abbr"]
		away_pts = game["teams"]["away"]["score"]

		print(f"{game_status} || {away_abbr} {away_pts}  v  {home_pts} {home_abbr}")

def get_fantasy_today():
	url = f"https://fantasy.espn.com/apis/v3/games/fhl/seasons/2023/segments/0/leagues/{xe.league_id}"
	mu_req = requests.get(url,
		params={'view': 'mMatchupScore'},
		cookies={
			'swid': xe.swid,
			'espn_s2': xe.espn_s2
		})

	print()
	return mu_req.json()['schedule']

def get_league_info():

	url = f"https://fantasy.espn.com/apis/v3/games/fhl/seasons/2023/segments/0/leagues/{xe.league_id}"
	team_req = requests.get(url,
		params={'view': 'mTeam'},
		cookies={
			'swid': xe.swid,
			'espn_s2': xe.espn_s2
		})

	print("Making request to team API")
	m_team_raw = team_req.json()

	team_list = []
	for t in m_team_raw['teams']:
		id = t["id"]
		div_id = t["divisionId"]
		abbr = t["abbrev"]
		name = t["name"].replace("  ", " ")

		rank = t["playoffSeed"]
		wins = t["record"]["overall"]["wins"]
		losses = t["record"]["overall"]["losses"]
		ties = t["record"]["overall"]["ties"]
		points_for = t["record"]["overall"]["pointsFor"]
		points_against = t["record"]["overall"]["pointsAgainst"]
		streak_len = t["record"]["overall"]["streakLength"]
		streak_type = t["record"]["overall"]["streakType"]

		acquisitions = t["transactionCounter"]["acquisitions"]
		drops = t["transactionCounter"]["drops"]
		move_to_ir = t["transactionCounter"]["moveToIR"]
		trades = t["transactionCounter"]["trades"]

		div = "East" if div_id == 0 else "West"
		streak_type = "Win streak" if streak_type == "WIN" else "Losing streak"

		this_team = FantasyTeam (id, div, abbr, name, rank, wins, losses, ties, points_for, points_against, streak_len, streak_type, acquisitions, drops, move_to_ir, trades)
		team_list.append(this_team)

	day = m_team_raw["scoringPeriodId"]
	this_week = m_team_raw["status"]["currentMatchupPeriod"]
	season = m_team_raw["seasonId"]

	meta_info = { "meta" : {
			"day": day,
			"week": this_week,
			"season": season
		}
	}

	return (team_list, meta_info)

if __name__ == '__main__':
    main();
