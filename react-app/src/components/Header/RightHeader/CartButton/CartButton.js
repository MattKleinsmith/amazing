import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import styles from "./CartButton.module.css";

export default function CartButton() {
    const cartItems = useSelector(state => state.cartItems);
    const quantities = Object.values(cartItems);
    const totalQuantity = quantities.reduce((sum, quantity) => sum += quantity, 0);

    return (
        <NavLink to="/cart" className={styles.wrapper}>
            <div className={totalQuantity < 10 ? styles.quantity : styles.largeQuantity}>{totalQuantity}</div>
            <div className={styles.row}>
                <div className={styles.cart} />
                <div className={styles.label}>Cart</div>
            </div>
        </NavLink>
    );
}
