import React, { Component } from 'react';
import { levels } from '../utilities/levelChecker'

const mirrorRoomColorMap = {
    'ANGER_1': 'ANGER',
    'ANGER_2': 'ANGER',
    'LOVE': 'LOVE',
    'SADNESS_1': 'SADNESS',
    'SADNESS_2': 'SADNESS',
    'JOY': 'JOY',
    'MIRROR_ROOM_1': 'TUTORIAL',
    'MIRROR_ROOM_2': 'TUTORIAL'
}

export default class GameScreen extends Component {
    render() {
        const mainLevel =  levels[this.props.level]
        const color = mainLevel !== 'MIRROR_ROOM'
            ? mainLevel
            : mirrorRoomColorMap[this.props.level]
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