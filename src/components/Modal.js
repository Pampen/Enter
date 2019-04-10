import React from 'react';

const backdropStyle = {
    position: 'fixed',
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    backgroundColor: 'rgba(0,0,0,0.3)',
    padding: 50
};

const modalStyle = {
    backgroundColor: '#fff',
    borderRadius: 5,
    maxWidth: 500,
    minHeight: 300,
    margin: '0 auto',
    padding: 30,
    position: "relative"
};

const footerStyle = {
    position: "absolute",
    top: 10,
    right: 10
};

export default class extends React.Component {
    onClose = (e) => {
        this.props.onClose && this.props.onClose(e)
    }
    render() {
        if (!this.props.show){
            return null;
        }
        return (
            <div style={backdropStyle}>
                <div style={modalStyle}>
                    {this.props.children}
                    <div style={footerStyle}>
                        <button onClick={(e) => { this.onClose(e)}}>
                            X
                        </button>
                    </div>
                </div>
            </div>
        )
    }
}