import React, { Component } from 'react';
import Testcommand from './singleCommand';

export default class Test extends Component {
    render() {
        const commandInfo = {
            goCommand: {
                commandName: "GO",
                commandDescription: "Use this command to navigate through the game"
            },
            takeCommand: {
                commandName: "TAKE",
                commandDescription:
                    "Use this command to pick up items and add them to your inventory"
            },
            inspectCommand: {
                commandName: "INSPECT",
                commandDescription:
                    "Use this command to inspect items that you have acquired"
            },
            useCommand: {
                commandName: "USE",
                commandDescription:
                    "Use this command to use an item in your inventory such as 'use key'"
            },
            throwCommand: {
                commandName: "THROW",
                commandDescription:
                    "Use this command to throw an item such as 'throw canvas'"
            }
        };
        const commandNames = Object.keys(commandInfo)

        return (
            <div className="commandList">
                <label><strong>Command List</strong></label>

                <ul className="ulCommands">
                    {
                        commandNames.map((commandName, i) =>
                            <Testcommand key={'item-' + i} commandList={commandInfo[commandName]} />
                        )
                    }
                </ul>
            </div >
        )
    }
}