import styles from "./LinksBar.module.css"

import { NavLink } from "react-router-dom"

export default function LinksBar() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.linksWrapper}>
                <NavLink className={styles.link} to="/s?k=toothbrush">Toothbrushes</NavLink>
            </div>
        </div>
    )
}
