import React from "react";
import Urls from "../Urls";

const Content: React.FunctionComponent = () => {
    return (
        <main>
            <Urls/>
        </main>
    );
};

export default React.memo(Content);