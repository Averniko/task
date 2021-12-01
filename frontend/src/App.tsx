// @ts-ignore
import logo from 'logo.svg'
import './App.css';
import * as React from "react";
import Layout from "./components/containers/Layout";

export const App: React.FunctionComponent = () => {
    return (
        <div className="App">
            <Layout/>
        </div>
    );
}

export default App;
