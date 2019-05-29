export default function returnFlaskPost(message, state) {
  return fetch("http://localhost:5000/", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    method: "POST",
    body: JSON.stringify({
      message,
      state: {
        usedItems: state.usedItems,
        inventory: state.inventory,
        level: state.level,
        isBurned: state.isBurned,
        pinkPuzzleItems: state.pinkPuzzleItems
      }
    })
  }).then(response => {
    return response.json();
  });
}