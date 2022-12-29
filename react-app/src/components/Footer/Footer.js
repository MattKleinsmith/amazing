import { useLocation } from "react-router"

export default function Footer() {
    const location = useLocation();
    const excludedPaths = ["signin", "register"];
    if (excludedPaths.some(path => location.pathname.includes(path)))
        return;
    return "Footer component";
}
