import { Link } from "react-router-dom";

export const Menu = (Props) => {
  const { text, image } = Props;
  return (
    <div className="flex items-center justify-center gap-2">
      <Link
        className="font-semibold text-2xl text-white hover:text-pale-brown"
        to={`/proyectos/${text.toLowerCase()}`} // Asegúrate de que las rutas son correctas
      >
        <div className="flex justify-center items-center gap-3">
          {image}
          {text}
        </div>
      </Link>
    </div>
  );
};
