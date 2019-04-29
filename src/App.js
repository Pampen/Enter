import React, { Component } from "react";
import "./styles/style.css";
import sendMessage from "./utilities/connect.js";
import ButtonContainer from "./components/button-container";
import GameScreen from "./components/game-screen";
import Terminal from "./components/terminal";
import Inventory from "./components/inventory";
import Modal from "./components/Modal";
import Commands from "./components/commands";
import Map from "./components/map";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "Outside",
      description: "This is outside.",
      chatboxText: [],
      inventory: {},
      usedItems: {
        lightSwitch: false
      },
      level: "OUTSIDE"
    };
    this.updateState = this.updateState.bind(this);
  }

  updateState(inputElementValue) {
    sendMessage(inputElementValue, this.state).then(response => {
      const newTitle = response.pageChanges.levelTitle || null;
      const newDescription = response.pageChanges.levelDescription || null;
      const newChatboxText = response.pageChanges.levelChatboxText || null;
      const newItemDescription = response.pageChanges.itemDescription || null;

      const newGameState = {};
      newGameState.inventory = response.state.inventory;
      newGameState.level = response.state.level;

      if (newTitle) {
        newGameState.title = newTitle;
      }
      if (newDescription) {
        newGameState.description = newDescription;
      }
      if (newChatboxText) {
        const currentChatboxText = this.state.chatboxText;
        currentChatboxText.push(newChatboxText);
        newGameState.chatboxText = currentChatboxText;
      }
      if (newItemDescription) {
        const currentChatboxText = this.state.chatboxText;
        currentChatboxText.push(newItemDescription);
        newGameState.chatboxText = currentChatboxText;
      }
      this.setState(newGameState);
      console.log(this.state);
    });
  }

  showMapModal = () => {
    this.setState({
      ...this.state,
      mapShow: !this.state.mapShow
    });
  };

  showInventoryModal = () => {
    this.setState({
      ...this.state,
      inventoryShow: !this.state.inventoryShow
    });
  };

  showCommandModal = () => {
    this.setState({
      ...this.state,
      commandShow: !this.state.commandShow
    });
  };
  render() {

    return (
      <main id="wrapper">
        <div className="container">
          <ButtonContainer
            props
            handleMapClick={this.showMapModal}
            handleInventoryClick={this.showInventoryModal}
            handleCommandClick={this.showCommandModal}
          />

          <div className="game-container">
            <GameScreen
              title={this.state.title}
              description={this.state.description}
              chatboxText={this.state.chatboxText}
              level={this.state.level}
            />
            <Modal onClose={this.showMapModal} show={this.state.mapShow}>
              <Map level={this.state.level} />
            </Modal>
            <Modal
              onClose={this.showInventoryModal}
              show={this.state.inventoryShow}
            >
              <Inventory inventory={this.state.inventory} />
            </Modal>
            <Modal
              onClose={this.showCommandModal}
              show={this.state.commandShow}
            >
              <Commands />
            </Modal>
            <Terminal updateState={this.updateState} />
          </div>
        </div>
      </main>
    );
  }
}

export default App;
