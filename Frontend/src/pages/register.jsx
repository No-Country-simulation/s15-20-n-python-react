import { useState } from "react"
import { Link } from "react-router-dom"
import apple from "../assets/img/apple.png"
import google from "../assets/img/google.png"
import tillde from "../assets/img/tilde.png"


const Register = () => {
  
  const [name, setName] = useState("")
  const [password, setPassword] = useState("")

  const HandlerChange = (e, set) => {
    console.log(e.target.value)
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
          <p>Te damos la bienvenida.</p>
          <p>Crea tu cuenta</p>
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

          <button type="submit">Registrarse</button>

        </form>

        <div className="Register__plataform">

          <p>O continúa con</p>

          <button>
            <img src={google} alt="" />
          </button>

          <button>
            <img src={apple} alt="" />
          </button>

        </div>

        <div className="Register__link">
          <p>¿Ya tienes una cuenta?</p>
          <Link to={"/auth/login"}>
           <p>Inicia sesión</p>
          </Link>
        </div>

        <div className="Register__benefits">

          <div>
            <img src={tillde} alt="" />
            <p>Obtiene acceso ilimitado a tareas, proyectos y almacenamiento.</p>
          </div>

          <div>
            <img src={tillde} alt="" />
            <p>Usa vistas diferentes de lista, tablero o calendario.</p>
          </div>

          <div>
            <img src={tillde} alt="" />
            <p>Invita a tus compañeros de equipo a explorar nuestra propuesta.</p>
          </div>

        </div>

        <p className="Register--conditions">Al registrarte, aceptas nuestras <span>Condiciones de Uso</span> y <span>Política de Privacidad.</span> </p>

      </div>
    )
  }
  
  export { Register };
  