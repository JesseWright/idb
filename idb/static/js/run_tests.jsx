const test_results_singleton;
var test_results = React.createClass({
  render: function() {
    var state = this.state
    return (
      <div>
      <button {state.buttonDisabled} onClick="this.handleClick()"/>
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
    $.get('', handleLoad, 'json');

  },
  handleLoad: function(results) {
    this.setState($.extend(
      this.state, {buttonDisabled: '', loadState: 'done', results: results}));

  }
});

function make_tests() {
  ReactDOM.render(
      React.createElement(test_results, {results: '', state: 'inactive', buttonDisabled: ''}, null),
      document.getElementById('test-results')
  );
}