import styles from "./Quantity.module.css";

export default function Quantity({ quantity, setQuantity }) {
    return (<>
        <select className={styles.wrapper}
            value={quantity} onChange={(e) => setQuantity(e.target.value)}>
            {[...Array(20).keys()].map(num => (
                <option key={num} value={num + 1}>
                    Qty: {num + 1}
                </option>))}
        </select>
    </>);
}
