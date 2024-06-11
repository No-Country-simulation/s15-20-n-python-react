import { Link } from "react-router-dom"
import img1 from "../assets/img/trabajoEquipo.webp"
import img2 from "../assets/img/todolist.webp"
import logo from "../assets/img/logo.png"
import cal from "../assets/img/calendario.png"
import trabajo from "../assets/img/trabajo.png"
import user from "../assets/img/usuario.png"
import mundo from "../assets/img/mundo.png"
import instagram from "../assets/svg/instagram.svg"
import twitter from "../assets/svg/twitter.svg"
import youtube from "../assets/svg/youtube.svg"
import tiktok from "../assets/svg/tiktok.svg"




const Landing = () => {
    return (
      <div className="Landing">

        <header className="lHeader">

          <div className="lHeader__Logo">
            <img src={logo} alt="" />
            <div>
              <p>
                <span className="pLogo">P</span>roject
              </p>
              <p>
                <span className="mLogo">M</span>anagment
              </p>
              <p>
                <span className="lLogo">L</span>atam
              </p>
            </div>
          </div>

          <div className="lHeader__Nav">
            <Link to={"/auth/login"}>Inicia sesión</Link>
            <Link className="lHeader__Nav--SignUp" to={"/auth/register"}>Regístrate</Link>
          </div>

        </header>

        <div className="lSection1">
          <h1>Gestión de Proyectos para Latinoamérica</h1>
          <p>Simplifica la gestión de tus proyectos con nuestra herramienta innovadora.</p>
          <button>
            <Link to={"/auth/register"}>Empezar ahora</Link>
          </button>
        </div>

        <div className="lSection2">

          <div>
            <h2>Colaboración Eficiente</h2>
            <p>Mejora la comunicación y la colaboración en tu equipo con nuestras herramientas integradas.</p>
          </div>

          <img src={img1} alt="" />

        </div>

        <div className="lSection2 flex-reverse">

          <div>
            <h2>Gestión Visual</h2>
            <p>Visualiza el progreso de tus proyectos con tableros intuitivos y personalizables.</p>
          </div>

          <img src={img2} alt="" />
          
        </div>

        <div className="lSection3">

          <h2>Cualidades del proyecto</h2>

          <div className="lSection3__list">

            <div>
              <img src={user} alt="" />
              <h3>Tareas y Subtareas</h3>
              <p>Organiza tus proyectos dividiéndolos en tareas y subtareas fácilmente manejables.</p>
            </div>

            <div>
              <img src={cal} alt="" />
              <h3>Calendarios y Plazos</h3>
              <p>Mantén tus proyectos a tiempo con calendarios integrados y recordatorios de plazos.</p>
            </div>

            <div>
              <img src={mundo} alt="" />
              <h3>Integraciones</h3>
              <p>Conecta con tus herramientas favoritas como Slack, Google Drive, y más.</p>
            </div>

            <div>
              <img src={trabajo} alt="" />
              <h3>Informes y Análisis</h3>
              <p>Genera informes detallados y analiza el rendimiento de tu equipo en tiempo real.</p>
            </div>

          </div>

        </div>

        <div className="lSection4">
          <h2>Comienza a mejorar la gestión de tus proyectos hoy</h2>
          <p>Experimenta con unas de las mejores plataformas de gestion totalmente gratis</p>
          <button>
            <Link to={"/auth/register"}>Regístrate Gratis</Link>
          </button>
        </div>

        <div className="lSection5">
          <form className="lSection5__Contacto" method="post">
            <p className="lSection5__Contacto--Titulo">Contáctanos</p>
            <p className="lSection5__Contacto--Subtitulo">¿Tienes alguna pregunta? <br /> ¡Nos encantaría saber de ti!</p>

            <div className="lSection5__Contacto__Group1">

              <div className="form--group">
                <label htmlFor="first-name">Tu nombre</label>
                <input type="text" name="first-name" />
              </div>

              <div className="form--group">
                <label htmlFor="last-name">Tu apellido</label>
                <input type="text" name="last-name" />
              </div>

            </div>

            <div className="form--group lSection5__Contacto__Group2 ">
              <label htmlFor="email">Tu correo electronico</label>
              <input type="email" name="email" />
            </div>

            <div className="lSection5__Contacto__Group3">
              <label htmlFor="email">Tu Mensaje</label>
              <textarea name="" id=""></textarea>
            </div>

            <button className="lSection5__Contacto--button" type="submit">Enviar</button>

          </form>

          <div className="lSection5--Imagen"></div>
        </div>

        <footer className="lFooter">

          <div className="lFooter__cont1">

            <div className="lHeader__Logo">
              <img src={logo} alt="" />
              <div>
                <p>
                  <span className="pLogo">P</span>roject
                </p>
                <p>
                  <span className="mLogo">M</span>anagment
                </p>
                <p>
                  <span className="lLogo">L</span>atam
                </p>
              </div>
            </div>

            <div className="lFooter__redes">
              <p>Siguenos en nuestras redes:</p>
              <ul>
                <li><a href="http://"><img src={instagram} /></a></li>
                <li><a href="http://"><img src={twitter} /></a></li>
                <li><a href="http://"><img src={youtube} /></a></li>
                <li><a href="http://"><img src={tiktok} /></a></li>
              </ul>
            </div>


          </div>

          <div className="lFooter__cont2">

            <div className="lFooter__cont2__items">

              <p>Emails</p>
              <ul>
                <li><a href="http://">Pmlatam@gmail.com</a></li>
                <li><a href="http://">Pmlatam@hotmail.com.ar</a></li>
              </ul>

            </div>

            <div className="lFooter__cont2__items">

              <p>Sobre Nosotros</p>
              <ul>
                <li><a href="http://">Blog</a></li>
                <li><a href="http://">Soporte</a></li>
                <li><a href="http://">Política de Privacidad</a></li>
                <li><a href="http://">Términos de Servicio</a></li>
              </ul>
              
            </div>
            
          </div>

        </footer>

      </div>
    )
  }
  
  export { Landing };
  