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
            var i = 1;
            var patients = this.state.data.map(function(patient){
            	var url = "/aml/" + i;
            	i = i + 1;
                return <tr>
                		 <td><a href={url}>{patient.patient_id}</a></td>
                		 <td>{patient.gender}</td>
                		 <td>{patient.ethnicity}</td>
                		 <td>{patient.platelet_result_count}</td>
                		 <td>{patient.vital_status}</td>
                	   </tr>
            })
        }
        return (
            <div>
                <h1>AML Patients</h1>
				<table className="ui celled table">
				  <thead>
				    <tr><th>Patient ID</th>
				    <th>Gender</th>
				    <th>Ethnicity</th>
				    <th>Platelet Count</th>
				    <th>Vital Status</th>
				  </tr></thead>
			      <tbody>
                    {patients}
                  </tbody>
                </table>
            </div>
        )
    }
})

ReactDOM.render(<PatientList url='/aml/patient/v1' pollInterval={10000} />, 
    document.getElementById('container'))
