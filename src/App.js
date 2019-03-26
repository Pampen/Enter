import React, { Component } from 'react';
import './style.css';
import sendMessage from './connect'

class App extends Component {
  constructor(props) {
    super(props)
    this.state={
      title: 'Default Title',
      description: 'This is a game!',
      chatboxText: []
    }
    this.handleClick=this.handleClick.bind(this)
  }
  handleClick() {
    sendMessage(this.inputElement.value).then(response => {
      let newTitle = response.newGameState.levelTitle || null
      let newDescription = response.newGameState.levelDescription || null
      let newChatboxText = response.newGameState.levelChatboxText || null
      let newState = {
      };
      if (newTitle) {
        newState.title = newTitle;
      };
      if (newDescription) {
        newState.description = newDescription;
      };
      if (newChatboxText) {
        const currentChatboxText = this.state.chatboxText;
        currentChatboxText.push(newChatboxText);
        newState.chatboxText = currentChatboxText;
      };
      this.setState(newState);
      console.log(this.state);
  });
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
