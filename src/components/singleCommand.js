import React, { Component } from 'react';

export default class TEST1 extends Component {
    render() {
        const commandList = this.props.commandList
        return (
            <li key={commandList.commandName} className="item" id="descriptionItem">
                <span className="item-name">
                    {commandList.commandName}
                </span>
                <span className="description">
                    {commandList.commandDescription}
                </span>
            </li>
        )
    }
}