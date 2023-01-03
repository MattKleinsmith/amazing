import styles from "./DeliveryTab.module.css";

import { useState } from "react";
import { useDispatch } from "react-redux";

import Price from "../../../Price/Price";
import Quantity from "../Quantity/Quantity";
import { postOrder } from "../../../../store/purchases"

export default function DeliveryTab({ product }) {
    const [quantity, setQuantity] = useState(1);

    const dispatch = useDispatch();

    const onBuyNow = async () => {
        const address = "my address from react";
        const cart = { [product.id]: quantity };
        try {
            const orderId = await dispatch(postOrder({ address, cart }));
            console.log("onBuyNow succeeded. Order id:", orderId);
        } catch (e) {
            console.log("onBuyNow failed:", e);
        }
    }

    return (<div className={styles.wrapper}>
        <div className={styles.price}>
            <Price product={product} />
            <div className={styles.count}>(${parseFloat(product.price).toFixed(2)} / Count)</div>
        </div>
        <div className={`prime ${styles.prime}`} />
        <div className={styles.freeReturns}>FREE Returns</div>
        <div className={styles.delivery}>FREE delivery <span className={styles.date}>Tuesday, December 27.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
        <div className={styles.address}></div>
        <div className={styles.inStock}>In Stock.</div>
        <Quantity quantity={quantity} setQuantity={setQuantity} />
        <div className={styles.addToCart}>Add to Cart</div>
        <div className={styles.buyNow} onClick={onBuyNow}>Buy Now</div>
        <div className={styles.secure}>
            <div className={styles.secureIconWrapper}>
                <img src="/images/secure.png" alt="Secure icon" height="15px" />
            </div>
            <div className={styles.secureText}>
                Secure transaction
            </div>
        </div>
        <div className={styles.details}>
            <div>
                <div className={styles.detailsLabel}>Ships from</div><div className={styles.detailsText}>Amazing</div>
            </div>
            <div>
                <div className={styles.detailsLabel}>Sold by</div><div className={styles.detailsText}>Amazing</div>
            </div>
            <div>
                <div className={styles.detailsLabel}>Packaging</div><div className={styles.detailsText}>Shows what's inside.</div>
            </div>
        </div>
    </div>);
}
