import styles from "./AccountDropdown.module.css";

import { useDispatch } from 'react-redux';
import { NavLink, useNavigate } from 'react-router-dom';
import { signOut } from '../../../../../store/session';

export default function AccountDropdown({ delay, setShowMenu }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    let timeoutId = null;

    const onClickSignOut = () => {
        dispatch(signOut());
        navigate("/signin");
    };

    const onMouseLeave = (e) => {
        if (!timeoutId) {
            timeoutId = setTimeout(() => {
                const hovered = Array.from(document.querySelectorAll(":hover"));
                if (!hovered.includes(document.querySelector("#accountButton")) &&
                    !hovered.includes(document.querySelector("#accountDropdown"))) {
                    setShowMenu(false);
                }
                timeoutId = null;
            }, delay);
        }
    }

    return <>
        <div id="accountDropdown" className={styles.wrapper} onMouseLeave={onMouseLeave}>

            <NavLink to="/signin">Sign in</NavLink>

            <div className={styles.row}>
                <div className={styles.right}>
                    <div>row 1</div>
                </div>
            </div>

            <div className={styles.row}>
                <div className={styles.right}>
                    <div>row 2</div>
                </div>
            </div>

            <div className={`${styles.row} ${styles.signOut}`} onClick={onClickSignOut}>
                <div className={`${styles.right}`}>Sign out</div>
            </div>

        </div>

        <div className={styles.triangle} />

        <div className={styles.background} />
    </>;
}
