import React, { Component } from 'react';

export default class Testitem extends Component {
    render() {
        const item = this.props.item
        return (

            <li key={item.itemName} className="item">
                <span className="item-name">
                    {item.itemName}
                </span>
                <span className="description">
                    {item.itemDescription}
                </span>
            </li>
        )
    }
}