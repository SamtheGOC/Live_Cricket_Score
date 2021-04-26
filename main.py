from win10toast import ToastNotifier
import requests
from bs4 import BeautifulSoup
from time import sleep


toaster = ToastNotifier()
a = 0


while a == 0:
    refresh_interval = 2 * 1000
    cricbuzz_url = 'https://www.cricbuzz.com/'
    page = requests.get(cricbuzz_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    teams = soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')
    team_scores = soup.find_all(class_='cb-ovr-flo')
    result_a = soup.find_all(class_='cb-ovr-flo cb-text-live')  # empty if no ongoing game
    result_b = soup.find_all(class_='cb-ovr-flo cb-text-complete')
    team1 = teams[0].get_text()
    team2 = teams[1].get_text()
    print(team1+' is playing against '+team2)


        #Put the values of ongoing matches' scores to the variables
    if not result_a:  # check if result_a is empty
        result_c2 = result_b[0].get_text()
        team1_score = team_scores[10].get_text()
        team2_score = team_scores[12].get_text()
        print(team1+ "'s current score : " + team1_score)
        print(team2+ "'s current score : " + team2_score)
        print('Result : ' + result_c2)


    else:
        result = result_a[0].get_text()
        team1_score = team_scores[8].get_text()
        team2_score = team_scores[10].get_text()
        t1_output = team1 + "'s current score : " + team1_score
        t2_output = team2 + "'s current score : " + team2_score
        print(team1 + "'s current score : " + team1_score)
        print(team2 + "'s current score : " + team2_score)
        print('Result : '+ result)
        toaster.show_toast(result, t1_output + '\n' + t2_output, duration=10)
        sleep(10)