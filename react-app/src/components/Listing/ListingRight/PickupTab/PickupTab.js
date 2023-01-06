import styles from "./PickupTab.module.css";

import { useState } from "react";

import Quantity from "../Quantity/Quantity";

export default function PickupTab({ product }) {
    const [quantity, setQuantity] = useState(1);

    let deliveryDate = new Date();
    deliveryDate.setDate(deliveryDate.getDate() + 2);
    deliveryDate = deliveryDate.toLocaleDateString('en-us', { weekday: "long", month: "long", day: "numeric" });

    return (<div className={styles.wrapper}>
        <div className={styles.price}>${parseFloat(product.price).toFixed(2)}</div>
        <div className={styles.delivery}>FREE pickup <span className={styles.date}>{deliveryDate}.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
        <div className={styles.hr} />
        <div className={styles.pickUpLabel}>Pick up at:</div>
        <div className={styles.pickUpLocationWrapper}>
            <div className={styles.pickUpLocation}><span className={styles.locker}>Amazing Hub Locker - Track | </span><span className={styles.distance}>0.08 mi</span></div>
        </div>
        <div className={styles.inStock}>In Stock.</div>
        <Quantity quantity={quantity} setQuantity={setQuantity} />
        <div className={styles.buyNow}>Buy Now</div>
        <div className={styles.details}>
            <div>
                <div className={styles.detailsLabel}>Ships from</div><div className={styles.detailsText}>Amazing</div>
            </div>
            <div>
                <div className={styles.detailsLabel}>Sold by</div><div className={styles.detailsText}>Amazing</div>
            </div>
        </div>
    </div>);
}
