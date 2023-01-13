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
                    <a rel="noreferrer" target="_blank" href="https://www.linkedin.com/in/matthewkleinsmith/" className={styles.link}>
                        <img className={styles.linkedinIcon} src="https://d1irxr40exwge2.cloudfront.net/linkedin.png" alt="linkedin logo" />
                    </a>
                    <a rel="noreferrer" target="_blank" href="https://github.com/MattKleinsmith/" className={styles.link}>
                        <img className={styles.githubIcon} src="https://d1irxr40exwge2.cloudfront.net/github-logo.png" alt="github logo" />
                        <img className={styles.githubText} src="https://d1irxr40exwge2.cloudfront.net/github.png" alt="github text logo" />
                    </a>
                    <a rel="noreferrer" target="_blank" href="https://github.com/MattKleinsmith/amazing/" className={styles.link}><h2>Project repo</h2></a>
                </div>
            </div>
        </div>
    );
}
