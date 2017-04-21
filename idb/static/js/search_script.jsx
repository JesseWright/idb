
var terms = "default";
var cur_page = 1;
var max_page = 1;

$('#searchForm').submit(function () {
    search_text = document.getElementById("searchBox").value
    window.location.href = ("/search_results/" + search_text);
    //keeps the page from reloading
    return false;
});

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
              'type': 'default'
          };
      },
      render: function() {
          var link_to_use = ""+ this.props.link + this.props.id;
          return(
                  <div className = "row">
                    <a href = {link_to_use}>
                        <div className = "idb-result-card">
                          <h1><b>{this.props.name}</b> - ({this.props.type})</h1>
                          <h4><i>context will go here</i></h4>
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
    if (prev_page !== cur_page)
        update_results(cur_page);
    else
        console.log("Tried to go to invalid page!");
    window.scrollTo(0,0);
}


var load = function(){
    $("#loadingDiv").hide();
    terms = document.getElementById("termsDiv").innerHTML;
    document.getElementById("termText").innerHTML = ('Showing results for "' + terms + '"');
    ReactDOM.render(
        React.createElement(page_ident, {page_num:1,max_page_num:1 }, null),
        document.getElementById('page-identifier')
    );
    update_results(0);
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
    var url = "/search/?term=" + terms + "&page=" + page;
    console.log(url);
    $.get(url,function(data,status)
    {



        if(status == 'success')
        {
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
            for(i = 0; i < data.data.length; i++)
            {
                d = data.data[i]
                if(d.type == "Artist") //artist
                {
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/artist/",id:d.id,type:d.type}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
                else if(d.type == "Medium") //medium
                {
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/media/",id:d.id,type:d.type}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
                else //work
                {
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/work/",id:d.id,type:d.type}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
            }
            max_page = data.pages;
            ReactDOM.render(
                React.createElement(page_ident, {page_num:cur_page,max_page_num:max_page }, null),
                document.getElementById('page-identifier')
            );
        }
        else
        {
            console.log("Server responded with error code, sorry.");
        }


    });

}
