from flask import render_template
from idb import app
from idb.models import *
from idb.queries import *
import subprocess
import time


@app.route('/')
def index():
    """Default route that renders the homepage using
    the template 'index.html'
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """Route to render our about page."""
    return render_template('about.html')


@app.route('/report')
def report():
    """Route to render the report page, although the actual report HTML
    is in 'report_text.html' and is rendered in an iFrame.
    """
    return render_template('report.html')


@app.route('/artists')
def artists():
    artists = Artist.query.all()
    first_page = artists[0:16]
    return render_template('artists.html', artists=first_page)


@app.route('/works')
def works():
    works = Work.query.all()
    first_page = works[0:16]
    return render_template('works.html', works=first_page)


@app.route('/eras')
def eras():
    images = []
    eras = Era.query.all()
    for era in eras:
        if era.works:
            images.append(era.works[0])
        else:
            images.append(None)
            # images = [if era.works: era.works[0].image for era in eras]
    return render_template('eras.html', eras=eras, images=images)


@app.route('/media')
def media():
    media = Medium.query.all()
    first_page = media[0:16]
    return render_template('media.html', media=first_page)


@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


@app.route('/artist/<int:id>')
def artist(id):
    artist = Artist.query.filter_by(id=id).first()

    works = []
    media = []
    for i in range(len(artist.works)):
        if i > 5:
            break
        works.append(artist.works[i])
    for j in range(len(artist.media)):
        if j > 5:
            break
        media.append(artist.media[j])

    return render_template('artist_instance.html', artist=artist, works=works,
                           media=media)


@app.route('/work/<int:id>')
def work(id):
    work = Work.query.filter_by(id=id).first()
    if work.colors:
        colors = work.colors.replace("{", "") \
            .replace("}", "").replace("'", "").split(",")
    else:
        colors = None
    artists = []
    for i in range(min(5, len(work.artists))):
        artists.append(work.artists[i])
    len_dict = {}
    if colors:
        len_dict['colors'] = len(colors)
    else:
        len_dict['colors'] = 1
    len_dict['media'] = len(work.media)
    if work.image:
        work._image = work.image.replace("{", "") \
            .replace("}", "").replace("'", "").split(",")[0]
    else:
        work._image = None
    return render_template('work_instance.html', work=work, artists=artists,
                           colors=colors, lendict=len_dict)


@app.route('/eras/<int:id>')
def era(id):
    era = Era.query.filter_by(id=id).first()
    if era.countries:
        countries = era.countries \
            .replace("{", "").replace("}", "").replace("'", "").split(",")
    else:
        countries = None
    works = []
    media = []
    artists = []
    for i in range(len(era.works)):
        if i > 5:
            break
        works.append(era.works[i])
    for j in range(len(era.media)):
        if j > 5:
            break
        media.append(era.media[j])
    for k in range(len(era.artists)):
        if k > 5:
            break
        artists.append(era.artists[k])
    return render_template('era_instance.html', era=era, countries=countries,
                           works=works, media=media, artists=artists)


@app.route('/media/<int:id>')
def medium(id):
    medium = Medium.query.filter_by(id=id).first()
    medium._image = medium.images.replace("{", "") \
        .replace("}", "").replace("'", "")

    if len(medium.colors) > 6:
        colors = medium.colors \
            .replace("{", "").replace("}", "").replace("'", "").split(",")
    else:
        colors = None

    return render_template('medium_instance.html', medium=medium,
                           colors=colors)

@app.route('/search_results/<terms>')
def search_results(terms):
    return render_template('search_results.html',terms=terms)

@app.route('/search/')
def search():
    total_start = time.time()
    ITEMS_PER_PAGE = 16
    args = request.args.to_dict()

    # seperate search terms into words
    search_terms = args["term"].split(" ")
    # filter out empty strings
    search_terms = list(filter(lambda x : x, search_terms))
    print("searching for ", end="")
    print(search_terms)

    # collect all objects from each model
    results = []
    print("collecting models... ", end="")
    for model in [Artist, Work, Medium, Era]:
        results += model.query.all()
    print("collected {} models.".format(len(results)))

    # transform results into more basic structures
    print("transforming... ", end="")
    start = time.time()
    results = list(map(lambda x : {
        "name"      : x.title if isinstance(x, Work) else x.name,
        "id"        : x.id,
        "type"      : type(x).__name__,
        "relevance" : x.relevance(search_terms),
        "object"    : x.serialize()
    }, results))
    print("transformed. {} models. {} seconds elapsed."
          .format(len(results), time.time() - start))

    # filter out items with 0 relevance
    print("filtering... ", end="")
    start = time.time()
    results = list(filter(lambda x : x["relevance"] > 1, results))
    print("filtered. {} models. {} seconds elapsed."
          .format(len(results), time.time() - start))

    # sort items by relevance
    print("sorting... ", end="")
    start = time.time()
    results = sorted(results, key=lambda x : x["relevance"], reverse=True)
    print("sorted. {} seconds elapsed.".format(time.time() - start))

    # page count method from query.py
    page_count = int(ceil(len(results) / float(ITEMS_PER_PAGE)))
    if "page" in args and args["page"]:
        results = results[int(args["page"]) * ITEMS_PER_PAGE : (int(
            args["page"]) + 1) * ITEMS_PER_PAGE]

    # serialize and return the results
    #results = list(map(lambda x : x.serialize(), results))
    end = time.time()
    print("Total elapsed time: " + str((end-total_start)) + " seconds.")
    return response(200, results, page_count)


@app.route('/report_text')
def report_text():
    return render_template('report_text.html')


@app.route('/getResults/tests/')
def tests():
    sb = subprocess.check_output(['python', '-m', 'unittest', 'idb.models'],
                                 stderr=subprocess.STDOUT).decode("utf-8")
    print(sb)
    return sb

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
