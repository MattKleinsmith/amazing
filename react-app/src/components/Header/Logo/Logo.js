import styles from "./Logo.module.css"

import { NavLink } from "react-router-dom"

export default function Logo() {
    return (
        <NavLink className={styles.wrapper} to="/" style={{ textDecoration: 'none' }}>
            <img className={styles.logo} src="/images/logo_white.png" alt="logo_white" />
            <div className={styles.prime} />
        </NavLink>
    )
}
