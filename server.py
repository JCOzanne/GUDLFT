import json

import pendulum
from flask import Flask, render_template, request, redirect, flash, url_for
from typing import List, Dict, Any


def loadClubs() -> List[Dict[str, Any]] :
    """
    Loads the list of club from clubs.json file
    :return: A list of clubs with their information.
    """
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions() -> List[Dict[str, Any]] :
    """
    Loads the list of competitions from competitions.json file
    :return: A list of competitions with their information.
    """
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    """
    Displays the home page.
    :return: HTML page
    """
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    """
    Displays the summary page after login.
    :return: HTML page with club details and competitions.
    """
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("email not found or invalid please try again")
        return redirect(url_for('index'))
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """
    Displays the booking page for a given competition and club.
    :param competition: The name of the competition.
    :param club: The name of the club.
    :return: HTML page with competition and club details.
    """
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    """
    Handles the purchase of competition places.
    :return: HTML page with booking status.
    """
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    competition_date = pendulum.parse(competition['date'])
    if competition_date < pendulum.now():
        flash('You cannot book places for a past competition !')
        return render_template('welcome.html', club=club, competitions=competitions)

    elif int(competition["numberOfPlaces"]) == 0:
        flash('The competition is over!')
        return render_template('welcome.html', club=club, competitions=competitions)
    elif placesRequired < 0:
        flash('You cannot book less than 0 places!')
        return render_template('welcome.html', club=club, competitions=competitions)
    elif placesRequired > int(club["points"]):
        flash ('You do not have enough points!')
        return render_template('welcome.html', club=club, competitions=competitions)
    elif placesRequired > 12:
        flash ('You cannot book more than 12 places!')
        return render_template('welcome.html', club=club, competitions=competitions)
    elif placesRequired > int(competition["numberOfPlaces"]):
        flash('You cannot book more than the available places!')
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        club['points'] = int(club['points']) - placesRequired
        flash(f"Great-booking complete! You booked {placesRequired} places.")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/clubPoints')
def clubPoints():
    """
    Displays the public table of club points.
    :return: HTML page with club points information.
    """
    return render_template('clubPoints.html', clubs=clubs)


@app.route('/logout')
def logout():
    """
    Logs the user out and redirects to the home page.
    :return: Redirects to the index page.
    """
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
