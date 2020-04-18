import React from "react";
import "./App.css";
import { Widget } from "rasa-webchat";

function App() {
  return (
    <div className="App">
      <div className="AppHeader">
        <Widget
          interval={2000}
          socketUrl={"http://localhost:5005"}
          socketPath={"/socket.io/"}
          title={"Nora"}
          inputTextFieldHint={"Type a message..."}
          connectingText={"Waiting for server..."}
          openLauncherImage="logo-1.svg"
          profileAvatar="logo-white.svg"
          embedded={true}
          params={{
            images: {
              dims: {
                width: 500,
                height: 500,
              },
            },
            storage: "local",
          }}
        />
      </div>
    </div>
  );
}

export default App;
