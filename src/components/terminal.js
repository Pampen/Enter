import React, { Component } from 'react';
import { levels } from '../utilities/levelChecker';

export default class GameScreen extends Component {
    handleSubmit(noDefault) {
        noDefault.preventDefault()
        this.props.updateState(this.inputElement.value)
        this.inputElement.value = ''
    }
    render() {
        const color = levels[this.props.level]
        return (
            <div className="terminal">
                <form onSubmit={this.handleSubmit.bind(this)}>
                <input
                    placeholder="Enter command..."
                    ref={
                        function(inputElement) {
                        this.inputElement=inputElement;
                        }.bind(this)
                    }
                    type="text"
                    className="terminal-input"
                ></input>
                <button id="enter-button">Enter</button>
                </form>
            </div>
        )
    }
}