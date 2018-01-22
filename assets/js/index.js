var React = require('react')
var ReactDOM = require('react-dom')

var PatientList = React.createClass({
    loadPatientsFromServer: function(){
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
        this.loadPatientsFromServer();
        setInterval(this.loadPatientsFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var patients = this.state.data.map(function(patient){
                return <li> {patient.patient_id} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {patients}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<PatientList url='/aml/patient/v1' pollInterval={10000} />, 
    document.getElementById('container'))