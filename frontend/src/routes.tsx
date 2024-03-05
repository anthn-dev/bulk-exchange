import React from 'react'
import {
  createBrowserRouter
} from 'react-router-dom'
import Register from './pages/Register'
import Login from './pages/Login'

const token = localStorage.getItem('token')

const router = createBrowserRouter([
  {
    path: '/',
    element: <Register token={token} />
  },
  {
    path: '/login',
    element: <Login />
  }
])

export default router
