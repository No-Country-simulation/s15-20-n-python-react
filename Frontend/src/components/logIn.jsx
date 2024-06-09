import { useState } from 'react'
import reactLogo from '../assets/react.svg'
import viteLogo from '../assets/vite.svg'

function LogIn() {

  const [name, setName] = useState("")
  const [password, setPassword] = useState("")
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  
  const HandlerChange = (e, set) => {
    console.log(e.target.value)
    set(e.target.value)
  }
  
  const HandlerSubmit = async (e) => {
    e.preventDefault()

    try {
      const response = await fetch('https://127.0.0.1:8000/user/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: 'algo',
          password: 'algo',
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await response.json()
      console.log(result)
    } catch (error) {
      console.log(error.message)
    } 
  }


  return (
    <>
      <form action="POST" onSubmit={(e)=>{HandlerSubmit(e)}}>

        <div>
          <label htmlFor="name">Nombre</label>
          <input onChange={(e)=>{HandlerChange(e, setName)}} value={name} type="text" name="name" />
        </div>

        <div>
          <label htmlFor="password">Contraseña</label>
          <input onChange={(e)=>{HandlerChange(e, setPassword)}} value={password} type="password" name="password" />
        </div>

        <input type="submit" />

      </form>
    </>
  )
}

export {LogIn}
