import React, { useState } from "react";

const houses = [
  { name: "Gryffindor", color: "red" },
  { name: "Slytherin", color: "green" },
  { name: "Hufflepuff", color: "yellow" },
  { name: "Ravenclaw", color: "blue" },
];

function App() {
  const [name, setName] = useState("");
  const [house, setHouse] = useState(null);

  const handleNameChange = (event) => {
    setName(event.target.value);
    // If name is empty, reset the house to null
    if (!event.target.value.trim()) {
      setHouse(null);
    }
  };

  const handleButtonClick = () => {
    // Generate a random house
    const randomHouse = houses[Math.floor(Math.random() * houses.length)];
    setHouse(randomHouse);
  };

  const handleClear = () => {
    setName("")
    setHouse(null)
  }

  return (
    <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh" }}>
      <div>
        <label>
          Enter your name:
          <input type="text" value={name} onChange={handleNameChange} />
        </label>
        <br />
        <button onClick={handleButtonClick}>Sort me into a house!</button>
        <br />
        <br />
        <button onClick={handleClear}>Clear</button>
        <br />
        {house && (
          <p style={{ background: house.color }}>
            <strong>Congratulations {name}, you have been sorted into {house.name}!!</strong>
          </p>
        )}
      </div>
    </div>
  );
}

export default App;
