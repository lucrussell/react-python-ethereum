import React from "react";
import Info from "./Info";
import { PageHeader } from "react-bootstrap";

require('../css/app.css');
var $ = require('jquery');

export default class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render () {
        return (
            <PageHeader>
                <div className='header-contents'>
                    <Info name='Rimini' />
                </div>
            </PageHeader>
        );
    }
}
