import React, { Component } from 'react';

export default class GameScreen extends Component {
    handleSubmit(noDefault) {
        noDefault.preventDefault()
        this.props.updateState(this.inputElement.value)
        this.inputElement.value = ''
    }
    render() {
<<<<<<< HEAD
        const color = levels[this.props.level]
=======
>>>>>>> f93e3f80b4901adc96963954f5a431ad39fc66ed
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