var Input = ReactBootstrap.Input;

var InputNode = React.createClass({
  render: function() {
    if (this.props.data.type === "choice") {
      var choices = this.props.data.choices.map(function(choice) {
        return <option value={choice.value}>{choice.display_name}</option>
      });
      return (
          <Input type="select" label={this.props.data.label}>
            {choices}
          </Input>
        )
    } else {
      return <Input type="text" label={this.props.data.label} />
    }
  }
});

var ObjectForm = React.createClass({
  handleSubmit: function(e) {
    e.preventDefault();
    console.log(this.refs);
    return false;
  },
  getInitialState: function() {
    return {data: {}}
  },
  componentDidMount: function() {
    $.ajax({
      url: '/api/authors/',
      type: 'OPTIONS',
      success: function(data, status, xhr) {
        this.setState({data: data.actions.POST});
      }.bind(this)
    });
  },
  render: function() {
    var data = this.state.data;
    var inputNodes = Object.keys(data).map(function(key) {
      if (data[key].read_only) {
        return;
      } else {
        return <InputNode ref={key} data={data[key]} />;
      };
    });
    return (
      <form onSubmit={this.handleSubmit}>
        {inputNodes}
        <button type="submit" className="btn btn-primary pull-right">submit</button>
      </form>
    );
  }
});

React.render(
  <ObjectForm />,
  document.getElementById('content')
);