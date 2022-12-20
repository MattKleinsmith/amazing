import styles from "./AccountDropdown.module.css";

import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { signOut } from '../../../../../store/session';

export default function AccountDropdown({ delay, setShowMenu }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    let timeoutId = null;

    const onClickSignOut = () => {
        dispatch(signOut());
        if (window.location.href.includes("your"))
            navigate("/");
    };

    const onMouseLeave = (e) => {
        console.log("LEFT");
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

            <div className={styles.row}>
                <div className={`${styles.iconWrapper}`}>
                    <i className={`fas fa-user-circle ${styles.profilePicture}`} />
                </div>
                <div className={styles.right}>
                    <div>row 1</div>
                    <div>row 2</div>
                </div>
            </div>

            <Link className={`${styles.row} ${styles.link}`} to='/your/purchases'>
                <div className={styles.iconWrapper}><i className={`fa-regular fa-clipboard`} /></div>
                <div className={`${styles.right} ${styles.purchases}`}>
                    Purchases and reviews
                </div>
            </Link>

            <div className={`${styles.row} ${styles.signOut}`} onClick={onClickSignOut}>
                <div className={styles.iconWrapper}>
                    <i className={`fa-solid fa-arrow-right-from-bracket`} />
                </div>
                <div className={`${styles.right}`}>Sign out</div>
            </div>

        </div>

        <img className={styles.triangle} src="/images/white-arrow.png" />

        <div className={styles.background} />
    </>;
}
