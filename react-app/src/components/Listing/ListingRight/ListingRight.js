import styles from "./ListingRight.module.css";

import { useRef } from "react";

import Price from "../../Price/Price";
import { useState } from "react";

export default function ListingRight({ product }) {

    const deliveryTabWrapperRef = useRef();
    const deliveryTabTextRef = useRef();

    const pickupTabWrapperRef = useRef();
    const pickupTabTextRef = useRef();
    const [showDeliveryTab, setShowDeliveryTab] = useState(true);

    const onPickupTabClick = (e) => {
        setShowDeliveryTab(false);

        // Text
        deliveryTabTextRef.current.classList.remove(styles.activeTabText);
        pickupTabTextRef.current.classList.add(styles.activeTabText);

        // Tab
        deliveryTabWrapperRef.current.classList.remove(styles.activeTabWrapper);
        pickupTabWrapperRef.current.classList.add(styles.activeTabWrapper);
    }

    const onDeliveryTabClick = (e) => {
        setShowDeliveryTab(true);

        // Text
        pickupTabTextRef.current.classList.remove(styles.activeTabText);
        deliveryTabTextRef.current.classList.add(styles.activeTabText);

        // Tab
        pickupTabWrapperRef.current.classList.remove(styles.activeTabWrapper);
        deliveryTabWrapperRef.current.classList.add(styles.activeTabWrapper);
    }

    const onPickupTabMouseEnter = (e) => {
        e.target.classList.add(styles.tabWrapperMouseEnter);
        pickupTabTextRef.current.classList.add(styles.tabTextMouseEnter);
    }

    const onPickupTabMouseLeave = (e) => {
        e.target.classList.remove(styles.tabWrapperMouseEnter);
        pickupTabTextRef.current.classList.remove(styles.tabTextMouseEnter);
    }

    const onDeliveryTabMouseEnter = (e) => {
        e.target.classList.add(styles.tabWrapperMouseEnter);
        deliveryTabTextRef.current.classList.add(styles.tabTextMouseEnter);
    }

    const onDeliveryTabMouseLeave = (e) => {
        e.target.classList.remove(styles.tabWrapperMouseEnter);
        deliveryTabTextRef.current.classList.remove(styles.tabTextMouseEnter);
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.tabs}>
                <div
                    ref={deliveryTabWrapperRef}
                    onClick={onDeliveryTabClick}
                    onMouseEnter={onDeliveryTabMouseEnter}
                    onMouseLeave={onDeliveryTabMouseLeave}
                    className={`${styles.tabWrapper} ${styles.activeTabWrapper}`}
                >
                    <div>
                        <div
                            ref={deliveryTabTextRef}
                            className={`${styles.tabText} ${styles.activeTabText}`}
                        >
                            Delivery
                        </div>
                    </div>
                </div>
                <div
                    ref={pickupTabWrapperRef}
                    onClick={onPickupTabClick}
                    onMouseEnter={onPickupTabMouseEnter}
                    onMouseLeave={onPickupTabMouseLeave}
                    className={`${styles.tabWrapper} ${styles.pickupTabWrapper}`}
                >
                    <div>
                        <div
                            ref={pickupTabTextRef}
                            className={`${styles.tabText}`}
                        >
                            Pickup
                        </div>
                    </div>
                </div>
            </div>

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
