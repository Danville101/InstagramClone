import * as api from "../api/login"


interface Logindata{

     username: string
     password: string
}


export const loginUser = async (loginDetails: Logindata)=>{

     try {
          const {data} = await api.loginUser(loginDetails)
          localStorage.setItem("Autherization", data.access)
      
          
          
     } catch (error) {
          console.log(error)
          
     }

}