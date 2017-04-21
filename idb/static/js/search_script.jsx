
var terms = "default";
var cur_page = 1;
var max_page = 1;

$('#searchForm').submit(function () {
    search_text = document.getElementById("searchBox").value
    window.location.href = ("/search_results/" + search_text);
    //keeps the page from reloading
    return false;
});

var load = function(){
    $("#loadingDiv").hide();
    terms = document.getElementById("termsDiv").innerHTML;
    document.getElementById("termText").innerHTML = ('Showing results for "' + terms + '"');
    ReactDOM.render(
        React.createElement(page_ident, {page_num:1,max_page_num:1 }, null),
        document.getElementById('page-identifier')
    );
    update_results(cur_page);
}

var page_ident = React.createClass({
        getDefaultProps: function(){
            return {
                'page_num': 1
            };
        },
        render: function() {
          return (<div>{this.props.page_num}/{this.props.max_page_num}</div>);
      }
      });

var no_results_card = React.createClass({
      render: function() {
        return (
            <div className = "idb-no-results-card">
                Sorry, there are no results for your search.
                <div className= "idb-maybe-text">Maybe try something else?</div>
            </div>);
    }
    });

var result_row = React.createClass({
      getDefaultProps: function(){
          return {
              'name': "default",
              'id': 1,
              'link': "/null/",
              'type': 'default',
              'context': "default_context"
          };
      },
      render: function() {
          var link_to_use = ""+ this.props.link + this.props.id;
          return(
                  <div className = "row">
                    <a href = {link_to_use}>
                        <div className = "idb-result-card">
                          <h1><b>{this.props.name}</b> - ({this.props.type})</h1>
                          <h4><i>{this.props.context}</i></h4>
                        </div>
                    </a>
                  </div>
          );
      }
    });

function handle_page_change(isPrev)
{

    var prev_page = cur_page;
    if (isPrev)
    {
        if (cur_page != 1)
        {
            cur_page = cur_page - 1;
        }
    }
    else
    {
        if(cur_page + 1 <= max_page)
            cur_page = cur_page + 1;
    }
    if (prev_page !== cur_page){
        console.log("cur "+ cur_page);
        update_results(cur_page);

    }
    else
        console.log("Tried to go to invalid page!");
    window.scrollTo(0,0);
}


$(document)
  .ajaxStart(function () {
    $("#loadingDiv").show();
  })
  .ajaxStop(function () {
    $("#loadingDiv").hide();
  });

$(document).ready(load);

function update_results(page)
{
    console.log(page);
    var url = "/search/?term=" + terms + "&page=" + (page-1);
    console.log(url);
    $.get(url,function(data,status)
    {



        if(status == 'success')
        {
            //console.log(data.data.length);
            console.log(data.pages);
            if(data.data.length == 0)
            {
                ReactDOM.render(
                    React.createElement(no_results_card, null, null),
                    document.getElementById("noResultsContainer")
                );
            }
            else {
                ReactDOM.render(
                    React.createElement('div', null, null),
                    document.getElementById("noResultsContainer")
                );
            }
            for(var i = 0; i < data.data.length; i++)
            {
                d = data.data[i]
                if(d.type == "Artist") //artist
                {
                    terms_context = search_model_for_context(d.type,d.object);
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/artist/",id:d.id,type:d.type,context:terms_context}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
                else if(d.type == "Medium") //medium
                {
                    terms_context = search_model_for_context(d.type,d.object);
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/media/",id:d.id,type:d.type,context:terms_context}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
                else //work
                {
                    terms_context = search_model_for_context(d.type,d.object);
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/work/",id:d.id,type:d.type,context:terms_context}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
            }
            max_page = data.pages;
            ReactDOM.render(
                React.createElement(page_ident, {page_num:cur_page,max_page_num:max_page }, null),
                document.getElementById('page-identifier')
            );
            $('i').wrapInTag({"words":terms.split(" ")});
        }
        else
        {
            console.log("Server responded with error code, sorry.");
        }


    });

}


function search_model_for_context(type,model)
{
    var ret_string = "";
    search_terms = document.getElementById("termsDiv").innerHTML.split(" ");
    if(type == "Artist")
    {
        for(var index = 0; index < search_terms.length; index++)
        {
            term = search_terms[index].toLowerCase();
            if(model.name && model.name.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in name: " + model.name + " ";
            if(model.nationality && model.nationality.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in nationality: " + model.nationality + " ";
            if(model.country && model.country.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in country: "+ model.country + " ";
            if(model.bio && model.bio.toLowerCase().indexOf(term) !== -1)
                ret_string += "in bio: " + model.bio.substring(model.bio.toLowerCase().indexOf(term),model.bio.toLowerCase().indexOf(term)+20) + "";
        }
    }
    else if(type == "Medium")
    {
        for(var index = 0; index < search_terms.length; index++)
        {
            term = search_terms[index].toLowerCase();
            if(model.name && model.name.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in name: " + model.name + " ";
            if(model.countries && model.countries.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in countries: "+ model.countries + " ";
        }
    }
    else
    {
        for(var index = 0; index < search_terms.length; index++)
        {
            term = search_terms[index].toLowerCase();
            if(model.title && model.title.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in title: " + model.title + " ";
            if(model.motifs && model.motifs.toLowerCase().indexOf(term) !== -1)
                ret_string+= "in motifs: " + model.motifs + " ";

        }
    }

    if(ret_string !== "")
        return "Found the search terms " + ret_string;
    else
        return "no context?";
}

// http://stackoverflow.com/a/9795091
$.fn.wrapInTag = function (opts) {
    // http://stackoverflow.com/a/1646618
    function getText(obj) {
        return obj.textContent ? obj.textContent : obj.innerText;
    }

    var tag = opts.tag || 'strong',
        words = opts.words || [],
        regex = RegExp(words.join('|'), 'gi'),
        replacement = '<' + tag + '>$&</' + tag + '>';

    // http://stackoverflow.com/a/298758
    $(this).contents().each(function () {
        if (this.nodeType === 3) //Node.TEXT_NODE
        {
            // http://stackoverflow.com/a/7698745
            $(this).replaceWith(getText(this).replace(regex, replacement));
        }
        else if (!opts.ignoreChildNodes) {
            $(this).wrapInTag(opts);
        }
    });
};
