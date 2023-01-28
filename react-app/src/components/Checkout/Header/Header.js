import styles from "./Header.module.css";

import { NavLink } from "react-router-dom";

export default function Header({ numItems }) {
    return <div className={styles.headerWrapper}>
        <div className={styles.header}>
            <NavLink to="/" className={styles.logo}><img src="https://d1irxr40exwge2.cloudfront.net/logo_black.png" alt="logo_black" /></NavLink>
            <div className={styles.checkout}>Checkout <span className={styles.checkoutItem}>(<NavLink to="/cart" className={styles.checkoutLink}>{numItems} item{numItems > 1 && "s"}</NavLink>)</span></div>
            <div className={styles.secureIconWrapper}>
                <img src="https://d1irxr40exwge2.cloudfront.net/secure.png" alt="Secure icon" height="20px" />
            </div>
        </div>
    </div>
}
