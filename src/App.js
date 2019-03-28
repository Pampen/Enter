import React, { Component } from 'react';
import './style.css';
import sendMessage from './connect'

class App extends Component {
  constructor(props) {
    super(props)
    this.state={
      title: 'Outside',
      description: 'You wake up outside, what do you want to do?',
      chatboxText: [],
      inventory: [
        'firstObject',
        'secondObject'
      ]
    }
    this.handleClick=this.handleClick.bind(this)
  }
  handleClick() {
    sendMessage(this.inputElement.value).then(response => {
      const newTitle = response.newGameState.levelTitle || null
      const newDescription = response.newGameState.levelDescription || null
      const newChatboxText = response.newGameState.levelChatboxText || null
      const newGameState = {
        inventory: []
      };
      if (newTitle) {
        newGameState.title = newTitle;
      };
      if (newDescription) {
        newGameState.description = newDescription;
      };
      if (newChatboxText) {
        const currentChatboxText = this.state.chatboxText;
        currentChatboxText.push(newChatboxText);
        newGameState.chatboxText = currentChatboxText;
      }
      if (response.inventory) {
        if (response.inventory.firstObject) {
          newGameState.inventory.push('firstObject');
        }
        if (response.inventory.secondObject) {
          newGameState.inventory.push('secondObject');
        }
      }
      this.setState(newGameState);
      console.log(this.state);
  })
};

  render() {
    return (
      <div id="wrapper">
        <main>
          <div className="container">
            <div className="game-container">
              <div className="game-screen">
                <div className="game-screen-header">
                  <h2 id="title">{this.state.title}</h2>
                  <p className="level-description">{this.state.description}</p>
                </div>
                <div className="game-text-box">
                  {
                    this.state.chatboxText.map((text, i) => {
                      return <p key={i} className="chatbox-text">{text}</p>
                    })
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
