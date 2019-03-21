export default function returnFlaskPost(message) {
    return fetch( 'http://localhost:5000/', {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, 
      method: 'POST',
      body: JSON.stringify( {
        message
      })
    }).then(response => {
        return response.json()
    })
  }