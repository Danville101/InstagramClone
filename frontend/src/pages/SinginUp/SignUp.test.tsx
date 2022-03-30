import React from 'react'
import Signup from './SignUp'
import {shallow} from 'enzyme'



describe('Testing the SignUp Page', () => {
     let wrapper ;
     beforeEach(() => {
          wrapper = shallow(<Signup/>)
     });

     test("render a button with the text of next",()=>{
          expect(wrapper.find("#btn-next").text()).toBe('Next')
     })


})