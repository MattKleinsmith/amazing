import styles from "./ListingRight.module.css";

import Price from "../../Price/Price";
import { useState } from "react";
import Tabs from "./Tabs/Tabs";

export default function ListingRight({ product }) {
    const [showDeliveryTab, setShowDeliveryTab] = useState(true);

    return (
        <div className={styles.wrapper}>

            <Tabs setShowDeliveryTab={setShowDeliveryTab} />

            {showDeliveryTab && <div className={styles.content}>
                <div className={styles.price}>
                    <Price product={product} />
                    <div className={styles.count}>(${product.price} / Count)</div>
                </div>
                <div className={`prime ${styles.prime}`} />
                <div className={styles.freeReturns}>FREE Returns</div>
                <div className={styles.delivery}>FREE delivery <span className={styles.date}>Tuesday, December 27.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
                <div className={styles.address}></div>
                <div className={styles.inStock}>In Stock.</div>
                <div className={styles.quantity}>Qty: 1</div>
                <div className={styles.addToCart}>Add to Cart</div>
                <div className={styles.buyNow}>Buy Now</div>
                <div className={styles.secure}>Secure transaction</div>
                <div className={styles.fulfillment}>
                    <div className={styles.shipsFrom}>Secure transaction</div>
                    <div className={styles.soldBy}>Secure transaction</div>
                    <div className={styles.packaging}>Secure transaction</div>
                </div>

                <div className={styles.hr} />
            </div>}

            {!showDeliveryTab && <div className={styles.content}>
                <div>Pick up tab</div>
                <div className={styles.price}>
                    <Price product={product} />
                    <div className={styles.count}>(${product.price} / Count)</div>
                </div>
                <div className={`prime ${styles.prime}`} />
                <div className={styles.freeReturns}>FREE Returns</div>
                <div className={styles.delivery}>FREE delivery <span className={styles.date}>Tuesday, December 27.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
                <div className={styles.address}></div>
                <div className={styles.inStock}>In Stock.</div>
                <div className={styles.quantity}>Qty: 1</div>
                <div className={styles.buyNow}>Buy Now</div>
                <div className={styles.fulfillment}>
                    <div className={styles.shipsFrom}>Amazon</div>
                    <div className={styles.soldBy}>Amazon.com</div>
                </div>

                <div className={styles.hr} />
            </div>}
        </div>
    );
}
