import React from 'react';

const GameScreenHeader = () => (
    <div className="game-screen-header">
        <h2 id="title">{this.state.title}</h2>
        <p className="level-description">{this.state.description}</p>
    </div>
);

export default GameScreenHeader;