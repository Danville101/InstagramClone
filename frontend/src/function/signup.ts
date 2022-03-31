import * as api from "../api/signup"
interface SignupData{
     email: string
     fullname: string
     username: string
     password: string

}


export const createNewUser = async (newuser: SignupData) => {
     try {
       const { data } = await api.createNewUser(newuser);
       return data;
     } catch (error) {
       console.log(error);
     }
   };