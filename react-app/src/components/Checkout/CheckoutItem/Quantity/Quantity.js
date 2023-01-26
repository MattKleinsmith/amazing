import styles from "./Quantity.module.css";

import { useDispatch } from "react-redux";
import { putCartItem } from "../../../../store/cartItems";

export default function Quantity({ productId, quantity }) {
    const dispatch = useDispatch();

    return (<>
        <select
            className={styles.wrapper}
            value={quantity}
            onChange={(e) => dispatch(putCartItem(productId, e.target.value))}
        >
            {[...Array(20).keys()].map(num => (<option key={num} value={num + 1}>Qty: {num + 1}</option>))}
        </select>
    </>);
}
