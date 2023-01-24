import { NavLink } from "react-router-dom";
import styles from "./CartButton.module.css";

export default function CartButton() {
    return (
        <NavLink to="/cart" className={styles.wrapper}>
            <div className={styles.quantity}>0</div>
            <div className={styles.row}>
                <div className={styles.cart} />
                <div className={styles.label}>Cart</div>
            </div>
        </NavLink>
    );
}
