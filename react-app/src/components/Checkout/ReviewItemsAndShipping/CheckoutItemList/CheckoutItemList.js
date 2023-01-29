import styles from "./CheckoutItemList.module.css";

import CheckoutItem from "./CheckoutItem/CheckoutItem";

export default function CheckoutItemList({ productDetails, cartItems, deliveryDateBig, deliveryDate, nextDeliveryDate, productIds }) {

    return <div className={`${styles.items}`}>
        <div>
            <span className={styles.bigDelivery}>Delivery: {deliveryDateBig}</span> <span className={styles.if}>If you order in the next 2 hours and 29 minutes
            </span>
            <div className={`${styles.if} ${styles.shippedFrom}`}>Items shipped from Amazing.com</div>
        </div>

        <div className={`${styles.flex}`}>
            <div>
                {productIds.map((productId, i) => <CheckoutItem key={i} product={productDetails[productId]} quantity={cartItems[productId]} />)}
            </div>

            <div>
                <div className={styles.choose}>Choose your Prime delivery option:</div>
                <input name="delivery" type="radio" id="delivery_0" defaultChecked={true} readOnly />
                <label htmlFor="delivery_0">
                    <span className={styles.date}>{deliveryDate}</span>
                    <div className={styles.free}>FREE <span className={styles.prime}>Prime Delivery</span></div>
                </label>
                <input name="delivery" type="radio" id="delivery_1" />
                <label htmlFor="delivery_1">
                    <span className={styles.date}>{nextDeliveryDate}</span>
                    <div className={styles.free}>FREE <span className={styles.prime}>Prime Delivery</span></div>
                </label>
            </div>
        </div>
    </div>
}
