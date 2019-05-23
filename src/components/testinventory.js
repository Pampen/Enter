import React, { Component } from 'react';
import Testitem from './testitem'

export default class testCommands extends Component {
    render() {
        const inventory = this.props.inventory
        const itemNames = Object.keys(inventory)
        if (itemNames.length === 0) {
            return (
                <div className="inventoryList">
                    <label>Inventory</label>
                    <p>You do not seem to be carrying anything...</p>
                </div>
            )
        }
        return (
            <div className="inventoryList">
                <label>Inventory</label>
                <ul className="ulInventory">
                    {
                        itemNames.map((itemName, i) =>
                            <Testitem key={'item-' + i} item={inventory[itemName]} />
                        )
                    }
                </ul>

            </div>
        );
    }
}