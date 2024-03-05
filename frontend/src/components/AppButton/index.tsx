import React from 'react'
import './style.css'

interface InputProps {
  title: string
  type: 'submit' | 'button'
  onClick?: (event: React.FormEvent) => void
}

const AppButton: React.FC<InputProps> = ({ title, type, onClick }) => {
  return (
    <div className='button-container'>
      <button
          className='button'
          type={type}
          onClick={onClick}
        >
          {title}
        </button>
    </div>
  )
}

export default AppButton
