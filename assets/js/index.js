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
    }, 
    search: function(event){
        var query = event.target.value.toLowerCase();
        var url = "/aml/search/" + query + "/v1";
        console.log(url);
        $.ajax({
            url: url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },
    render: function() {
        if (this.state.data) {
            console.log('DATA!')

            // construct a table with the results for each patient
            var patients = this.state.data.map(function(patient) {
            	var url = "/aml/" + patient.id;
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

                  <div className="ui search">
                    <div className="ui icon input">
                        <input className="prompt" type="text" placeholder="Search all fields..."
                            onChange={e => this.search(e)}/>
                        <i className="search icon"></i>
                    </div>
                  </div>

				<table className="ui striped table">
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
