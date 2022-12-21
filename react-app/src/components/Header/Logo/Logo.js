import { NavLink } from "react-router-dom"
import styles from "./Logo.module.css"

export default function Logo() {
    return (
        <NavLink className={styles.wrapper} to="/" style={{ textDecoration: 'none' }}>
            <img src="/images/logo_white.png" />
        </NavLink>
    )
}
