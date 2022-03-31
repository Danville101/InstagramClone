import React from 'react'
import Signup from './SignUp'
import {shallow} from 'enzyme'
import userEvent from '@testing-library/user-event';



describe('Testing the SignUp Page', () => {
     let wrapper:any ;
     beforeEach(() => {
          wrapper = shallow(<Signup/>)
     });


     const credentials = {
     email:"test@example.com",
     fullname:"Mr Test",
     username:"testCause101",
     password:"Test303101"}

     test("render a button with the text of next",()=>{
          expect(wrapper.find("#btn-next").text()).toBe('Next')
     })


     test("valid email is passed to email field",()=>{
          
          const emailInput = wrapper.find("#email")
          emailInput.value = credentials.email
          expect(emailInput.value).toBe('test@example.com')


          const fullnameInput= wrapper.find("#fullname")
          fullnameInput.value = credentials.fullname
          expect(fullnameInput.value).toBe("Mr Test")

          const usernameInput= wrapper.find("#username")
          usernameInput.value = credentials.username
          expect(usernameInput.value).toBe("testCause101")

          const passwordInput = wrapper.find("#password")
          passwordInput.value = credentials.password
          expect(passwordInput.value).toBe("Test303101")
     })

     test("validates model on button click",()=>{
          const handleSubmit = jest.fn();
          const signup = wrapper.find("#btn-next")
          signup.simulate("click")
          expect(handleSubmit).toHaveBeenCalled
     })

     test(" render login bar", ()=>{

          expect(wrapper.find("#login-bar").text()).toBe("Have an account? Log in")


     })

})