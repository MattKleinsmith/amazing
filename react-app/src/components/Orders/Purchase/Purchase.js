import styles from "./Purchase.module.css";

export default function Purchase({ purchase }) {
    const createdAt = (new Date(purchase.created_at)).toLocaleDateString('en-us', { year: "numeric", month: "long", day: "numeric" });;

    return (
        <div className={styles.wrapper}>
            <div className={styles.top}>
                <div className={styles.left}>
                    <div>
                        <div className={styles.label}>ORDER PLACED</div>
                        <div className={styles.value}>{createdAt}</div>
                    </div>
                    <div>
                        <div className={styles.label}>TOTAL</div>
                        <div className={styles.value}>${parseFloat(purchase.price * purchase.quantity).toFixed(2)}</div>
                    </div>
                    <div>
                        <div className={styles.label}>SHIP TO</div>
                        <div className={styles.value}>{purchase.address.split('\n')[0]}</div>
                    </div>
                </div>
                <div className={styles.label}>
                    ORDER # {purchase.order_id}
                </div>
            </div>
        </div>
    );
}
