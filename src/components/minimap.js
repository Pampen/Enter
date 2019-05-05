import React, { Component } from "react";
import { levels } from "../utilities/levelChecker";
import tutorialMap from './maps/tutorial'

const maps = {
    /*Put map functions here. Check tutorial.js in folder maps*/ 
    'TUTORIAL': tutorialMap
};

class MapRow extends Component {
    render () {
        return (<div className="map-row">
        {this.props.row.map((mapCell) => {
            return <MapCell mapCell={mapCell} level={this.props.level} levelHistory={this.props.levelHistory}/>
        })}
    </div>
        );
    };
};
class MapCell extends Component {
    render () {
        let mapCellClasses = 'map-cell '
        if ( !this.props.mapCell || !this.props.levelHistory[this.props.mapCell.id]) {
            mapCellClasses += 'map-cell--hidden '
        };
        if ( this.props.mapCell && this.props.mapCell.id === this.props.level) {
            mapCellClasses += 'map-cell--current '
        };
        return (
            <div className={mapCellClasses}>
                
                {
                    this.props.mapCell
                        ? this.props.mapCell.cellName
                        : ''
                }
                {
                    this.props.mapCell && this.props.mapCell.connections
                        ? this.props.mapCell.connections.map((connection) => {
                            return <MapConnection connection ={connection}/>
                        })
                        : ''
                }
                <div className="map-cell-name">
                    {
                        this.props.mapCell && this.props.mapCell.color
                            ? <p className={this.props.mapCell.color}>{this.props.mapCell.name}</p>
                            : '' 
                    }
                </div>
            </div>
        );
    };
;}

class MapConnection extends Component {
    render() {
        let mapCellConnectionClasses = ' map-cell-connection '
        mapCellConnectionClasses += 'map-cell-connection--' +
            this.props.connection.toLowerCase() + ' '
        return <div className={mapCellConnectionClasses}> </div>
    }
}

export default class MiniMap extends Component {
  render() {
    console.log(this.props.levelHistory)
    const currentMainLevel = levels[this.props.level]
    const currentMap = maps[currentMainLevel]
    if( !currentMap) {
        return ''
    };
    return (
        <div className="map-wrapper">
            <div className="map-compass">
                <span className="map-compass-n">N</span>
                <span className="map-compass-s">S</span>
                <span className="map-compass-w">W</span>
                <span className="map-compass-e">E</span>
                <div className="map-compass-needle"></div>
            </div>
            {currentMap.map((row) => {
                return <MapRow 
                    level={this.props.level}
                    levelHistory={this.props.levelHistory}
                    row={row}
                />
        } )}
        </div>
    );
  };
};