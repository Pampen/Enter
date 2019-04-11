export default function returnFlaskPost(message, state) {
    return fetch( 'http://localhost:5000/', {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, 
      method: 'POST',
      body: JSON.stringify( {
        message,
        state: {
          inventory: state.inventory,
          level: state.level
        }
      })
    }).then(response => {
        return response.json()
    })
  }