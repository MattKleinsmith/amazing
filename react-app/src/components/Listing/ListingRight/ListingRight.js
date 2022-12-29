import styles from "./ListingRight.module.css";

import { useState } from "react";

import Tabs from "./Tabs/Tabs";
import DeliveryTab from "./DeliveryTab/DeliveryTab";
import PickupTab from "./PickupTab/PickupTab";

export default function ListingRight({ product }) {
    const [showDeliveryTab, setShowDeliveryTab] = useState(true);
    return (
        <div className={styles.wrapper}>
            <Tabs setShowDeliveryTab={setShowDeliveryTab} />
            {showDeliveryTab && <DeliveryTab product={product} />}
            {!showDeliveryTab && <PickupTab product={product} />}
        </div>
    );
}
