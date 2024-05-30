
import { Landing } from "../pages/landing"
import { Register } from "../pages/register";
import { Routes, Route } from 'react-router-dom';

function App() {


  return (
    <>
        <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/auth" >
              <Route path="register" element={<Register />} />
            </Route>
        </Routes>
    </>
  )
}

export default App
