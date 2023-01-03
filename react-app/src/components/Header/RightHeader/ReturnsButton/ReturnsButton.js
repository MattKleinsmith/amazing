import styles from "./ReturnsButton.module.css";

import { NavLink } from "react-router-dom";
import { useState, useEffect } from "react";

export default function ReturnsButton() {
    const [showMenu, setShowMenu] = useState(false);

    useEffect(() => {
        if (!showMenu) return;
        const closeMenu = () => setShowMenu(false);
        document.addEventListener('click', closeMenu);
        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    return (
        <NavLink style={{ textDecoration: "none" }} to="/orders">
            <div className={styles.wrapper} onClick={() => setShowMenu(true)}>
                <div className={styles.row1}>Returns</div>
                <div className={styles.row2}>& Orders</div>
            </div>
        </NavLink>
    );
}
