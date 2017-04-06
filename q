[1mdiff --git a/idb/queries.py b/idb/queries.py[m
[1mindex 2fc75b0..b102b39 100644[m
[1m--- a/idb/queries.py[m
[1m+++ b/idb/queries.py[m
[36m@@ -15,9 +15,13 @@[m [mdef response(status, data, pages):[m
     return jsonify(ret)[m
 [m
 @app.route("/query_artist")[m
[31m-def query_artist():[m
[31m-    args = request.args.to_dict()[m
[32m+[m[32mdef url_query_artist():[m
[32m+[m[32m    artists, page_count  = query_artist(request.args.to_dict())[m
[32m+[m[32m    serialized_models = list(map(lambda x: x.serialize(), artists))[m
[32m+[m[32m    return response(200, serialized_models, page_count)[m
 [m
[32m+[m
[32m+[m[32mdef query_artist(args):[m
     artists = Artist.query[m
     if "order_by" in args and args["order_by"]:[m
         if args["order_by"] == "name" or  args["order_by"] == "dob":[m
[36m@@ -29,19 +33,15 @@[m [mdef query_artist():[m
         artists = date_filter(artists, lambda x : x > int(args["date_after"]), "dob")[m
     if "date_before" in args and args["date_before"]:[m
         artists = date_filter(artists, lambda x : x < int(args["date_before"]), "dob")[m
[31m-[m
     if "ascending" in args and args["ascending"] == "0":[m
         artists = artists[::-1][m
 [m
     page_count = int(ceil(len(artists) / float(ITEMS_PER_PAGE)))[m
 [m
[31m-[m
     if "page" in args and args["page"]:[m
         artists = artists[int(args["page"]) * ITEMS_PER_PAGE : (int(args["page"]) + 1) * ITEMS_PER_PAGE][m
 [m
[31m-    serialized_models = list(map(lambda x: x.serialize(), artists))[m
[31m-[m
[31m-    return response(200, serialized_models, page_count)[m
[32m+[m[32m    return artists, page_count[m
 [m
 def date_filter(models, func, attribute):[m
     filtered = [][m
