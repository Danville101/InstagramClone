import React, { useEffect } from 'react'
import {useState} from 'react'
import axios from "axios";
//import { loginUser } from '../../function/login'
import {useNavigate ,Navigate} from "react-router-dom"
const Login = () => {
     
     const [username, setUsername]= useState('')
     const [password, setPassword] = useState('')
     const [loggedIn, setLoggedIn] = useState(false)

     const navigate:any= useNavigate()

     /*const onClickHandler = async (e:React.SyntheticEvent)=>{
          e.preventDefault()
          
                await loginUser({
                    username: username,
                    password: password
               }).then((res:any)=>{
                    if(res){
                    setLoggedIn(true)}
               }).catch((err)=>{
                    alert(err)
               })
               
          
          
     }*/

     const newClickHandeler= async (e:React.SyntheticEvent)=>{
          e.preventDefault()
          await axios.post(
               'http://localhost:8000/api/user/login/',{
                    username: username,
                    password: password
               }
          ).then((res:any)=>{
               localStorage.setItem('Autherization',res.data.access)
               setLoggedIn(true)
          }).catch(()=>{

               alert("Please enter correct email or password")
          })

     }


     useEffect(()=>{
          if(localStorage.getItem("Autherization")){
               navigate("/")
          }
     },[])

     {if(loggedIn){
          return(<Navigate to="/"/>)
     }}

  return (
     <div>
     <form onSubmit={newClickHandeler}>
          <input type="text" placeholder="username" value={username} onChange={e=>{setUsername(e.target.value)}}/>
          <input type="password" placeholder="password" value={password} onChange={e=>{setPassword(e.target.value)}}/>
          <button type="submit" id="login">Log in</button>
     </form>

     <div id="signup-bar">
          <p>Don't have an account?</p> <a href="#">Sign up</a>
          
     </div>

</div>


   
  )
}

export default Login

