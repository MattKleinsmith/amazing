import styles from "./AccountButton.module.css";

import { useState, useEffect } from "react";
import { useSelector } from 'react-redux';

import AccountDropdown from "./AccountDropdown/AccountDropdown";

export default function AccountButton() {
    const [showMenu, setShowMenu] = useState(false);
    const ui = useSelector(state => state.ui);
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        if (!showMenu) return;
        const closeMenu = () => setShowMenu(false);
        document.addEventListener('click', closeMenu);
        return () => document.removeEventListener("click", closeMenu);
    }, [showMenu]);

    return (
        <>
            <div className={styles.wrapper} onClick={() => setShowMenu(true)}>
                <div className={styles.row1}>Hello, {user ? user.fullname : "Matthew"}</div>
                <div className={styles.row2}>Account & Lists</div>
                <img src={"/images/nav-arrow.png"} alt="▼" />
            </div>
            {showMenu && <AccountDropdown user={user} ui={ui} />}
        </>
    );
}
