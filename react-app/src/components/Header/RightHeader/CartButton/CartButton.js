import styles from "./CartButton.module.css";

export default function CartButton() {
    return (
        <div className={styles.cartButton} >
            <div className={styles.quantity}>0</div>
            <div className={styles.row}>
                <img src={"/images/cart.png"} alt={"cart"} />
                <div className={styles.label}>Cart</div>
            </div>
        </div>
    );
}
