import styles from "./LinksBar.module.css"

import { NavLink } from "react-router-dom"

export default function LinksBar() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.linksWrapper}>
                <NavLink className={styles.link} to="/s?k=toothbrushes">Toothbrushes</NavLink>
                <NavLink className={styles.link} to="/s?k=phones">Phones</NavLink>
                <NavLink className={styles.link} to="/s?k=basics">Amazing Basics</NavLink>
                <NavLink className={styles.link} to="/s?k=makeup">Makeup</NavLink>
                <a rel="noreferrer" target="_blank" className={styles.link} href="https://www.linkedin.com/in/matthewkleinsmith/">LinkedIn</a>
                <a rel="noreferrer" target="_blank" className={styles.link} href="https://github.com/MattKleinsmith/">GitHub</a>
                <a rel="noreferrer" target="_blank" className={styles.link} href="https://github.com/MattKleinsmith/amazing/">Project repo</a>
                <a rel="noreferrer" target="_blank" className={styles.link} href="mailto:mwksmith@gmail.com">Email</a>
                <a rel="noreferrer" target="_blank" className={styles.link} href="https://mattkleinsmith.github.io/">Portfolio</a>
            </div>
        </div>
    )
}
