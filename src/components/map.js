import React, { Component } from "react";
import apple from "../assets/apple.jpg";
import { levels } from "../utilities/levelChecker";

class Map extends Component {
  render() {
    let currentLevel = this.props.level;
    for (const key in levels) {
      if (key === currentLevel) {
        currentLevel = levels[key];
      }
    }
    console.log(currentLevel);
    switch (currentLevel) {
      case "ANGER":
        return <img src={apple} alt="an testimage" />;
      case "LOVE":
        return <img src={apple} alt="an testimage" />;
      case "JOY":
        return <img src={apple} alt="an testimage" />;
      case "SADNESS":
        return <img src={apple} alt="an testimage" />;
      case "TUTORIAL":
        return <img src={apple} alt="an testimage" />;
      default:
        return <div>Where are you and how did you get here?</div>;
    }
  }
}

export default Map;
