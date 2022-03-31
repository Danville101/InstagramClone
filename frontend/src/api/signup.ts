import axios from "axios";

const url :string="http://localhost:8000/api/user/signup/"

interface SignupData{
     email: string
     fullname: string
     username: string
     password: string

}

export const createNewUser = (newuser: SignupData) =>axios.post(url,newuser)