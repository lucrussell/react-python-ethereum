import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";

var $ = require('jquery');

export default class Info extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};

        this.getInfo = this.getInfo.bind(this);
        this.deployContract = this.deployContract.bind(this);
        this.callContract = this.callContract.bind(this);
    }

    callback(text) {
        this.setState({text: text});
    }

    getInfo() {
        $.get(window.location.href + 'info', (data) => {
            console.log(data);
            this.callback(data);
        });
    }

    deployContract() {
        $.get(window.location.href + 'deploy_contract', (data) => {
            console.log(data);
            this.callback(data);
        });
    }

    callContract() {
        $.get(window.location.href + 'call_contract', (data) => {
            console.log(data);
            this.callback(data);
        });
    }

    render () {
        return (
            <Grid>
                <Row>
                <Col md={7} mdOffset={5}>
                    <h1>{this.state.text}</h1>
                    <hr/>
                </Col>
                </Row>
                <Row>
                <Col md={7} mdOffset={5}>
                    <Button bsSize="large" bsStyle="danger" onClick={this.getInfo}>
                    Get Info
                    </Button>
                     <Button bsSize="large" bsStyle="danger" onClick={this.deployContract}>
                    Deploy Contract
                    </Button>
                    <Button bsSize="large" bsStyle="danger" onClick={this.callContract}>
                    Test Contract
                    </Button>
                </Col>
                </Row>
            </Grid>
        );
    }
}
