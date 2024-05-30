import { useState } from "react"
import { Link } from "react-router-dom"
import apple from "../assets/img/apple.png"
import google from "../assets/img/google.png"


const Log = () => {
  
  const [name, setName] = useState("")
  const [password, setPassword] = useState("")

  const HandlerChange = (e, set) => {
    set(e.target.value)
  }
  
  const HandlerSubmit = async (e) => {
    e.preventDefault()

    // try {
    //   const response = await fetch('https://127.0.0.1:8000/user/token/', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify({
    //       username: 'algo',
    //       password: 'algo',
    //     }),
    //   });

    //   if (!response.ok) {
    //     throw new Error('Network response was not ok');
    //   }

    //   const result = await response.json()
    //   console.log(result)
    // } catch (error) {
    //   console.log(error.message)
    // } 
  }

    return (
      <div className="Register">

        <div className="Register__welcome">
          <p>Bienvenida de vuelta.</p>
          <p>Entra en tu cuenta</p>
        </div>
        
        <form className="form" action="POST" onSubmit={(e)=>{HandlerSubmit(e)}}>

          <div className="form--group">
            <label htmlFor="name">Tu nombre de usuario</label>
            <input onChange={(e)=>{HandlerChange(e, setName)}} value={name} type="text" name="name" />
          </div>

          <div className="form--group">
            <label htmlFor="password">Tu contraseña</label>
            <input onChange={(e)=>{HandlerChange(e, setPassword)}} value={password} type="password" name="password" />
          </div>

          <button type="submit">Entrar</button>

        </form>

        <div className="Register__plataform">

          <p>O entra con</p>

          <button>
            <img src={google} alt="" />
          </button>

          <button>
            <img src={apple} alt="" />
          </button>

        </div>

        <div className="Register__link">
          <p>¿No tienes una cuenta?</p>
          <Link to={"/auth/register"}>
           <p>Registráte</p>
          </Link>
        </div>

      </div>
    )
  }
  
  export { Log };
  