import React, { Component } from 'react';
import './styles/style.css';
import sendMessage from './utilities/connect.js'
import ButtonContainer from './components/button-container'
import GameScreen from './components/game-screen'
import Terminal from './components/terminal'
import Modal from './components/Modal'

import apple from './assets/apple.jpg'
import testBild from './assets/testBild.png'

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
    this.updateState=this.updateState.bind(this)
  }

  updateState(inputElementValue) {
    sendMessage(inputElementValue, this.state).then(response => {
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

showMapModal = () => {
    this.setState({
      ...this.state,
      mapShow: !this.state.mapShow
    });
}

showInventoryModal = () => {
  this.setState({
    ...this.state,
    inventoryShow: !this.state.inventoryShow
  });
}

showCommandModal = () => {
  this.setState({
    ...this.state,
    commandShow: !this.state.commandShow
  });
}

  render() {
    return (
      <main id="wrapper">
        <div className="container">
          <ButtonContainer props handleMapClick={this.showMapModal} handleInventoryClick={this.showInventoryModal} handleCommandClick={this.showCommandModal}/>
        
          <div className="game-container">
            <GameScreen
              title={this.state.title}
              description={this.state.description}
              chatboxText={this.state.chatboxText}
            />
            <Terminal
            updateState={this.updateState}
            />
            <Modal 
              onClose={this.showMapModal}
              show={this.state.mapShow}>
              <img src={apple} alt="An apple"/>,
            </Modal>
            <Modal
              onClose={this.showInventoryModal}
              show={this.state.inventoryShow}>
                <img src={testBild} alt="An apple"/>
            </Modal>
            <Modal
              onClose={this.showCommandModal}
              show={this.state.commandShow}>
            </Modal>
        </div> 
      </div>
    </main>
    );
  }
}

export default App;