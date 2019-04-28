import React from "react";

const modalStyle = {
  backgroundColor: "#333",
  padding: 30,
  position: "absolute",
  top: 0,
  bottom: 0,
  left: 0,
  right: 0
};

const footerStyle = {
  position: "absolute",
  top: 10,
  right: 10,
  borderRadius: 0,
  backgroundColor: "transparent"
};

export default class extends React.Component {
  onClose = e => {
    this.props.onClose && this.props.onClose(e);
  };
  render() {
    if (!this.props.show) {
      return null;
    }
    return (
      <div className="animation-fade-in" style={modalStyle}>
        {this.props.children}
        <div style={footerStyle}>
          <button
            onClick={e => {
              this.onClose(e);
            }}
            className="close-button"
          >
            CLOSE (X)
          </button>
        </div>
      </div>
    );
  }
}
