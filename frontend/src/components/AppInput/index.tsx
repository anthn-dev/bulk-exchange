import React from 'react'
import type { ChangeEvent } from 'react'

import type InputProps from '../../interfaces/AppInput'

import './style.css'

const AppInput: React.FC<InputProps> = ({ label, value, type, onChange }) => {
  const handleInputChange: any = (event: ChangeEvent<HTMLInputElement>) => {
    const inputValue = event.target.value
    const parsedValue = type === 'number' ? parseFloat(inputValue) : inputValue
    if (type === 'text') {
      const onlyAlphabets = /^[a-zA-Z]+$/

      if (onlyAlphabets.test(parsedValue.toString()) || parsedValue === '') {
        onChange(parsedValue)
      }
    } else {
      onChange(parsedValue)
    }
  }

  return (
    <div className='field'>
      <label>
        {label}
        <br />
        <input
          className='app-input'
          type={type}
          value={value}
          onChange={handleInputChange}
          required
        />
      </label>
    </div>
  )
}

export default AppInput
