import img1 from "../assets/img/template-img1.webp"
import img2 from "../assets/img/template-img2.webp"


const Landing = () => {
    return (
      <div className="Landing">

        <header className="lHeader">

          <div className="lHeader__Logo">
            <p>Site name</p>
          </div>

          <div className="lHeader__Nav">
            <a href="http://">Log In</a>
            <a className="lHeader__Nav--SignUp" href="http://">Sign Up</a>
          </div>

        </header>

        <div className="lSection1">
          <h1>Landing page title</h1>
          <p>And a subheading describing your site, too</p>
          <button>button</button>
        </div>

        <div className="lSection2">

          <div>
            <h2>Heading</h2>
            <p>A subheading for this section, as long or as short as you like</p>
          </div>

          <img src={img1} alt="" />

        </div>

        <div className="lSection2 flex-reverse">

          <div>
            <h2>Heading</h2>
            <p>Another subheading—maybe it’s related to the image on the left, or the button below </p>
          </div>

          <img src={img2} alt="" />
          
        </div>

        <div className="lSection3">

          <h2>Heading</h2>

          <div className="lSection3__list">

            <div>
              <h3>Subheading</h3>
              <p>Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story. </p>
            </div>

            <div>
              <h3>Subheading</h3>
              <p>Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story. </p>
            </div>

            <div>
              <h3>Subheading</h3>
              <p>Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story. </p>
            </div>

            <div>
              <h3>Subheading</h3>
              <p>Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story. </p>
            </div>

          </div>

        </div>

        <div className="lSection4">
          <h2>Heading</h2>
          <p>Plus a subheading for your site’s footer</p>
          <button>button</button>
        </div>

        <footer className="lFooter">

          <div className="lFooter__cont1">

            <p>Site Name</p>

            <ul>
              <li><a href="http://"><img src="" /></a></li>
              <li><a href="http://"><img src="" /></a></li>
              <li><a href="http://"><img src="" /></a></li>
              <li><a href="http://"><img src="" /></a></li>
            </ul>

          </div>

          <div className="lFooter__cont2">

            <div className="lFooter__cont2__items">

              <p>Topic</p>
              <ul>
                <li><a href="http://">Page</a></li>
                <li><a href="http://">Page</a></li>
                <li><a href="http://">Page</a></li>
              </ul>

            </div>

            <div className="lFooter__cont2__items">

              <p>Topic</p>
              <ul>
                <li><a href="http://">Page</a></li>
                <li><a href="http://">Page</a></li>
                <li><a href="http://">Page</a></li>
              </ul>
              
            </div>
            
          </div>

        </footer>

      </div>
    )
  }
  
  export { Landing };
  