import React from 'react';
import './App.css';
import{BrowserRouter as Router, Routes, Route, Link, } from "react-router-dom"
import Signup from './pages/SinginUp/SignUp'
import Login from "./pages/Login/Login"
import Home from "./pages/Home/Home"


function App() {
  return (
    <Router>
    <Routes>
      <Route path="/signup" element={<Signup/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/" element={<Home/>}/>
    </Routes>
  </Router>
  );
}

export default App;
