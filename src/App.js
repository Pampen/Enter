import React, { Component } from 'react';
import './style.css';
import sendMessage from './connect'

class App extends Component {
  constructor(props) {
    super(props)
    this.state={
      messages: []
    }
    this.handleClick=this.handleClick.bind(this)
  }
  handleClick() {
    sendMessage(this.inputElement.value).then(response => {
      var messages = this.state.messages;
      messages.push(this.inputElement.value);
      this.setState({messages: messages});
  })
};
  /*renderMessages() {
    Text render, title render, chat render goes here.
  }*/
  render() {
    return (
      <div id="wrapper">
        <main>
          <div className="container">
            <div className="game-container">
              <div className="game-screen">
                <div className="game-screen-header">
                </div>
                <div className="game-text-box">
                  {
                    //Chatbox-text insert
                  }
                </div>
              </div>
              <div className="terminal">
                <input 
                  ref={
                    function(inputElement) {
                      this.inputElement=inputElement;
                    }.bind(this)
                  }
                  type="text"
                  className="terminal-input"
                ></input>
                <button id="game-button" onClick={this.handleClick}>CLICKME</button>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }
}

export default App;
