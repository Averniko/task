import React, {useEffect, useState} from 'react'
import {Url} from "../model/Models";
import {backendURL, urlApi} from "../utils/Api";

const Urls: React.FunctionComponent = () => {
    const [subpartField, setSubpart] = useState<string>("");
    const [redirectField, setRedirect] = useState<string>("");
    const [urls, setUrls] = useState<Url[]>([]);
    const [error, setError] = useState<string>("");

    useEffect(() => {
        urlApi.list()
            .then(response => {
                console.log(response.data)
                setUrls(response.data.results)
            })
            .catch(console.log);
    }, []);

    const handleChangeSubpart = (event: any) => {
        event.preventDefault();
        setSubpart(event.target.value)
    }

    const handleChangeUrl = (event: any) => {
        event.preventDefault();
        setRedirect(event.target.value)
    }

    const handleSubmit = (event: any) => {
        event.preventDefault();
        const url: Url = {subpart: subpartField, redirect: redirectField}
        urlApi.create(url)
            .then(response => {
                setUrls([{subpart: response.data.subpart, redirect: response.data.redirect}, ...urls])
                setError("")
                console.log(response)
            })
            .catch(error => {
                if (error.response && error.response.status == 400) {
                    setError(JSON.stringify(error.response.data))
                } else {
                    console.log('Error', error.message)
                }
            });
    }

    const items: any[] = [];

    urls.forEach((url) => {
        items.push(<tr>
            <td><a href={`http://localhost/url/${url.subpart}`}>{`http://localhost/url/${url.subpart}`}</a></td>
            <td><a href={url.redirect}>{url.redirect}</a></td>
        </tr>)
    });

    return (
        <React.Fragment>
            <form className="text-lg-start" onSubmit={handleSubmit}>
                <div className="form-group m-2">
                    <label htmlFor="inputSubpart">Subpart</label>
                    <input type="text" className="form-control" id="inputSubpart"
                           placeholder="Enter subpart" onChange={handleChangeSubpart}/>
                </div>
                <div className="form-group m-2">
                    <label htmlFor="inputUrl">Url</label>
                    <input type="text" className="form-control" id="inputUrl"
                           placeholder="Enter url" onChange={handleChangeUrl}/>
                </div>
                <button type="submit" className="btn btn-primary m-2">Submit</button>
            </form>
            {error && <div className="alert alert-danger">
                {error}
            </div>}
            <table className="table">
                <thead>
                <tr>
                    <th scope="col">Short url</th>
                    <th scope="col">Url</th>
                </tr>
                </thead>
                <tbody>
                {items}
                </tbody>
            </table>
        </React.Fragment>
    )
};

export default Urls