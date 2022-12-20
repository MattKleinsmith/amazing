import styles from "./CartButton.module.css";

import { useNavigate } from "react-router";

export default function CartButton() {
    const navigate = useNavigate();
    return (
        <div className={styles.cartButton} onClick={() => navigate('/cart')} >
            <div className={styles.quantity}>0</div>
            <div className={styles.row}>
                <img src={"/images/cart.png"} alt={"cart"} />
                <div className={styles.label}>Cart</div>
            </div>
        </div>
    );
}
