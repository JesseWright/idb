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
def url_query_artist():
    artists, page_count  = query_artist(request.args.to_dict())
    serialized_models = list(map(lambda x: x.serialize(), artists))
    return response(200, serialized_models, page_count)

@app.route("/query_work")
def url_query_work():
    works, page_count  = query_work(request.args.to_dict())
    serialized_models = list(map(lambda x: x.serialize(), works))
    for work in serialized_models:
        work["height"] = str(work["height"])
        work["width"] = str(work["width"])
        work["depth"] = str(work["depth"])
    return response(200, serialized_models, page_count)

@app.route("/query_medium")
def url_query_medium():
    media, page_count  = query_medium(request.args.to_dict())
    serialized_models = list(map(lambda x: x.serialize(), media))
    return response(200, serialized_models, page_count)

def query_artist(args):
    artists = Artist.query
    if "order_by" in args and args["order_by"]:
        if args["order_by"] == "name" or  args["order_by"] == "dob":
            artists = artists.order_by(args["order_by"])
    artists = artists.all()
    if "name_filter" in args and args["name_filter"]:
        artists = string_filter(artists, "name", args["name_filter"])
    if "date_after" in args and args["date_after"]:
        artists = date_filter(artists, lambda x : x > int(args["date_after"]), "dob")
    if "date_before" in args and args["date_before"]:
        artists = date_filter(artists, lambda x : x < int(args["date_before"]), "dob")
    if "ascending" in args and args["ascending"] == "0":
        artists = artists[::-1]

    page_count = int(ceil(len(artists) / float(ITEMS_PER_PAGE)))

    if "page" in args and args["page"]:
        artists = artists[int(args["page"]) * ITEMS_PER_PAGE : (int(args["page"]) + 1) * ITEMS_PER_PAGE]

    return artists, page_count

def query_work(args):
    works = Work.query
    if "order_by" in args and args["order_by"]:
        if args["order_by"] == "title" or  args["order_by"] == "date":
            works = works.order_by(args["order_by"])
    works = works.all()
    if "name_filter" in args and args["name_filter"]:
        works = string_filter(works, "title", args["name_filter"])
    if "date_after" in args and args["date_after"]:
        works = date_filter(works, lambda x : x > int(args["date_after"]), "date")
    if "date_before" in args and args["date_before"]:
        works = date_filter(works, lambda x : x < int(args["date_before"]), "date")
    if "ascending" in args and args["ascending"] == "0":
        works = works[::-1]

    page_count = int(ceil(len(works) / float(ITEMS_PER_PAGE)))

    if "page" in args and args["page"]:
        works = works[int(args["page"]) * ITEMS_PER_PAGE : (int(args["page"]) + 1) * ITEMS_PER_PAGE]

    return works, page_count

def query_medium(args):
    works = Medium.query
    if "order_by" in args and args["order_by"]:
        if args["order_by"] == "name" or  args["order_by"] == "date":
            works = works.order_by(args["order_by"])
    works = works.all()
    if "name_filter" in args and args["name_filter"]:
        works = string_filter(works, "title", args["name_filter"])
    if "date_after" in args and args["date_after"]:
        works = date_filter(works, lambda x : x > int(args["date_after"]), "date")
    if "date_before" in args and args["date_before"]:
        works = date_filter(works, lambda x : x < int(args["date_before"]), "date")
    if "ascending" in args and args["ascending"] == "0":
        works = works[::-1]



    page_count = int(ceil(len(works) / float(ITEMS_PER_PAGE)))

    if "page" in args and args["page"]:
        works = works[int(args["page"]) * ITEMS_PER_PAGE : (int(args["page"]) + 1) * ITEMS_PER_PAGE]

    return works, page_count

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
