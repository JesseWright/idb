var test_results = React.createClass({
  getInitialState: function() {
    return $.extend({},this.props);
  },
  render: function() {
    var state = this.state;
    var btnClass = buttonDisabled ? 'btn-disabled' : '';
    return (
      <div>
      <button className="{btnClass}" onClick={this.handleClick}>Run Tests</button>
        <div className="test-results {state.loadState}">
          <div className="overlay">
            <div className="spinner">
              <img src="/static/img/spinner.gif"/>
            </div>
          </div>
          <pre>{state.results}</pre>
        </div>
      </div>);
  },
  handleClick: function() {
    if(!this.state.buttonDisabled) {
      this.setState($.extend(
        this.state, {buttonDisabled: true, loadState: 'loading'}));
      $.get('/artists/', this.handleLoad, 'json');
    }

  },
  handleLoad: function(results) {
    this.setState($.extend(
      this.state, {buttonDisabled: false, loadState: 'done', results: results}));

  }
});

var make_tests = function() {
  ReactDOM.render(
      React.createElement(test_results,
        {results: '', loadState: 'inactive', buttonDisabled: false}, null),
      document.getElementById('test')
  );
}

$(document).ready(make_tests);
