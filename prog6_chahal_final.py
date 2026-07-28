## Major: Computer Science ##

## Creation Date: November 26th, 2024 ##

## Due Date: December 6th, 2024 ##

## Course: CS115-02 ##

## Professor Name: Professor Shimkanon ##

## Assignment: 6 ##

## Filename: prog6_chahal_final.py ##

## Purpose: This program will organize the 23/24 LaLiga league dataset, ##
## namely table statistics, team statsistics, and player statistics, ##  
## with the objective to find trends in top teams. ##

## Dataset Source: https://www.kaggle.com/datasets/whisperingkahuna/la-liga-202324-players-and-team-insights?select=files_descriptions.csv ##

##############################################################

# ----- FILE IMPORTS ----- #
import csv
import pandas as pd

table_df = pd.read_csv('Laliga_table_2023_24.csv')
home_df = pd.read_csv('Laliga_table_home_2023_24.csv') 
away_df = pd.read_csv('Laliga_table_away_2023_24.csv') 


interceptions_df = pd.read_csv('interception_team.csv') 
clearances_df = pd.read_csv('effective_clearance_team.csv') 
clean_sheets_df = pd.read_csv('clean_sheet_team.csv')
goals_df = pd.read_csv('team_goals_per_match.csv')
pass_accuracy_df = pd.read_csv('accurate_pass_team.csv') 
possession_df = pd.read_csv('possession_percentage_team.csv')
tackles_df = pd.read_csv('won_tackle_team.csv')
team_ratings_df = pd.read_csv('team_ratings.csv')

player_assists_df = pd.read_csv('player_top_assists.csv')
player_clean_sheets_df = pd.read_csv('player_clean_sheets.csv')
player_clearances_df = pd.read_csv('player_effective_clearances.csv')
player_dribbles_df = pd.read_csv('player_contests_won.csv')
player_goals_df = pd.read_csv('player_top_scorers.csv') 
player_interceptions_df = pd.read_csv('player_interceptions.csv')
player_pass_accuracy_df = pd.read_csv('player_accurate_passes.csv')
player_tackles_df = pd.read_csv('player_tackles_won.csv')
player_ratings_df = pd.read_csv('player_player_ratings.csv')
# ----- FILE IMPORTS ----- #

###############################################################
## Function Name: league_table                               ##
##                                                           ##
## Description:   This function returns user's desired table ##
##                statistic of LaLiga (table_aspect)         ##
##                                                           ##
## Parameters:    csv: table_df,home_df, away_df             ##
##                                                           ##   
## Return Value:  Dataframe of input tabe_aspect:            ##
##                entire table, home table, or away table    ##
###############################################################
def league_table(table_df, home_df, away_df):
   
   # Loop start
   while True:
        table_aspect = input('\nAny specific table aspect?:'
                               '\n-Entire Table'
                               '\n-Home Table'
                               '\n-Away Table'
                               '\ntype "back" to return to main menu.'
                               '\n\nI would like to see: ' )
        
        # Takes user back to main menu
        if table_aspect.lower() == 'back': 
            break 
        
        # Returns complete standings
        elif table_aspect.lower() == 'entire table':
            print('\n23/24 LaLiga Final Table Standings:')
            return table_df.to_string(index=False)
        
        # Return home table standings
        elif table_aspect.lower() == 'home table':
            print('\n23/24 LaLiga Final Home Records:')
            return home_df.to_string(index=False)
        
        # Returns away table standings
        elif table_aspect.lower() == 'away table':
            print('\n23/24 LaLiga Final Away Records:')
            return away_df.to_string(index=False)
        
        else:
            print('\nInvalid option. Please try again.')
            
###############################################################
## Function Name: team_stats                                 ##
##                                                           ##
## Description:   This function returns a table of the       ##
##                user's desired team statistic of LaLiga    ##
##                (team_option)                              ##
##                                                           ## 
## Parameters:    csv: clean_sheets_df,clearances_df,goals_df##
##                ,interceptions_df,pass_accuracy_df,        ##
##                possession_df,tackles_df,team_ratings_df   ##
##                                                           ##
## Return Value:  Dataframe of input attcking_aspect:        ##
##                clean sheets,clearances,goals,             ##
##                interceptions,pass accuracy,possession,    ##
##                tackles,team ratings                       ##
###############################################################            
def team_stats(clean_sheets_df,clearances_df,goals_df,interceptions_df,pass_accuracy_df,
               possession_df,tackles_df,team_ratings_df):
    
    # Loop start
    while True:
        team_choice = input('\nWhat team statistic would you like to see?:'
                            '\n- Clean Sheets'
                            '\n- Clearances'
                            '\n- Goals'
                            '\n- Interceptions'
                            '\n- Pass Accuracy'
                            '\n- Possession'
                            '\n- Tackles'
                            '\n- Team Ratings'
                            '\ntype "back" to return to main menu.'
                            '\n\nI would like to see: ')
        
        # Takes user back to main menu
        if team_choice.lower() == 'back':
            break
        
        # Returns team clean sheets
        elif team_choice.lower() == 'clean sheets':
            print('\n23/24 LaLiga Team Clean Sheets')
            return clean_sheets_df.drop(columns=['Country']).to_string(index=False)
        
        # Returns team clearances
        elif team_choice.lower() == 'clearances':
            print('\n23/24 LaLiga Team Effective Clearances:')
            return clearances_df.drop(columns=['Country']).to_string(index=False)
        
        # Returns team goals
        elif team_choice.lower() == 'goals':
            print('\n23/24 LaLiga Team Goals:')
            return goals_df.drop(columns=['Country']).to_string(index=False)
        
        # Returns team interceptions
        elif team_choice.lower() == 'interceptions':
            print('\n23/24 LaLiga Team Ball Interceptions:')
            return interceptions_df.drop(columns=['Country']).to_string(index=False) 
        
        # Returns team passing accuracy
        elif team_choice.lower() == 'pass accuracy':
            print('\n23/24 LaLiga Team Passing Accuracy:')
            return pass_accuracy_df.drop(columns=['Country']).to_string(index=False)
        
        # Returns team possession percentage
        elif team_choice.lower() == 'possession':
            print('\n23/24 LaLiga Possession Percentage:')
            return possession_df.drop(columns=['Country']).to_string(index=False)
        
        # Returns successful tackles
        elif team_choice.lower() == 'tackles':
            print('\n23/24 LaLiga Team Successful Tackles:')
            return tackles_df.drop(columns=['Country']).to_string(index=False)
        
        # Returns average team ratings
        elif team_choice.lower() == 'team ratings':
            print('\n23/24 LaLiga Average Team Ratings:')
            return team_ratings_df.drop(columns=['Country']).to_string(index=False)
        
        else:
            print('\nInvalid option. Please try again.')
            
###############################################################
## Function Name: player_stats                               ##
##                                                           ##
## Description:   This function returns user's desired player##
##                statistic of LaLiga                        ##
##                (player_choice)                            ##
##                                                           ##
## Parameters:    csv: player_assists_df,                    ##
##                player_clean_sheets_df,player_clearances_df##
##                ,player_dribbles_df,player_goals_df,       ##
##                player_interceptions_df,player_tackles_df, ##
##                player_ratings_d                           ##
##                                                           ##
## Return Value:  Dataframe of input player_choice: assists, ##
##                dribbles,clean sheets,clearances,goals,    ##
##                interceptions,pass accuracy,tackles        ##
##                player ratings                             ##
###############################################################
def player_stats(player_assists_df,player_clean_sheets_df,
                 player_clearances_df,player_dribbles_df,player_goals_df,
                 player_interceptions_df,player_tackles_df,player_ratings_df):
   
    # Loop start
    while True:
        player_choice = input('\nWhat player statistic would you like to see?:'
                              '\n- Assists'
                              '\n- Dribbles'
                              '\n- Clean Sheets'
                              '\n- Clearances'
                              '\n- Goals'
                              '\n- Interceptions'
                              '\n- Pass Accuracy'
                              '\n- Tackles'
                              '\n- Player Ratings'
                              '\ntype "back" to return to main menu.'
                              '\n\nI would like to see: ')
        
        # Takes user back to main menu
        if player_choice.lower() == 'back':
            break
        
        # Returns player assists
        elif player_choice.lower() == 'assists':
            print('\n23/24 LaLiga Player Assists')
            return player_assists_df.to_string(index=False)
        
        # Returns player successful dribbles
        elif player_choice.lower() == 'dribbles':
            print('\n23/24 LaLiga Successful Dribbles')
            return player_dribbles_df.to_string(index=False)
        
        # Returns player clean sheets
        elif player_choice.lower() == 'clean sheets':
            print('\n23/24 LaLiga Player (Goalkeeper) Clean Sheets:')
            return player_clean_sheets_df.to_string(index=False)
        
        # Returns player effective clearances
        elif player_choice.lower() == 'clearances':
            print('\n23/24 LaLiga Player Effective Clearances:')
            return player_clearances_df.to_string(index=False)
        
        # Returns player successful dribbles
        elif player_choice.lower() == 'successful dribbles':
            print('\n23/24 LaLiga Player Successful Dribbles')
            return player_dribbles_df.to_string(index=False)

        # Returns player goals 
        elif player_choice.lower() == 'goals':
            print('\n23/24 LaLiga Player Goals:')
            return player_goals_df.to_string(index=False)
        
        # Returns player interceptions
        elif player_choice.lower() == 'interceptions':
            print('\n23/24 LaLiga Player Interceptions:')
            return player_interceptions_df.to_string(index=False)
        
        # Returns player pass accuracy
        elif player_choice.lower() == 'pass accuracy':
            print('\n23/24 LaLiga Player Pass Accuracy:')
            return player_pass_accuracy_df.to_string(index=False)
        
      
        # Returns player successful tackles 
        elif player_choice.lower() == 'tackles':
            print('\n23/24 LaLiga Player Successful Tackles:')
            return player_tackles_df.to_string(index=False)
        
        # Returns average player ratings
        elif player_choice.lower() == 'player ratings':
            print('\n23/24 LaLiga Average Player Ratings:')
            return player_ratings_df.to_string(index=False)
        
        else:
            print('\nInvalid option. Please try again.')
                
if __name__ == '__main__':
    
    # Loop start
    while True:
        option = input('\nWhat LaLiga statistic would you like to see?:'
                       '\n- Table Statistics (Table)'
                       '\n- Team Statistics (Team)'
                       '\n- Player Statistics (Player)'
                       '\n\nI would like to see: ')

        # Table option
        if option.lower() == 'table statistics' or option.lower() == 'table':
            print(league_table(table_df, home_df, away_df))
        
        # Team option
        elif option.lower() == 'team statistics' or option.lower() == 'team':
            print(team_stats(clean_sheets_df,clearances_df,goals_df,interceptions_df,
                             pass_accuracy_df,possession_df,tackles_df,team_ratings_df))
            
        # Player option
        elif option.lower() == 'player statistics' or option.lower() == 'player':
            print(player_stats(player_assists_df,player_clean_sheets_df,
                               player_clearances_df,player_dribbles_df,player_goals_df,
                               player_interceptions_df,player_tackles_df,player_ratings_df))

        else:
            print('\nInvalid option. Please try again.')