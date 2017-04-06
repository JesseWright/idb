
        var cur_page = 1;
        var first_run = 1;
        var old_name = undefined;
        var old_startDate = undefined;
        var old_endDate = undefined;
        var page_enum = {
            ARTISTS: 'artist',
            WORKS: 'work',
            MEDIA: 'medium'
        };
        var new_card_data = undefined;

        var artist_card = React.createClass({
              getDefaultProps: function(){
                  return {
                      'name': "default",
                      'dob' : "1899",
                      'image' : '/static/img/vangogh.jpg',
                      'id': 1,
                      'link': "/artist/"
                  };
              },
              render: function() {
                  var link_to_use = ""+ this.props.link + this.props.id;
                  return(
                    <a href={link_to_use}>
                        <div className="idb-card">
                          <img className = "idb-artist-portrait"src={this.props.image}></img>
                          <div className = "idb-artist-name">{this.props.name}</div>
                          <div className = "idb-artist-birth-death">{this.props.dob}</div>
                        </div>
                    </a>
                  );
              }
            });


        var load = function(){
            update(1,1,document.title);
        }

        //load cards when page loads
        $(document).ready(load);

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




        function handle_page_change(isPrev,request_page)
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
                cur_page = cur_page + 1;
            }
            if (prev_page !== cur_page)
                update(1,cur_page,request_page);
            else
                console.log("Tried to go back from page 1. Nice try! I'm like, maybe 1 step ahead of you.")
        }

        function update(sort_order,page_num,request_page)
        {
            /*
            //steps to do what I actually want to do
            1. get the values we're going to need
            2. check for errors
                a. if there were no errors, build the filters
            3. check to see if our list of filters is the same one we already had
            4. check if we're on our first run of the page
            6. get new card data
            7. update the cards based on that data
            */

            name = document.getElementById('nameBox').value;
            dateStart = document.getElementById('dateStart').value; //on the media page, this is the date delta
            dateEnd = document.getElementById('dateEnd').value;

            //first check to make sure neither date is zero
            if (dateStart < 0 || dateEnd < 0)
                document.getElementById('errorText').textContent = "Error: don't use a negative value.";
            //if neither of them were, then we're good to build our filters
            else
            {
                if (request_page != page_enum.MEDIA && (dateEnd < dateStart))
                    document.getElementById('errorText').textContent = "Error: end date < start date.";
                else
                {
                    document.getElementById('errorText').textContent = "";
                    if (request_page == page_enum.MEDIA)
                    {


                            //we have to do a little math on the media page
                            base = parseInt(dateEnd);
                            delta = parseInt(dateStart);
                            if(isNaN(base) || isNaN(delta))
                            {
                                dateStart = "";
                                dateEnd = "";
                            }
                            else
                            {
                                dateStart = base - delta;
                                dateEnd = base + delta;
                            }

                    }

                    //clear the error text
                    document.getElementById('errorText').textContent = "";
                    var order_by = undefined;
                    var ascending = undefined;

                    switch (sort_order)
                    {
                        case 1:
                            if (request_page == page_enum.WORKS)
                                order_by = "title";
                            else
                                order_by = "name";
                            ascending = 1;
                            break;
                        case 2:
                            if (request_page == page_enum.WORKS)
                                order_by = "title";
                            else
                                order_by = "name";
                            ascending = 0;
                            break;
                        case 3:
                            if (request_page == page_enum.ARTISTS)
                                order_by = "dob";
                            else if (request_page == page_enum.WORKS)
                                order_by = "date";
                            else
                                order_by = "average_age"
                            ascending = 1;
                            break;
                        case 4:
                            if (request_page == page_enum.ARTISTS)
                                order_by = "dob";
                            else if (request_page == page_enum.WORKS)
                                order_by = "date";
                            else
                                order_by = "average_age"
                            ascending = 0;
                            break;
                    }

                    var filters = {
                        "order_by": order_by,
                        "ascending":ascending,
                        "name_filter":name,
                        "date_after":dateStart,
                        "date_before":dateEnd,
                        "page":(page_num-1)
                    }

                }
            }

            if (!first_run && (old_name !== name || old_startDate !== dateStart || old_endDate !== dateEnd))
            {
                page_num = 1;
                old_name = name;
                old_startDate = dateStart;
                old_endDate = dateEnd;
            }
            //need this block to prevent weird page number jumps on the first new page request
            if (first_run)
            {
                old_name = name;
                old_startDate = dateStart;
                old_endDate = dateEnd;
                first_run = 0;
            }
            get_new_card_data(filters,request_page,page_num);


            cur_page = page_num;



        }

        function get_new_card_data(filters,request_page,page_num)
        {
            var url = "/query_" + request_page + "?";
            url = url + 'order_by=' + filters.order_by + '&name_filter=' + filters.name_filter
                + '&date_after=' + filters.date_after + '&date_before=' + filters.date_before + '&ascending='
                + filters.ascending + '&page=' + filters.page;
            console.log(url);
            $.get(url,function(data,status){
                if(status == 200)
                {
                    update_cards(data);
                    ReactDOM.render(
                        React.createElement(page_ident, {page_num:page_num,max_page_num:(data.pages) }, null),
                        document.getElementById('page-identifier')
                    );
                }
                else
                {
                    update_cards(undefined);
                    ReactDOM.render(
                        React.createElement(page_ident, {page_num:-1,max_page_num:0 }, null),
                        document.getElementById('page-identifier')
                    );
                }


            });

        }
        function update_cards(data){
            if(!data)
            {
                for (i = 0; i < 16; i++){
                    d = data.data[i];
                    ReactDOM.render(
                        React.createElement(artist_card, {name:d.name,dob:d.dob,image:d.image,id:d.id,}, null),
                        document.getElementById('card-' + i)
                    );
                }
            }
            else {
                for (i = 0; i < data.data.length; i++){
                    d = data.data[i];
                    ReactDOM.render(
                        React.createElement(artist_card, {name:d.name,dob:d.dob,image:d.image,id:d.id,}, null),
                        document.getElementById('card-' + i)
                    );
                }
                for(j = i; j < 16; j ++)
                {
                    ReactDOM.render(
                        React.createElement('div', null, null),
                        document.getElementById('card-' + j)
                    );
                }
            }

        }
        function get_page_enum(){
            return page_enum;
        }
