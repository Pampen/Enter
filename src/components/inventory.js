import React, { Component } from 'react';
import Item from './item'

export default class Inventory extends Component {
    render() {
        console.log(this.props.inventory)
        const inventory = this.props.inventory
        const itemNames = Object.keys(inventory)
        if(itemNames.length==0) {
            return (
                <div className="inventory">
                    <p>You do not seem to be carrying anything...</p>
                </div>
            )
        }
        return(
           <div className="inventory">
                <ul>
                    {
                        itemNames.map( (itemName, i) =>
                            <Item key={'item-'+ i} item={inventory[itemName]}/>
                        )
                    }
                </ul>
           </div>
        )
    }
}