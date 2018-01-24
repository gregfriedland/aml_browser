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

        // Construct a table with the results; complex fields like arrays and objects
        // get their own nested tables
        var table_body = [];
        for (field in patient) {
            var val;
            if (typeof(patient[field]) === "string") {
                val = patient[field];
                table_body.push(<tr><td><b>{field}</b></td><td>{val}</td></tr>);
            } else if (Array.isArray(patient[field]) && patient[field].length > 0) {
                if (typeof(patient[field][0]) === "string") {
                    var sub_rows = [];
                    for (var i = 0; i < patient[field].length; i++) {
                        sub_rows.push(<tr><td>{patient[field][i]}</td></tr>);
                    }
                    val = <div><table className="ui celled table"><thead></thead><tbody>{sub_rows}</tbody></table></div>;
                } else {
                    var cols = Object.keys(patient[field][0]);
                    var sub_header = [];
                    for (var i = 0; i < cols.length; i++) {
                        sub_header.push(<th>{cols[i]}</th>);
                    }
                    var sub_rows = [];
                    for (var i = 0; i < patient[field].length; i++) {
                        var sub_row = [];
                        for (var c = 0; c < cols.length; c++) {
                            sub_row.push(<td>{patient[field][i][cols[c]]}</td>);
                        }
                        sub_rows.push(<tr>{sub_row}</tr>);
                    }
                    val = <div><table className="ui celled table"><thead><tr>{sub_header}</tr></thead><tbody>{sub_rows}</tbody></table></div>;
                }
                table_body.push(<tr><td><b>{field}</b></td><td>{val}</td></tr>);
            } else {
                table_body.push(<tr><td><b>{field}</b></td><td></td></tr>);                
            }
        }
        return (
            <div>
                <h1>AML Patient {patient.patient_id}</h1>
                <table className="ui striped table">
                  <tbody>
                    {table_body}
                  </tbody>
                </table>
            </div>
        )
    }
})

ReactDOM.render(<Patient url={patient_url} pollInterval={10000} />, 
    document.getElementById('container'))

