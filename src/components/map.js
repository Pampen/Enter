import React, { Component } from "react";
import apple from "../assets/apple.jpg";

class Map extends Component {
  render() {
    switch (this.props.level) {
      case "OUTSIDE":
      case "PORCH":
      case "GREENHOUSE":
        return <img src={apple} alt="an testimage" />;
      case "BEACH":
      case "CABIN":
      case "CELLAR":
      case "GATE":
      case "OUTSIDE_SHED":
      case "SHED":
      case "OUTSIDE_SHIPWRECK":
      case "SHIPWRECK":
      case "LIGHTHOUSE_OUTSIDE":
      case "LIGHTHOUSE":
      case "LIGHTHOUSE_TOP":
        return <img src={apple} alt="an testimage" />;
      case "BLUE_START":
      case "BLUE_TORCH_ROOM":
      case "BLUE_CORRIDOR_1":
      case "BLUE_CORRIDOR_2":
      case "BLUE_CORRIDOR_3":
      case "BLUE_CORRIDOR_4":
      case "BLUE_CORRIDOR_5":
      case "BLUE_CORRIDOR_6":
      case "BLUE_CORRIDOR_7":
      case "BLUE_CORRIDOR_8":
      case "BLUE_CORRIDOR_9":
      case "BLUE_FINISH":
        return <img src={apple} alt="an testimage" />;
      case "MAIN_HALL":
        return <img src={apple} alt="an testimage" />;
      case "LIVING_ROOM":
      case "KITCHEN":
      case "HALL":
      case "UPPER_FLOOR":
      case "BEDROOM":
      case "BASEMENT":
      case "ATTIC":
      case "CRIBROOM":
      case "BABYROOM":
      case "NURSINGROOM":
      case "STUDYROOM":
      case "MESSYROOM":
        return <img src={apple} alt="an testimage" />;
      default:
        return null;
    }
  }
}

export default Map;
