import React from 'react';
import './ChessBoard.css';

class ChessBoard extends React.Component {
  render() {
    const boardSize = 8;
    const squares = [];

    // Define the initial state of the board
    const boardState = [
      ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['', '', '', '', '', '', '', ''],
      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ];

    for (let row = 0; row < boardSize; row++) {
      for (let col = 0; col < boardSize; col++) {
        const squareColor = (row + col) % 2 === 0 ? 'white' : 'black';
        const piece = boardState[row][col];

        squares.push(
          <div key={`${row}-${col}`} className={`square ${squareColor}`}>
            {piece && <img src={`pieces/${piece}.png`} alt={piece} />}
          </div>
        );
      }
    }

    return (
      <div className="chess-board">
        {squares}
      </div>
    );
  }
}

export default ChessBoard;
