import axios from "axios";
import {Url} from "../model/Models";

export const backendURL = process.env.REACT_APP_BACKEND_URL;
export const apiURL = `${backendURL}/api`;

export const api = axios.create({
    headers: {
        "Content-Type": "application/json;charset=utf-8"
    },
    baseURL: apiURL
});

export const urlApi = {
    list() {
        return api.get("url/", {withCredentials: true});
    },
    create(url: Url) {
        return api.post("url/", url, {withCredentials: true});
    }
};