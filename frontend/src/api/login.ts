import axios from "axios";

const url: string = 'http://localhost:8000/api/user/login/'

interface Logindata{

     username: string
     password: string
}

export const loginUser = (loginDetails:Logindata)=>axios.post(url, loginDetails)
