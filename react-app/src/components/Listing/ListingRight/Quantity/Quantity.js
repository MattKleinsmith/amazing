import styles from "./Quantity.module.css";

export default function Quantity({ quantity, setQuantity }) {
    return (<>

        <select
            value={quantity} onChange={(e) => setQuantity(e.target.value)}>
            {[...Array(30).keys()].map(num => (
                <option key={num} value={num + 1}>
                    {num + 1}
                </option>))}
        </select>

        <div className={styles.wrapper}>
            <span className={styles.quantityLabel}>Qty:</span>
            <span className={styles.quantity}>{quantity}</span>
            <span className={styles.iconWrapper}><span className={styles.icon}>⠀⠀</span></span>
        </div>
    </>);
}
