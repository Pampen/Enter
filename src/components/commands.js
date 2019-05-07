import React, { Component } from 'react';
import Command from './command';

export default class Commands extends Component {
    render() {
        const commandInfo = {
            goCommand: {
                commandName: "GO (North/West/South/East)",
                commandDescription: "Use this command to navigate through the game"
            },
            takeCommand: {
                commandName: "TAKE (item/stairs)",
                commandDescription:
                    "Use this command to pick up items and add them to your inventory"
            },
            inspectCommand: {
                commandName: "INSPECT (item)",
                commandDescription:
                    "Use this command to inspect items that you have acquired"
            },
            useCommand: {
                commandName: "USE (item/stairs)",
                commandDescription:
                    "Use this command to use an item in your inventory such as 'use key'"
            },
            throwCommand: {
                commandName: "THROW (item)",
                commandDescription:
                    "Use this command to throw an item such as 'throw canvas'"
            }
        };
        console.log(commandInfo)
        const commandNames = Object.keys(commandInfo)

        return (
            <div className="inventory">
                <ul>
                    {
                        commandNames.map((commandName, i) =>
                            <Command key={'item-' + i} commandList={commandInfo[commandName]} />
                        )
                    }
                </ul>
            </div>
        )
    }
}