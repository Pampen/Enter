import React, { Component } from 'react';

export default class ButtonContainer extends Component {
    handleMapClick() {
        this.props.handleMapClick()
    }
    handleInventoryClick() {
        this.props.handleInventoryClick()
    }
    handleCommandClick() {
        this.props.handleCommandClick()
    }
    render() {
        return( 
            <div className="button-container">
                <div id="main-buttons">
                <button
                    className="game-button"
                    id="inventory-button"
                    onClick={this.handleInventoryClick.bind(this)}>I
                </button>
                <button
                    className="game-button"
                    id="map-button"
                    onClick={this.handleMapClick.bind(this)}>M
                </button>
                </div>
                <button 
                    className="game-button" 
                    id="command-button"
                    onClick={this.handleCommandClick.bind(this)}>C
                </button>
            </div>
        )
    } 
}
