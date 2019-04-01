import React, { Component } from 'react';
import './style.css';
import sendMessage from './connect'

class App extends Component {
  constructor(props) {
    super(props)
    this.state={
      title: 'Outside',
      description: 'This is outside.',
      chatboxText: [],
      inventory: {
        firstObject: false,
        secondObject: false
      },
      level: 'OUTSIDE'
    }
    this.handleClick=this.handleClick.bind(this)
  }

  handleClick(noDefault) {
    noDefault.preventDefault()
    sendMessage(this.inputElement.value, this.state).then(response => {
      const newTitle = response.pageChanges.levelTitle || null
      const newDescription = response.pageChanges.levelDescription || null
      const newChatboxText = response.pageChanges.levelChatboxText || null
      const newGameState = {}
      newGameState.inventory = response.state.inventory
      newGameState.level = response.state.level
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
                <form onSubmit={this.handleClick}>
                  <input 
                      ref={
                        function(inputElement) {
                          this.inputElement=inputElement;
                        }.bind(this)
                      }
                      type="text"
                      className="terminal-input"
                  ></input>
                  <button id="game-button">Enter</button>
                </form>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }
}

export default App;
