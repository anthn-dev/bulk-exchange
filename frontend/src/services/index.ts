import axios from 'axios'

import type FormDataInterface from '../interfaces/Form'

const API_URL = process.env.REACT_APP_BACKEND_URL

export const register: FormDataInterface | any = async (formData: FormDataInterface) => {
  try {
    const response = await axios.post<FormDataInterface>(
      `${API_URL}user/register/`,
      {
        headers: {
          Accept: 'application/json'
        },
        ...formData
      }
    )

    return response
  } catch (error) {
    return error
  }
}

export const update: any = async (
  formData: FormDataInterface,
  token: string | null
) => {
  try {
    const response = await axios.patch<FormDataInterface>(
      `${API_URL}user/update/`,
      formData,
      {
        headers: {
          Accept: 'application/json',
          Authorization: `Token ${token}`
        }
      }
    )

    return response
  } catch (error) {
    return error
  }
}

export const getDetails: any = async () => {
  try {
    const response = await axios.get<FormDataInterface>(
      `${API_URL}user/details/`,
      {
        headers: {
          Accept: 'application/json',
          Authorization: `Token ${localStorage.getItem('token') ?? ''}`
        }
      }
    )

    return response
  } catch (error) {
    return error
  }
}

export const login: any = async (formData: FormDataInterface) => {
  try {
    const response = await axios.post<FormDataInterface>(
      `${API_URL}user/login/`,
      {
        headers: {
          Accept: 'application/json'
        },
        ...formData
      }
    )

    return response
  } catch (error) {
    return error
  }
}
