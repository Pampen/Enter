import React, { Component } from "react";
import { levels } from "../utilities/levelChecker";
import MiniMap from './minimap';

class Map extends Component {
  render() {
    let mainLevel;
    for (const key in levels) {
      if (key === this.props.level) {
        mainLevel = levels[key];
      };
    };
    return <MiniMap mainLevel={mainLevel} level={this.props.level} levelHistory={this.props.levelHistory} />
  };
};

export default Map;