
import { Landing } from "../pages/landing"
import { Routes, Route } from 'react-router-dom';

function App() {


  return (
    <>
        <Routes>
            <Route path="/" element={<Landing />} />
        </Routes>
    </>
  )
}

export default App
