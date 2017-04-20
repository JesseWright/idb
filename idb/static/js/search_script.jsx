
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

var result_row = React.createClass({
      getDefaultProps: function(){
          return {
              'name': "default",
              'id': 1,
              'link': "/null/"
          };
      },
      render: function() {
          var link_to_use = ""+ this.props.link + this.props.id;
          return(
              <a href = {link_to_use}>
                  <div className = "row">
                      <h1>{this.props.name}</h1>
                      <hr></hr>
                  </div>
              </a>
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
        console.log(url);


        if(status == 'success')
        {


            for(i = 0; i < data.data.length; i++)
            {
                d = data.data[i]
                if(d.bio) //artist
                {
                    console.log("found artist!");
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/artist/",id:d.id}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
                else if(d.average_age) //medium
                {
                    console.log("found Media!");
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.name,link:"/media/",id:d.id}, null),
                        document.getElementById('result-holder-' + i)
                    );
                }
                else //work
                {
                    console.log(d);
                    console.log("found work!");
                    ReactDOM.render(
                        React.createElement(result_row, {name:d.title,link:"/work/",id:d.id}, null),
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
