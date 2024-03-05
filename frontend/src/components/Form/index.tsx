import React from 'react'
import type { FormEvent } from 'react'

import AppButton from '../AppButton'
import Input from '../AppInput'

import type FormDataInterface from '../../interfaces/Form'

import './style.css'

interface FormProps {
  formData: FormDataInterface
  isLogin: boolean
  handleInputChange: (fieldName: string, value: string | number) => void
  handleSubmit: (event: FormEvent) => void
}

const Form: React.FC<FormProps> = ({ isLogin, formData, handleInputChange, handleSubmit }) => {
  return (
    <form className='form' onSubmit={handleSubmit}>
      {
        !isLogin &&
        <Input
          label='First Name'
          type="text"
          value={formData.first_name}
          onChange={(value) => { handleInputChange('first_name', value) }}
        />
      }

      {
        !isLogin &&
        <Input
          label='Surname'
          type="text"
          value={formData.last_name}
          onChange={(value) => { handleInputChange('last_name', value) }}
        />
      }

      {
        !isLogin &&
        <Input
          label='Phone'
          type="number"
          value={formData?.phone}
          onChange={(value) => { handleInputChange('phone', value) }}
        />
      }

      <Input
        label='Email'
        type="email"
        value={formData.email}
        onChange={(value) => { handleInputChange('email', value) }}
      />

      <Input
        label='Password'
        type='password'
        value={formData.password}
        onChange={(value) => { handleInputChange('password', value) }}
      />

      <AppButton title='Submit' type='submit' />
    </form>
  )
}

export default Form
