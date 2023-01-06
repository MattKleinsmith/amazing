import styles from "./AccountDropdown.module.css";

import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useNavigate } from 'react-router-dom';
import { signIn, signOut } from '../../../../../store/session';

export default function AccountDropdown({ delay, setShowMenu }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const user = useSelector(state => state.session.user);
    let timeoutId = null;

    const onClickSignOut = () => {
        dispatch(signOut());
        navigate("/signin");
    };

    const onDemo = () => {
        dispatch(signIn({ email: "email@email.com", password: "password" }));
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
            }, delay);
        }
    }

    return <>
        <div id="accountDropdown" className={user ? styles.wrapper : styles.wrapperSignedOut} onMouseLeave={onMouseLeave}>

            {!user && <div className={styles.signInWrapper}>
                <NavLink style={{ textDecoration: "none" }} to="/signin"><div className={`${styles.signIn}`}>Sign in</div></NavLink>
                <div style={{ textDecoration: "none" }} to="/signin"><div className={`${styles.signIn} ${styles.demo}`} onClick={onDemo}>Demo user</div></div>
                <div className={styles.new}>New customer? <NavLink to="/register">Start here.</NavLink></div>
            </div>
            }

            {user && <div className={styles.content}>
                <div className={styles.YourAccount}>Your Account</div>

                <NavLink className={styles.link} to="/inventory">Manage products</NavLink>

                <NavLink className={styles.link} to="/addresses">Manage addresses</NavLink>

                <NavLink className={styles.link} to="/orders">Manage orders</NavLink>

                <NavLink className={styles.link} to="/" onClick={onClickSignOut}>Sign out</NavLink>
            </div>}

        </div>

        <div className={styles.triangle} />

        <div className={styles.background} />
    </>;
}
