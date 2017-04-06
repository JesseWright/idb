var test_results = React.createClass({
  getInitialState: function() {
    return this.props;
  },
  render: function() {
    var state = this.state;
    return (
      <div>
      <button disabled={state.buttonDisabled} onClick="this.handleClick()"/>
        <div className="test-results {state.loadState}">
          <div class="overlay">
            <div class="spinner">
              <img src="/static/img/spinner.gif"/>
            </div>
          </div>
          <pre>{state.results}</pre>
        </div>
      </div>);
  },
  handleClick: function() {
    this.setState($.extend(
      this.state, {buttonDisabled: 'disabled', loadState: 'loading'}));
    $.get('http://www.kingsofchaos.com', handleLoad, 'json');

  },
  handleLoad: function(results) {
    this.setState($.extend(
      this.state, {buttonDisabled: '', loadState: 'done', results: results}));

  }
});

var make_tests = function() {
  ReactDOM.render(
      React.createElement(test_results, {results: '', loadState: 'inactive', buttonDisabled: ''}, null),
      document.getElementById('tests')
  );
}

$(document).ready(make_tests);
