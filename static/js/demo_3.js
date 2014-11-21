var Head = React.createClass({
  render: function() {
    var headNodes = this.props.keys.map(function(key) {
      return (
        <th>{key}</th>
      )
    });
    return (
      <tr>
        {headNodes}
      </tr>
    )
  }
});

var Row = React.createClass({
  render: function() {
    var data = this.props.data;
    var rowNodes = this.props.keys.map(function(key) {
      return (
        <td>{data[key]}</td>
      )
    });
    return (
      <tr>
        {rowNodes}
      </tr>
    )
  }
});

var DataTable = React.createClass({
  loadStuff: function() {
    $.ajax({
      url: this.props.url,
      success: function(data, status, xhr) {
        this.setState({data: data});
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadStuff();
    setInterval(this.loadStuff, 100);
  },
  render: function() {
    var keys = this.state.data.length > 0 ? Object.keys(this.state.data[0]) : [];
    var nodes = this.state.data.map(function (data) {
      return <Row keys={keys} data={data} />
    });

    return (
      <table className="table" role="table">
        <thead>
          <Head keys={keys} />
        </thead>
        <tbody>
          {nodes}
        </tbody>
      </table>
    );
  }
})

React.render(
  <DataTable url={url} />,
  document.getElementById('content')
);