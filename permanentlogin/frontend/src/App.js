import React from "react";
import axios from "axios";

function App() {
  const onClickHandler = async () => {
    try {
      console.log(
        await axios({
          url: "http://127.0.0.1:8000/users/",
          method: "get",
        })
      );
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div className="App">
      <button onClick={onClickHandler}>GET</button>
    </div>
  );
}

export default App;
