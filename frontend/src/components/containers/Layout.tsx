import React from 'react'
import Content from "./Content";

const Layout: React.FunctionComponent = () => {

    return (
        <div>
            {/*<Sidebar/>*/}
            <div>
                {/*<Header/>*/}
                <div className="container">
                    <Content/>
                </div>
                {/*<Footer/>*/}
            </div>
        </div>
    )
};

export default Layout