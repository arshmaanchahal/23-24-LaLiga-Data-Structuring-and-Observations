# 23/24 LaLiga Data Structure and Observations

## Description
Since its inception in 1929, LaLiga has only had 9 different champions, with Real Madrid (36 titles), FC Barcelona (27 titles), and Atletico Madrid (11 titles) combining for 74 of the 93 titles ever awarded. This project was built to explore trends and patterns behind that dominance by organizing and analyzing the 2023/2024 LaLiga season's table, team, and player statistics.

The program uses pandas to load and organize a collection of CSV datasets covering final standings (overall, home, and away), team-level statistics (clean sheets, effective clearances, goals, interceptions, pass accuracy, possession, tackles, and team ratings), and player-level statistics (assists, dribbles, clean sheets, clearances, goals, interceptions, pass accuracy, tackles, and player ratings). Since all teams in the dataset are Spanish, the redundant "Country" column was dropped from the team-level data frames for readability.

Given the large amount of data available, a text-based user interface was built so a user can choose exactly what they want to see: table statistics, team statistics, or player statistics. Selecting a category prompts the user for the specific stat they're interested in, then returns the corresponding data frame for review.

## Key Findings
* Real Madrid finished atop every table (entire, home, and away), ending the season with a 29-5-1 record and 95 points, staying undefeated at home and suffering only a single loss on the road. The top 4 finishers were Real Madrid, FC Barcelona, Girona, and Atletico Madrid.
* Real Madrid led the league in clean sheets, goals scored, and passing accuracy — but top teams were often only average or below average in defensive stats like tackles, clearances, and interceptions, despite conceding the fewest goals overall.
* Possession and passing did not always favor the top teams: Las Palmas, who finished 16th in the league, ranked 2nd in ball possession (ahead of possession-focused champions Real Madrid) and 3rd in accurate passes per match, ahead of clubs like Atletico Madrid and Girona.
* Individual player rankings frequently favored players from mid- or bottom-table teams over players from the league's top clubs — for example, Villarreal's Ilias Akhomach (8th-place finish) ranked 2nd in successful dribbles, ahead of Real Madrid's Vinicius Jr., who finished 6th in that category. Player passing accuracy was the one individual stat that consistently favored players from top teams.
* Overall, the data suggests that controlling possession and disciplined passing — rather than individual standout performances — are what most consistently separate LaLiga's top teams from the rest of the league, by limiting opposition chances and converting that control into clean sheets and points.

## Data
* **La Liga 2023/24: Team & Player Stats** by Karman Ali, via [Kaggle](https://www.kaggle.com/datasets/whisperingkahuna/la-liga-202324-players-and-team-insights)

## Languages and Utilities Used
* Python
* pandas
* csv

## Environments Used
* Visual Studio Code

## Author
Arshmaan Chahal
