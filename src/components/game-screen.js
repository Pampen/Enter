import React, { Component } from 'react';
import { levels } from '../utilities/levelChecker'

export default class GameScreen extends Component {
    render() {
        const color = levels[this.props.level]
        console.log('COLOOOOOOOOOOOR: ' + color)
        return (
            <div className="game-screen">
                <div className="game-screen-header">
                    <h2 id="title" className={color}>{this.props.title}</h2>
                    <p className="level-description">{this.props.description}</p>
                </div>
                <div className="game-text-box">
                    {
                        this.props.chatboxText.map((text, i) => {
                            return <p key={i} className="chatbox-text">{text}</p>
                        })
                    }
                </div>
            </div>
        )
    }
}