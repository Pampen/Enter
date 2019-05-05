import React, { Component } from "react";
import { levels } from "../utilities/levelChecker";
import tutorialMap from './maps/tutorial'

const maps = {
    /*Put map functions here. Check tutorial.js in folder maps*/ 
    'TUTORIAL': tutorialMap
}

class MapRow extends Component {
    render () {
        return
    }
}
class MapCell extends Component {
    render () {
        return
    }
}
export default class MiniMap extends Component {
  render() {
    console.log(this.props.levelHistory)
    const currentMainLevel = levels[this.props.level]
    const currentMap = maps[currentMainLevel]
    if( !currentMap) {
        return ''
    }
    return (
        <div className="map-wrapper">
            {currentMap.map((row) => {
                return (
                <div className="map-row">
                    {row.map((mapCell) => {
                        let mapCellClasses = 'map-cell '
                        if ( !mapCell || !this.props.levelHistory[mapCell.id]) { mapCellClasses += 'map-cell--hidden ' }
                        if ( mapCell && mapCell.id === this.props.level) { mapCellClasses += 'map-cell--current ' }
                        return (
                            <div className={mapCellClasses}>
                                
                                {
                                    mapCell ? mapCell.cellName : ''
                                }
                                {
                                    mapCell && mapCell.connections ? mapCell.connections.map((connection) => {
                                        let mapCellConnectionClasses = ' map-cell-connection '
                                        mapCellConnectionClasses += 'map-cell-connection--' + connection.toLowerCase() + ' '
                                        return <div className={mapCellConnectionClasses}> </div>
                                    }) : ''
                                }
                        
                            </div>
                        )
                    })}
                </div>
            )
        } )}
        </div>
    )
  }
}
