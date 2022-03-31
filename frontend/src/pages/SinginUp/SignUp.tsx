import React from 'react'
import {useState} from "react"
import {createNewUser} from "../../function/signup"

const Signup = () => {

     

     const [email, setEmail]=useState("")
     const [fullname, setFullName]=useState("")
     const [password, setPassword]=useState("")
     const [username, setUsername]=useState("")

     const onClickHandler= async (e:React.SyntheticEvent) => {
          e.preventDefault();
          try{
               await createNewUser({
                    email: email,
                    fullname: fullname,
                    username: username,
                    password: password
                    
               }) 
          } catch (err) {
               console.log(err)
          }
     }

  return (
    <div>
         <form onSubmit={onClickHandler}>
              <input type="email" id="email" placeholder="Email" value={email} onChange={(e)=>setEmail(e.target.value) }/>
              <br/>
              <input type="text" id="fullname"  value={fullname}  placeholder="Fullname" onChange={(e)=>setFullName(e.target.value) }/>
              <br/>
              <input type="text" id="username" value={username} placeholder="Username" onChange={(e)=>setUsername(e.target.value) }/>
              <br/>
               <input type="password" id="password"  placeholder='Password' value={password} onChange={(e)=>{setPassword(e.target.value)}} />
               <button id="btn-next">Next</button>
         </form>


         <div id="login-bar">
              <p>Have an account?</p>
              <a href="#"> Log in</a></div>
         
    </div>
  )
}

export default Signup