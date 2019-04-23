import React, { Component } from 'react';

export default class Command extends Component {
    render() {
        const commandList=this.props.commandList
        return(
            <li key={commandList.commandName} className="item">
                <span className="item-name"> 
                    {commandList.commandName}
                </span>
                <span className="item-description">
                    {commandList.commandDescription}
                </span>
            </li>
        )
    }
}