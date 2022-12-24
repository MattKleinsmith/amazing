import styles from "./Quantity.module.css";

import { useRef } from "react";

export default function Quantity({ quantity, setQuantity }) {
    const ref = useRef();
    if (ref.current) ref.current.click();
    return (<>
        <select ref={ref} className={styles.wrapper}
            value={quantity} onChange={(e) => setQuantity(e.target.value)}>
            {[...Array(30).keys()].map(num => (
                <option key={num} value={num + 1}>
                    Qty: {num + 1}
                </option>))}
        </select>
    </>);
}
