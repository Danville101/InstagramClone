import React from 'react';
import './App.css';
import{BrowserRouter as Router, Routes, Route, Link} from "react-router-dom"
import Signup from './pages/SinginUp/SignUp'


function App() {
  return (
    <Router>
    <Routes>
      <Route path="/signup" element={<Signup/>}/>

    </Routes>
  </Router>
  );
}

export default App;
