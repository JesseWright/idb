# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

import re
from math import ceil
from flask import render_template, request, jsonify
from idb import app
from idb.models import *

ITEMS_PER_PAGE = 16

def response(status, data, pages):
    ret = {"status":status,"pages":pages,"data":data}
    return jsonify(ret)

@app.route("/query_artist")
def query_artist():
    args = request.args.to_dict()

    artists = Artist.query
    if "order_by" in args:
        if args["order_by"] == "name" or  args["order_by"] == "dob":
            artists = artists.order_by(args["order_by"])
    artists = artists.all()
    if "name_filter" in args:
        artists = string_filter(artists, "name", args["name_filter"])
    if "date_after" in args:
        artists = date_filter(artists, lambda x : x > int(args["date_after"]), "dob")
    if "date_before" in args:
        artists = date_filter(artists, lambda x : x < int(args["date_before"]), "dob")

    if "ascending" in args and args["ascending"] == "0":
        artists = artists[::-1]

    page_count = int(ceil(len(artists) / float(ITEMS_PER_PAGE)))


    if "page" in args:
        artists = artists[int(args["page"]) * ITEMS_PER_PAGE : (int(args["page"]) + 1) * ITEMS_PER_PAGE]

    serialized_models = list(map(lambda x: x.serialize(), artists))

    return response(200, serialized_models, page_count)

def date_filter(models, func, attribute):
    filtered = []
    for model in models:
        try:
            if func(getattr(model, attribute).year):
                filtered.append(model)
        except:
            pass
    return filtered

def string_filter(models, attribute, search_string):
    print attribute, search_string
    if not search_string:
        return models
    return list(filter(lambda x : x.__dict__[attribute] is not None and x.__dict__[attribute].find(search_string) != -1, models))
