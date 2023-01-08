import styles from "./LinksBar.module.css"

import { NavLink } from "react-router-dom"

export default function LinksBar() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.linksWrapper}>
                <NavLink className={styles.link} to="/s?k=toothbrush">Toothbrushes</NavLink>
                <NavLink className={styles.link} to="/s?k=phone">Phones</NavLink>
                <NavLink className={styles.link} to="/s?k=basics">Amazon Basics</NavLink>
                <NavLink className={styles.link} to="/s?k=makeup">Makeup</NavLink>
            </div>
        </div>
    )
}
