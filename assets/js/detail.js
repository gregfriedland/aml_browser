var React = require('react')
var ReactDOM = require('react-dom')

var path = new URL(window.location).pathname;
path = path.replace(/\/$/, "");
var patient_pk = path.split("/").pop();
var patient_url = '/aml/patient/' + patient_pk + '/v1';

var Patient = React.createClass({
    loadOnePatientFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadOnePatientFromServer();
        setInterval(this.loadOnePatientFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var patient = this.state.data;
        }
        return (
            <div>
                <h1>Hello detail!</h1>
                <ul>
                    {patient.patient_id}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<Patient url={patient_url} pollInterval={10000} />, 
    document.getElementById('container'))

