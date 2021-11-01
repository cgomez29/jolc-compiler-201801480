import { Footer } from "./components/Footer/Footer";
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Home } from "./page/home/Home";
import { Analyze } from "./page/analyze/Analyze";
import { Report } from "./page/report/Report";
import { Navbar } from "./components/Navbar/Navbar";
import { UserContext } from "./context/UserContext";
import "bootswatch/dist/lux/bootstrap.min.css";

const App = () => {
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");
  const [err, setErr] = useState("");
  const [symbols, setSymbols] = useState("");

  return (
    <Router>
      <UserContext.Provider
        value={{
          inputText,
          setInputText,
          outputText,
          setOutputText,
          err,
          setErr,
          symbols,
          setSymbols,
        }}
      >
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/analyze" component={Analyze} />
          <Route exact path="/report" component={Report} />
        </Switch>
        <Footer />
      </UserContext.Provider>
    </Router>
  );
};

export default App;
