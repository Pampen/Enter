import React, { Component } from 'react';
import Command from './command';

export default class Commands extends Component {
    render() {
        const commandInfo = this.props.commandInfo
        console.log(commandInfo)
        const commandNames = Object.keys(commandInfo)

        return(
           <div className="inventory">
                <ul>
                    {
                        commandNames.map( (commandName, i) =>
                            <Command key={'item-'+ i} commandList={commandInfo[commandName]}/>
                        )
                    }
                </ul>
           </div>
        )
    }
}