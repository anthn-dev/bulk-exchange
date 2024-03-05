import React, { useState, useEffect } from 'react'

import { useNavigate } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify'

import AppButton from '../../components/AppButton'
import Form from '../../components/Form'

import type FormDataInterface from '../../interfaces/Form'
import type LoginToken from '../../interfaces/Login'
import { getDetails, register, update } from '../../services'

import 'react-toastify/dist/ReactToastify.css'
import './style.css'

const App: React.FC<LoginToken> = ({ token }) => {
  const navigate = useNavigate()
  const [formData, setFormData] = useState<FormDataInterface>({
    first_name: '',
    last_name: '',
    phone: '',
    email: '',
    password: ''
  })

  const [loading, setLoading] = useState(true)

  const handleInputChange: any = (fieldName: string, value: string | number) => {
    setFormData((prevData) => ({
      ...prevData,
      [fieldName]: value
    }))
  }

  useEffect(() => {
    const getUserDetails: any = async () => {
      const response: FormDataInterface | any = await getDetails()
      setLoading(false)
      if (response.status === 200) {
        setFormData((pre) => {
          return {
            ...pre,
            first_name: response.data.first_name,
            last_name: response.data.last_name,
            phone: response.data.phone,
            email: response.data.email
          }
        })
      }
    }
    getUserDetails().then()
  }, [])

  const handleSubmit: any = async (event: React.FormEvent) => {
    event.preventDefault()
    setLoading(true)
    const response: FormDataInterface | any = token
      ? await update(formData, token)
      : await register(formData)
    setLoading(false)
    if (response.status === 200) {
      toast.success('Account updated successfully!')
      setFormData((pre) => {
        return {
          ...pre,
          password: ''
        }
      })
    } else if (response.status === 201) {
      toast.success('Account created successfully!')
      setTimeout(() => {
        navigate('/login')
      }, 500)
    } else {
      const errors = response?.response?.data || {}
      if (Object.values(errors).length > 0) {
        const error: any = Object.values(errors)[0]
        toast.error(typeof error === 'string' ? error : error[0])
      }
    }
  }

  const logout: any = (event: React.FormEvent) => {
    event.preventDefault()
    localStorage.clear()
    navigate('/login')
  }

  return (
    <div>
      <ToastContainer />
      {
        loading
          ? <div className='spinner'></div>
          : (
            <div>
              <h1 className='heading'>
                {token ? 'Update Account' : 'Create Account'}
              </h1>
              {!token && (
                <p className='heading'>
                  Already have an account? <a href='/login'>Login</a>
                </p>
              )}
              <Form
                isLogin={false}
                formData={formData}
                handleInputChange={handleInputChange}
                handleSubmit={handleSubmit}
              />
              {token && <AppButton title='Logout' type='button' onClick={logout} />}
            </div>
            )
      }
    </div>
  )
}

export default App
