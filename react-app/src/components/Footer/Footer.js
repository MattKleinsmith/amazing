import styles from "./Footer.module.css"

import { useLocation } from "react-router"

export default function Footer() {
    const location = useLocation();
    const excludedPaths = ["signin", "register"];
    if (excludedPaths.some(path => location.pathname.includes(path)))
        return;
    return (
        <div className={styles.wrapper}>
            <div className={styles.footer}>
                <div className={styles.content}>
                    <a href="https://www.linkedin.com/in/matthewkleinsmith/" className={styles.link}>
                        <img className={styles.linkedinIcon} src="/images/linkedin.png" alt="linkedin logo" />
                    </a>
                    <a href="https://github.com/MattKleinsmith/" className={styles.link}>
                        <img className={styles.githubIcon} src="/images/github-logo.png" alt="github logo" />
                        <img className={styles.githubText} src="/images/github.png" alt="github text logo" />
                    </a>
                    <a href="https://github.com/MattKleinsmith/amazing/" className={styles.link}><h2>Project repo</h2></a>
                </div>
            </div>
        </div>
    );
}
