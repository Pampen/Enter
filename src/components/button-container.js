import React, { Component } from 'react';

export default class ButtonContainer extends Component {
    handleMapClick() {
        this.props.handleMapClick()
    }
    render() {
        return( 
            <div className="button-container">
                <div id="main-buttons">
                <button className="game-button" id="inventory-button">I</button>
                <button
                    className="game-button"
                    id="map-button"
                    onClick={this.handleMapClick.bind(this)}>M
                </button>
                </div>
                <button className="game-button" id="command-button">C</button>
            </div>
        )
    } 
}
