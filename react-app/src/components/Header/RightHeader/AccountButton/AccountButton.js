import styles from "./AccountButton.module.css";

import { useState, useEffect } from "react";
import { useSelector } from 'react-redux';

import AccountDropdown from "./AccountDropdown/AccountDropdown";

export default function AccountButton() {
    const [showMenu, setShowMenu] = useState(false);
    const user = useSelector(state => state.session.user);
    let timeoutId = null;
    const TIMEOUT_DELAY = 150;

    useEffect(() => {
        if (!showMenu) return;
        const closeMenu = () => setShowMenu(false);
        document.addEventListener('click', closeMenu);
        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    const onMouseEnter = (e) => {
        if (!timeoutId) {
            timeoutId = setTimeout(() => {
                const hovered = Array.from(document.querySelectorAll(":hover"));
                if (hovered.includes(document.querySelector("#accountButton"))) {
                    setShowMenu(true);
                }
                timeoutId = null;
            }, TIMEOUT_DELAY);
        }
    }

    const onMouseLeave = (e) => {
        if (!timeoutId) {
            timeoutId = setTimeout(() => {
                const hovered = Array.from(document.querySelectorAll(":hover"));
                if (!hovered.includes(document.querySelector("#accountButton")) &&
                    !hovered.includes(document.querySelector("#accountDropdown"))) {
                    setShowMenu(false);
                }
                timeoutId = null;
            }, TIMEOUT_DELAY);
        }
    }

    return (
        <>
            <div id="accountButton" className={styles.wrapper} onMouseEnter={onMouseEnter} onMouseLeave={onMouseLeave}>
                <div className={styles.row1}>Hello, {user ? user.fullname.split(" ")[0] : "sign in"}</div>
                <div className={styles.row2}>
                    <div className={styles.row2row1}>Account & Lists</div>
                    <img src={"/images/nav-arrow.png"} alt="▼" />
                </div>
            </div>
            {showMenu && <AccountDropdown delay={TIMEOUT_DELAY} setShowMenu={setShowMenu} />}
        </>
    );
}
