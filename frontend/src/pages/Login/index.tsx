import React, { useState } from 'react'

import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

import { useNavigate } from 'react-router-dom'

import Form from '../../components/Form'
import type LoginToken from '../../interfaces/Login'
import { login } from '../../services'
import type FormDataInterface from '../../interfaces/Form'
import AppButton from '../../components/AppButton'

const Login: React.FC = () => {
  const navigate = useNavigate()
  const [formData, setFormData] = useState<FormDataInterface>({
    email: '',
    password: ''
  })
  const [loading, setLoading] = useState(false)

  const handleInputChange: any = (fieldName: string, value: string | number) => {
    setFormData((prevData) => ({
      ...prevData,
      [fieldName]: value
    }))
  }

  const handleSubmit: any = async (event: React.FormEvent) => {
    event.preventDefault()
    setLoading(true)
    const response: LoginToken | any = await login(formData)
    setLoading(false)
    if (response.status === 200) {
      toast.success('Login Successfull!')
      const token = response?.data?.token || ''
      localStorage.setItem('token', token)
      navigate('/')
    } else {
      const errors = response?.response?.data || {}
      if (Object.values(errors).length > 0) {
        const error: any = Object.values(errors)[0]
        toast.error(typeof (error) === 'string' ? error : error[0])
      }
    }
  }

  const back: any = (event: React.FormEvent) => {
    event.preventDefault()
    navigate('/')
  }

  return (
    <div>
      <ToastContainer />
      <h1 className='heading'>Login</h1>
      {
        loading
          ? <div className='spinner'></div>
          : <Form
            isLogin={true}
            formData={formData}
            handleInputChange={handleInputChange}
            handleSubmit={handleSubmit}
          />
      }
      <AppButton title='Back' type='button' onClick={back} />
    </div>
  )
}

export default Login
