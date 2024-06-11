import { Landing } from "../pages/landing";
import { Register } from "../pages/register";
import { Log } from "../pages/log";
import { Routes, Route } from "react-router-dom";
import { Layout } from "../components/layout";
import { Tablero } from "../pages/tablero";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/proyectos" element={<Layout />}>
        <Route path="tablero" element={<Tablero />} />
      </Route>
      <Route path="/auth">
        <Route path="register" element={<Register />} />
        <Route path="login" element={<Log />} />
      </Route>
    </Routes>
  );
}

export default App;
