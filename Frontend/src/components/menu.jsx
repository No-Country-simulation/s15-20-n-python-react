import { Link } from "react-router-dom"

export const Menu = (Props) => {
    const { text, image } = Props;
    return (
        <div className="flex items-center justify-center gap-2">
            <Link className="font-semibold text-2xl text-white active:text-pale-brown" to={`/${text}`} >
                {image}
            </Link>
            <Link className="font-semibold text-2xl text-white active:text-pale-brown" to={`/${text}`} >{text}</Link>
        </div>
    )
}