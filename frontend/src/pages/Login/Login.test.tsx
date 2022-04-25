import React from 'react'
import Login from './Login'
import {shallow} from 'enzyme'


describe('Login', () => {

     let wrapper: any;

     beforeEach(() => {
          wrapper = shallow(<Login/>)
     })
     const credentials = {
          username:"testCause101",
          password:"Test303101"}

     test('should render Instagram',()=>{
          
          const usernameInput= wrapper.find("#username")
          usernameInput.value = credentials.username
          expect(usernameInput.value).toBe("testCause101")

          const passwordInput = wrapper.find("#password")
          passwordInput.value = credentials.password
          expect(passwordInput.value).toBe("Test303101")

     })

     test('should renderd login',()=>{

          expect(wrapper.find("#login").text()).toBe("Log in")

     })

     test("Login button should be clickable",()=>{
          const handleSubmit = jest.fn();
          const login = wrapper.find("#login")
          login.simulate("click")
          expect(handleSubmit).toHaveBeenCalled
     } )

     test("Signup Bar",()=>{
          expect(wrapper.find("#signup-bar").text()).toBe("Don't have an account? Sign up")
     })
})