import { useLocation } from "react-router"

export default function Footer() {
    const location = useLocation();
    if (location.pathname.includes("signin")) {
        return;
    }
    return "Footer component"
}
