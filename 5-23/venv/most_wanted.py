"""
    Using the 'allMostWanted.json' file of FBI's most wanted, create an API server that will provide the following endpoints:

    /highbounty
        Find the 20 highest bounties from all the records and return for each record at least the bounty amount, the name of the person and an id.
    
    /details/<person_id>
        Provide a webpage of the details and picture(s) of the period for the id provided in a user-friendly way.
"""

from flask import Flask, request
import json

app = Flask(__name__)

with open("list.json", "r") as f


@app.route("/highbounty")
def search():
    return 