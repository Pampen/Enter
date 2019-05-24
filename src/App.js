import React, { Component } from "react";
import "./styles/style.css";
import sendMessage from "./utilities/connect.js";
import GameScreen from "./components/game-screen";
import Terminal from "./components/terminal";
import Map from "./components/map";
import { levels } from './utilities/levelChecker';
import Testinventory from "./components/testinventory";
import Testcommand from "./components/testCommands"

const audioFile = {
  'TUTORIAL': 'tutorial.mp3',
  'JOY': 'joy.mp3',
  'ANGER': 'anger.mp3',
  'LOVE': 'love.mp3',
  'SADNESS': 'sadness.mp3',
  'MIRROR_ROOM': 'mirror_room.mp3',
  'MAIN_HALL': 'tutorial.mp3',
  'MAIN_HALL_RETURN_FROM_GREEN': 'tutorial.mp3',
  'MAIN_HALL_RETURN_FROM_RED': 'tutorial.mp3',
  "MAINHALL_ALL": 'tutorial.mp3',
  "MAINHALL_RED": 'tutorial.mp3',
  "MAINHALL_PINK": 'tutorial.mp3',
  "MAINHALL_BLUE": 'tutorial.mp3'
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      startedGame: false,
      title: "Outside",
      description: "It's cold outside. There is a strange old house in front of you.There isn't much to see around you. You are surrounded by dense forest. There is also a small path covered in leaves to the west side of the house.",
      chatboxText: [],
      inventory: {},
      usedItems: {
        lightSwitch: false,
      },
      pinkPuzzleItems: [],
      isBurned: [],
      level: "OUTSIDE",
      levelHistory: {
        OUTSIDE: true
      },
      audio: './Audio/tutorial.mp3'
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
      newGameState.usedItems = response.state.usedItems
      newGameState.isBurned = response.state.isBurned;
      newGameState.pinkPuzzleItems = response.state.pinkPuzzleItems;
      newGameState.levelHistory = this.state.levelHistory
      newGameState.audio = './Audio/' + audioFile[levels[newGameState.level]]

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
      newGameState.levelHistory[response.state.level] = true;
      this.setState(newGameState);
      console.log(this.state);
    });
  }
  componentDidMount = () => {
    document.querySelector("body").addEventListener('keydown', (event) => {
      if (event.keyCode === 13) {
        if (!this.state.startedGame) {
          this.setState({ startedGame: true })
        }
      }
    })
  }
  handleKeyDown = () => {
    console.log('hello')
  }
  render() {
    console.log(this.state.level)

    return (
      <main id="wrapper">
          {
          !this.state.startedGame
          ? <div className="main-menu">
              <h1 className="game-title">
                <span id="game-title-first-letter">E</span>nter:<span id="title-animation">_</span>
              </h1>
              <span id="title-animation">
                <h2 className="start-game">Press enter</h2>
              </span>
            </div> 
          : null
        }
        <div className="container">
          <div className="game-container">
            <GameScreen
              title={this.state.title}
              description={this.state.description}
              chatboxText={this.state.chatboxText}
              level={this.state.level}
            />
            <Map level={this.state.level} levelHistory={this.state.levelHistory} />

            <Testinventory inventory={this.state.inventory} />
            <Testcommand />

            <Terminal updateState={this.updateState} />
          </div>
        </div>
          {
            this.state.startedGame 
            ? <audio
              autoPlay
              loop
              src={this.state.audio}>
              </audio>
            : null
          }
      </main>
    );
  }
}
export default App;