import styles from "./Tabs.module.css";

import { useRef } from "react";

export default function Tabs({ setShowDeliveryTab }) {

    const deliveryTabWrapperRef = useRef();
    const deliveryTabTextRef = useRef();

    const pickupTabWrapperRef = useRef();
    const pickupTabTextRef = useRef();

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
        </div>
    );
}
